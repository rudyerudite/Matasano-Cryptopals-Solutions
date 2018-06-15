from Crypto.Cipher import AES
import Crypto.Util.Counter 
import os
import struct
from collections import Counter
import string

key="YELLOW SUBMARINE"
nonce=struct.pack("<Q",0)

def encr():#each line is stor3d as diff entity in list
	ct1=[]
	small=100000
	with open("q20.txt","r") as f:
		for line in f:
			ct1.append(encrypt1(line.decode("base64")))

	return ct1

def encrypt1(ct):
	count=0
	ctr=Crypto.Util.Counter.new(64,prefix=nonce,initial_value=count)
	obj=AES.new(key,AES.MODE_CTR,counter=ctr)
	return obj.encrypt(ct)
#abv code applies for server side encryption

def cut(ct):
	small=10000
	for i in range(len(ct)):
		if(len(ct[i])<small):
				small=len(ct[i])
			
	for i in range(len(ct)):
		ct[i]=ct[i][:small]
	print(small,len(ct))
	ct=trans(ct,small,len(ct))
	freq1(ct,small,len(ct))

	return

def trans(ct,small,c):
	ct1=[]

	for i in range(small):
		q=""
		for j in range(c):
			q+=ct[j][i]
		ct1.append(q)
	return ct1

def freA(s,small):
	count=Counter(s) #would make a dictioary
	ac=sum(count[l] for l in string.ascii_letters+' ')
	if((ac*100/small)>=80):
		pc=sum(count[l] for l in string.punctuation)
		if((pc*100/small)<=10):
			freq={'e':12.49,'t':9.28,'a':8.04,'o':7.64,'i':7.57,'n':7.23,'s':6.51,'r':6.28,'h':5.05,'l':4.07,
			'd':3.28,'c':3.34,'u':2.73,'m':2.51,'f':2.40,'p':2.14,'g':1.87,'w':1.68,'y':1.66,'b':1.48,'v':1.05,'k':0.54,
			'x':0.23,'j':0.16,'q':0.12,'z':0.09}
			fc=sum(count[l] for l in freq)
			return fc
	else:
		return 1

def final(ct,test,small):
	f=encr()
	for i in range(len(f)):
		s=""
		s="".join(chr(ord(a)^ord(b)) for a,b in zip(f[i],test))
		print(s)


def freq1(ct,small,c):
	test=""
	for i in range(small):
		sm=0
		for k in range(256): 
			s=""
			for j in range(c):
				s+=chr(ord(ct[i][j])^k)
			#if(i==0):
				#print s
				
			z=freA(s,c)
			if(z!=1):
				if(z>sm):
					sm=z
					high=k
			if(k==255):
				test+=chr(high)
	print(test)
	print(len(test))
	final(ct,test,small)



text=encr()
cut(text)
