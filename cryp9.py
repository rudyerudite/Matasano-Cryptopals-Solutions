s= raw_input()
import binascii

block=q=""
flag=i=j=1
l=1
print("Original length is:"+str(len(s)))
while(flag!=0):
	l=len(s)
	if(l<16):
		block+=s+(binascii.hexlify(chr(16-l)))*((16-l)/2)
		j+=l	
		break
	elif(l>16):
		block+=s[0:16]
		s=s[16:l]

	else:
		block+=s
		break
	

print("Length of the padded block is:"+str(len(block)))
print(block)
	
