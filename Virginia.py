import sys
import random

def main():
	k = []
	n = int(raw_input())
	for i in range(n):
		k.append(random.randint(1, 26))
	print k

	plain_file = open('plain.txt', 'r')
	cipher_file = open('cipher.txt', 'w')

	i = 0
	for line in plain_file:
		for char in line:
			if char.isalpha():
				cipher = (ord(char.upper()) - 65 + k[i%n]) % 26 + 65
				cipher_file.write(chr(cipher))
				i = i + 1

	plain_file.close()
	cipher_file.close()

	cipher_file = open('cipher.txt', 'r')
	dec_file = open('dec.txt', 'w')

	i = 0
	for line in cipher_file:
		for char in line:
			if char.isalpha():
				dec = (ord(char) - 65 - k[i%n]) % 26 + 65
				dec_file.write(chr(dec))
				i = i + 1

	cipher_file.close()
	dec_file.close()


if __name__ == '__main__':
	main()