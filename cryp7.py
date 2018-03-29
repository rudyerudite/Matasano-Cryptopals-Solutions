from Crypto.Cipher import AES

s=AES.new("YELLOW SUBMARINE",AES.MODE_ECB) #creates an encryptor object and give it encryption
ct=""										   #key and the mode
with open("q7.txt") as f:
	for line in f:
		line=(line.strip()).decode("base64")
		ct+=line
		#ct="".join(list(open("q7.txt","r"))).decode("base64")
pt=s.decrypt(ct)
print(pt)