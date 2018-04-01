from Crypto.Cipher import AES

iv="\x00"*16
ct=""
d=AES.new("YELLOW SUBMARINE", AES.MODE_CBC,iv)

with open("q10.txt") as f:
	for line in f:
		line=(line.strip())
		ct+=line
pt=d.encrypt(ct)
print(pt)
