import binascii

def xor(line):
	for j in range(0,255):
		r=""
		for i in range(len(line)):
			r+=chr(ord(line[i])^j)	
		print(r)
c=0
with open('ques4.txt') as f:
	for line in f:
		print(str(line))
		line=binascii.unhexlify(line.strip())
		print(c)
		c+=1
		xor(line)