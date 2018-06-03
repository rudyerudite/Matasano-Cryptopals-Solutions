from Crypto.Cipher import AES
import Crypto.Util.Counter
import os
import struct

#server side encryption function
key=os.urandom(16)
nonce=os.urandom(8)#is this right?
count=0

def encr1(ash):
	ltr=Crypto.Util.Counter.new(64, prefix=nonce, initial_value=count) #rest of the 64 bits will belong to nonce this fn will be for count
	obj=AES.new(key,AES.MODE_CTR,counter=ltr)
	return(obj.encrypt(ash))


def encr2(inp):
	pre="comment1=cooking%20MCs;userdata="
	app=";comment2=%20like%20a%20pound%20of%20bacon"
	inj=lambda inp: inp.replace(';','?').replace('=','?')
	ash=pre+inj(inp)+app
	return (encr1(ash)).encode("base64")
#server side decryption
def decr1(ash):
	ltr=Crypto.Util.Counter.new(64, prefix=nonce, initial_value=count) #rest of the 64 bits will belong to nonce this fn will be for count
	obj=AES.new(key,AES.MODE_CTR,counter=ltr)
	return(obj.decrypt(ash))

def decr2(inp):
	dec=decr1(inp)
	print(dec)
	if ";admin=true;" in dec:
		print("flipping sucessfull")
	else:
		print("flipping unsucessfull")

def exploit(ques):
	ques=list(ques)
	ques[32]=chr(ord(ques[32])^ord('?')^ord(';'))
	ques[38]=chr(ord(ques[38])^ord('?')^ord('='))
	ques[43]=chr(ord(ques[43])^ord('?')^ord(';'))
	return "".join(ques)



inp=";admin=true;"
ques=encr2(inp)
ans=exploit(ques.decode("base64"))
decr2(ans)


#print(decr2(ques.decode("base64"))) decryption function works


