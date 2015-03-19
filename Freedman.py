#!/usr/bin/python
# -*- coding: utf-8 -*-
plain_file = open('plain.txt', 'r')
cipher_file = open('cipher.txt', 'r')
plain_freq = {}
cipher_freq = {}
n = 0

def init_freq():
	for alpha in range(0+65, 26+65):
		plain_freq[chr(alpha)] = 0
		cipher_freq[chr(alpha)] = 0

def ic():
	global n
	counter = 0
	for line in plain_file:
		for char in line:
			if char.isalpha():
				plain_freq[char] += 1
				counter += 1
	for line in cipher_file:
		for char in line:
			if char.isalpha():
				cipher_freq[char] += 1

	for alpha in range(0+65, 26+65):
		plain_freq[chr(alpha)] /= float(counter)
		cipher_freq[chr(alpha)] /= float(counter)

	plain_ic = 0
	cipher_ic = 0
	for (alpha, freq) in plain_freq.items():
		plain_ic += freq * freq
	for (alpha, freq) in cipher_freq.items():
		cipher_ic += freq * freq
	print plain_ic
	print cipher_ic
	n = int((0.067 - 0.0385) / (cipher_ic - 0.0385))
	print n

def key():
	global cipher_file
	i = 0
	cipher_file.close()
	cipher_file = open('cipher.txt', 'r')
	for line in cipher_file:
		for char in line:
			if char.isalpha():
				if i % n == 0:
					cipher_freq[char] += 1
				i = i + 1
	e = 'E'
	max_freq = 0
	for (alpha, freq) in cipher_freq.items():
		if freq > max_freq:
			max_freq = freq
			e = alpha

	print (ord(e) - ord('E')) % 26

def main():

	init_freq()
	ic()
	init_freq()
	key()

if __name__ == '__main__':
	main()