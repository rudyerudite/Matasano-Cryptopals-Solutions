s=raw_input()
#incomplete code correcions to be made
pad=ord(s[-1:])
check=s[-pad:]
if(check==s[:-1]*pad or pad<=16 or pad!=0):
	print("cool")
else:
	print("error")


