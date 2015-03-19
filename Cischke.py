# -*- coding: utf-8 -*-
cipher_text = []
shift = []
prefix = ''
counter = -1

row = -1
line = 0

def getchar():
	global row
	global line
	row += 1
	if row == len(cipher_text[line]):
		line += 1
		row = 0

	if line == len(cipher_text):
		return "EOF"

	return cipher_text[line][row] 

def ungetc():
	global row
	global line
	row -= 1
	if row < 0:
		line -= 1
		row = len(cipher_text[line]) - 1

	return cipher_text[line][row]

def scanner():
	global counter
	char = getchar()
	counter += 1
	if char == 'EOF':
		return 'EOF'
	while True:
		if char == prefix[0]:
			char = getchar()
			counter += 1
			if char == 'EOF':
				return 'EOF'
			if char == prefix[1]:
				char = getchar()
				counter += 1
				if char == 'EOF':
					return 'EOF'
				if char == prefix[2]:
					return counter - 2
				else:
					char = ungetc()
					counter -= 1
		else:
			char = getchar()
			counter += 1
			if char == 'EOF':
				return 'EOF'

def divisor(s):
	d = []
	for i in range(2, s):
		if s % i == 0:
			d.append(i)
	return d

def main():
	global cipher_text
	global prefix
	global counter
	cipher_file = open('cipher.txt', 'r')
	cipher_text = cipher_file.readlines()
	cipher_file.close()
	for i in range(1, 6):
		prefix = getchar() + getchar() + getchar()
		counter += 3
		print prefix
		r = scanner()
		if r == 'EOF':
			break;
		if r is not None:
			print r
			shift.append(r)

	for i in range(len(shift) - 1, 0, -1):
		shift[i] = shift[i] - shift[i-1] - 3

	for i in range(0, len(shift)):
		shift[i] = divisor(shift[i])
	
	print shift


if __name__ == '__main__':
	main()