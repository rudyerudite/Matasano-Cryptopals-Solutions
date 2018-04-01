s= raw_input()


block=q=""
flag=i=j=0
print("Original length is:"+str(len(s)))
while(flag==0):
	l=len(s)
	if(l<16):
		while(i<16-l):
			q+="\x01"
			i+=1
		block+=s+q
		break
	elif(l>16):
		block+=s[0:16]
		s=s[16:l]
	else:
		block+=s
		break
print("Length of the padded block is:"+str(len(block)))

	