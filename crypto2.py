def xor(s1,s2):
	return "".join(chr(ord(a)^ord(b))for a,b in zip(s1,s2)).encode("hex")

s1=raw_input()
print("Now give me the key")
s2=raw_input()

s1=s1.decode("hex")
s2=s2.decode("hex")

print(xor(s1,s2))
