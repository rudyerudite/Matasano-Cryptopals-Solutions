import binascii

pt=raw_input()
key='ICE'
j=0
r=""
for i in range(len(pt)):
	r+="".join(chr(ord(pt[i])^ord(key[j])))
	j+=1
	if(j%3==0):
		j=1
print(binascii.hexlify(r))