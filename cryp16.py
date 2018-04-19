from Crypto.Cipher import AES
import os
import binascii

 # ur random key generated for encryption in CBC mode
key=os.urandom(16)
iv=os.urandom(16)
obj=AES.new(key,AES.MODE_CBC,iv)

def pkcs(a,bs):
	#this fn does apprp padding to whatever string it rcvs alongwith the blocksize here the resultant length is 96
	a+=chr(bs-(len(a)%bs))*(bs-(len(a)%bs))
	return a

#getting the encrypted text as str1+payload+str2
def preapnd(instr):#appending and prepending the input with random strings and then paddding the resultant and encrypting it
				   #this is supposed to be my supplied main encryption fn and I have to exploit it 
	instr=instr.replace(';','$').replace('=','$')
	str1="comment1=cooking%20MCs;userdata="
	str2=";comment2=!20like!20a%20pound!20of%20bacon"
	#print(str1+instr+str2)
	str1=obj.encrypt(pkcs(str1+instr+str2,16))
	
	return str1		#returns a string that has been encrypted and padded

#check if you are the admin or not
def check(_str):
	_str=obj.decrypt(_str)
	print(_str)
	return ";admin=true;" in _str
#take in my payload i.e. basically admin=true???

def exploit(inp):
	#need to get the blocksize of the prefix so as to reach the crux
	print("Welcome to slytherin")
	ct=list(preapnd(inp))
	ctnw=""
	#ct1=list(ct[32:48])
	#k=""
	#ct1[0]=chr((ord(ct1[0])^ord("$"))^ord(";"))
	#ct1[6]=chr((ord(ct1[6])^ord("$"))^ord("="))
	#ct1[11]=chr((ord(ct1[11])^ord("$"))^ord(";"))
	#fg="".join(ct1)
	#ctnw=ct[:32]+fg+ct[48:]
	print(obj.decrypt(ct[32]))
	ct[32]=chr((ord(ct[32])^ord("$"))^ord(";"))
	ct[38]=chr((ord(ct[38])^ord("$"))^ord("="))
	ct[43]=chr((ord(ct[43])^ord("$"))^ord(";"))
	ctnw="".join(ct)
	k=check(ctnw)
	print(k)
	if(k=="True"):
		print("Alohomora")
	else:
		print("I'm for Snape's detention tonight")

inp=";admin=true;"
exploit(inp)
#aim is to flip the bits ; and =

print("Expecto patronum!!!")
	
















