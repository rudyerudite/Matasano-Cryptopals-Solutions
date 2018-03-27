import binascii

def xor(s1,s2):
	return "".join(chr(ord(a)^ord(b))for a,b in zip(s1,s2)).encode("hex")

pt=raw_input()
key='ICE'
r=""
for i in range(0,len(pt),3):
	s=pt[i:i+3]
	print(s)
	r+=xor(s,key)
	
print(r)

