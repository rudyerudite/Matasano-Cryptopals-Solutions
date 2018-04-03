import binascii

s=binascii.unhexlify(raw_input())
pad=ord(s[-1:])
check=s[-pad:]

print(len(s))
print(pad)
if(ord(s[16-pad])==pad and (check)==(s[-1:]*pad) and pad<=16 and pad!=0 ):
	print("cool")
else:
	print("error")


