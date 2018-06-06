#padding oracle- something that would take the ciphertext from the user decrypt it privately and tell whether the padding is done correctly or not



from Crypto.Cipher import AES
import os
import random
import struct

key=os.urandom(16)
IV=os.urandom(16)
	
def pad(a):
	bs=16
	print(bs-len(a)%16)
	#this fn does apprp padding to whatever string it rcvs alongwith the blocksize here the resultant length is 96
	a+=chr(bs-(len(a)%bs))*(bs-(len(a)%bs))
	return a

def selrand():
	a=["MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=","MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=",
	"MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==","MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==","MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl",
	"MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==","MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==","MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=","MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=",
	"MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93"]
	
	i=random.randrange(0,9)
	print("Revealing the answer before...")
	print(a[i].decode('base64'))
	#print(len(a[i].decode('base64')))
	return pad(a[i].decode("base64"))
#we can pass ct of any length and it just has to tell us whether we have done correct padding or not
def encr():
	c=selrand()
	print(len(c))
	obj=AES.new(key, AES.MODE_CBC,IV)
	ques=obj.encrypt(c)
	print(ord(c[-1:]))
	return (IV+ques).encode("base64")
#encryption function works



def decr(inp):
	#print(len(inp))
	obj=AES.new(key, AES.MODE_CBC,IV)
	d=obj.decrypt(inp)

	#padding validation here
	
	last_byte=ord(d[-1:])
	check=d[-last_byte:] #takes in all the extra last_byteding characters 
	if(check==(d[-1:]*last_byte) and last_byte<=16 and last_byte!=0 ):

		return 1
	else:
		
		return 0

def exploit(inp,bp,adr):
	print("expecto Patronum!")
	print(adr)
	ans=""
	c1=fake=""
	flag=c=0
	if(adr==1):
		c2=inp[-16:]
	else:
		c2=inp[-16*adr:-(16)*(adr-1)]

	c3=inp[-16*(adr+1):-16*(adr)]
	for k in range(1,bp+1):
		c1=fake=""#to find corresponding plaintext bytes uptill bp-1
		#print("trial")
		for i in range (1,k):#to change the bytes after 16-bp so that they are modified afor padding
			#print('tobias')
			f=ord(ans[-i])^k^ord(c3[16-i]) #modifying the ctext after 
			#c1=c1[::-1]
			c1=chr(f)+c1
			#print(i,k)
		flag=c=0
		while(flag!=1):			
			c+=1
			fake="0"*(16-k)+chr(c)+c1
			flag=decr(fake+c2)
			if(flag==1):
				p=chr(k^ord(fake[-k])^ord(c3[16-k]))
				#print(ord(p))
				ans=p+ans
			if(c==255):
				print("couldn't find")
				break
	return ans
#one block decrypted sucessfully

def exp1():
	k=""
	l=encr()
	limit=(len(l)-16)/16
	for i in range(1,limit):
		k=exploit(l.decode("base64"),16,i)+k
	print("my final decrypted answer:")
	print(k)
exp1()