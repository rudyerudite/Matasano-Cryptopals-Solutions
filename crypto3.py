def xor1(s):
	for j in range(0,255):
		r=""
		for i in range(len(s)):
			r+=chr(ord(s[i])^j)	
		print(r)



import binascii
s=raw_input() 
s=binascii.unhexlify(s)
xor1(s)




 