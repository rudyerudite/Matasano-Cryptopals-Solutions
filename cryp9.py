s= raw_input()
import binascii

block=q=""
flag=1
print("Original length is:"+str(len(s)))
while(flag!=0):
	l=len(s)
	if(l<16):
		amt=16-l%16
		p = binascii.unhexlify('%02d' % amt)
		block+=s+p*amt
			
		break
	elif(l>16):
		block+=s[0:16]
		s=s[16:l]

	else:
		block+=s+(binascii.unhexlify('%02d' % 16))*16
		
		break
	

print("Length of the padded block is:"+str(len(block)))
print(block)
	
