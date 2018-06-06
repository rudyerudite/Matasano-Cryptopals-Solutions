from Crypto.Cipher import AES
import os
import random
import struct

key=os.urandom(16)
IV=os.urandom(16)
	
def pad(a): #padding function
	bs=16
	print(bs-len(a)%16)
	a+=chr(bs-(len(a)%bs))*(bs-(len(a)%bs))
	return a

def selrand(): #server selects any random string 
	a=["MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=","MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=",
	"MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==","MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==","MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl",
	"MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==","MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==","MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=","MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=",
	"MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93"]
	
	i=random.randrange(0,9)
	print("Revealing the answer before...")	#done for checking purpose
	print(a[i].decode('base64'))
	return pad(a[i].decode("base64"))		#string is padded aand send to encr

def encr():
	c=selrand()								
	obj=AES.new(key, AES.MODE_CBC,IV)		
	ques=obj.encrypt(c)						#encrypt the string and send it 
	return (IV+ques).encode("base64")

def decr(inp):								#decrypt function so as to validate the padding...ths is the padding oracle
	obj=AES.new(key, AES.MODE_CBC,IV)
	d=obj.decrypt(inp)
	last_byte=ord(d[-1:])
	check=d[-last_byte:] 					#returns 1 if valid o/wise returns 0
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
	if(adr==1):								#c2 will be my ciphertext which'll be appended to my cusstom ciphertext
		c2=inp[-16:]						#c2 is selected depending on the block which's to be decrypted
	else:									#c2 will be used for finding all the bytes in a block
		c2=inp[-16*adr:-(16)*(adr-1)]

	c3=inp[-16*(adr+1):-16*(adr)]			#c3 is the ciphertext block selected previous to the one which is used for appending
	for k in range(1,bp+1):
		c1=fake=""							
		for i in range (1,k):
			f=ord(ans[-i])^k^ord(c3[16-i])
			c1=chr(f)+c1					#used for decrypting second-,third-... bytes 
		flag=c=0							#c is our iter value... probability for getting the right c is 1/256
		while(flag!=1):			
			c+=1
			fake="0"*(16-k)+chr(c)+c1		#my custom ciphertext 
			flag=decr(fake+c2)				#appending custom one with c2 
			if(flag==1):					#if the chosen c was right then this eq used for finding actual plaintext
				p=chr(k^ord(fake[-k])^ord(c3[16-k])) 
				ans=p+ans
			if(c==255):
				print("couldn't find")
				break
	return ans

def exp1():
	k=""
	l=encr()
	limit=(len(l)-16)/16					#dividing into blocks
	for i in range(1,limit):
		k=exploit(l.decode("base64"),16,i)+k
	print("my final decrypted answer:")
	print(k)
exp1()

#\x01 considered valid padding
#We're modifying the last byte of our custom ct to get valid padding. why only this one is valid? Well, the rest 15 bytes will be treated as 
#part of string. c2[n-1] when decrypted will have a very rare chance of being the same as the last byte of P2'. 
