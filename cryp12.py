
from Crypto.Cipher import AES
import os

def pkcs(a,bs):	#this fn does apprp padding to whatever string it rcvs alongwith the blocksize
	p_len = lambda inp: (bs - len(inp) % bs)
	p = lambda inp: inp + chr(p_len(inp))*p_len(inp)
	return p

def rkey(): # ur random key generated 
	key=os.urandom(16)
	return key
#here's the box!!! put a pt and there u get ur ct!
def encrypt(pt,a):
	k=rkey()
	pt=pkcs(pt+a,16) #pt+unkonwn string is passed for padding
	aobj=AES.new(k,AES.MODE_ECB)
	ct=aobj.encrypt(pt)
	return ct

def detect_ecb(a):
	n=len(a)
	l=0
	for i in range(n):
		s=data[i*16:(i+1)*16]
		for j in range(i+1,n):
			z=data[j*16:(j+1)*16]
			if(s==z):
					l=1
					break
	return l



#divide the input string into diff. bytes by using byteaarray...bytearrays usually create a list of mutable obj, string...each char reffrd singly?
#i thought it might separate my input into each diff bytes


a=bytearray("".join(list(open("q12.txt","r"))).decode("base64"))
true=detect_ecb(a)
if(true==1): #only executed if ecb mode is detected
	encrypt(pt,a) # here I think pt will be smth from my lib and a will be my unk string
	
print(a)

#random key generation 

