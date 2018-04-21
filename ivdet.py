from Crypto.Cipher import AES
import os

def pkcs(pt,bs):
	pt+=chr(bs-len(pt)%bs)*(bs-len(pt)%bs)
	return pt

def encrcbc(pt,bs):
	pt=pkcs(pt,bs)
	obj=AES.new(key,AES.MODE_CBC,IV)
	ct=obj.encrypt(pt)
	return ct

def decrcbc(ct,bs):
	k=len(ct)
	l=[]
	ct1=ct+"\x00"*16+ct #using a null string as my guessed ciphertext block string
			    #I'm not padding it b4 decryption of the combined strings
	obj=AES.new(key,AES.MODE_CBC,IV)
	pt1=obj.decrypt(ct1)
	l=[chr(ord(a)^ord(b)) for a,b in zip(pt1[:16],pt1[16+k:])]
	hg="".join(l)
	if(IV==hg):	   #comparing predicted IV with actual one
		print("You got the snitch!")
	else:
		print("Slytherin gets a point")

key="Yellow Submarine"
IV=os.urandom(16)
s="I solemnly swear that I'm upto no good"
pt=s.encode("base64")
bs=16
cipher=encrcbc(pt,bs)
decrcbc(cipher,bs)
	






	




