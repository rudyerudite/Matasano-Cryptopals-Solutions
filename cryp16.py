from Crypto.Cipher import AES
import os


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
	instr=instr.replace(';','?').replace('=','?')
	str1="comment1=cooking%20MCs;userdata="
	str2=";comment2=!20like!20a%20pound!20of%20bacon"
	ash=str1+instr+str2
	print(ash[32])
	str1=obj.encrypt(pkcs(str1+instr+str2,16))
	
	return str1		#returns a string that has been encrypted and padded

#check if you are the admin or not
def check(_str):
	obj1=AES.new(key,AES.MODE_CBC,iv)
	_str=obj1.decrypt(_str)
	print(_str)
	return ";admin=true;" in _str
#take in my payload i.e. basically admin=true???

def exploit(inp):
	#need to get the blocksize of the prefix so as to reach the crux
	print("Welcome to slytherin")
	ct=list(preapnd(inp))
	f="".join(ct)
	ctnw=""
	ct[16]=chr(ord(ct[16])^ord('?')^ord(';'))
	ct[22]=chr(ord(ct[22])^ord('?')^ord('='))
	ct[27]=chr(ord(ct[27])^ord('?')^ord(';'))
	ctnw="".join(ct)
	'''for i in range(len(f)) :
		if(f[i]!=ctnw[i]):
			print(ctnw[i],f[i])
			print("Ron's stupidity!")'''																						
	k=check(ctnw)
	if(k==True):
		print("Alohomora")
	else:
		print("I'm for Snape's detention tonight")

inp=";admin=true;"
exploit(inp)
#aim is to flip the bits ; and =

print("Expecto patronum!!!")
	
















