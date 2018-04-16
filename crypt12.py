from Crypto.Cipher import AES
import os

s="a"*15

def rkey(): # ur random key generated 
	key=os.urandom(16)
	return key

def pkcs(a,bs):
	#this fn does apprp padding to whatever string it rcvs alongwith the blocksize
	a+=chr(bs-(len(a)%bs))*(bs-(len(a)%bs))
	return a

def trial1(b,q,s):
	ans=""
	for i in range(0,q):
		ct=s+chr(b[i])
		pt=obj.decrypt(ct)
		l=str(trial2(s,pt))
		ans+=l
		s=ct[1:]
	return ans

def trial2(s,pt):
	for i in range(256):
		zc=s+chr(i)
		zp=obj.decrypt(zc)
		if(zp==pt):
			return chr(i)

obj=AES.new(rkey(),AES.MODE_ECB)

a=bytearray("".join(list(open("q12.txt","r"))).decode("base64"))	#decoding the current data from base64
b=pkcs(a,16)
u=trial1(a,len(b),s)
print(u)
														#padding the given data for fitting blocksize 16
