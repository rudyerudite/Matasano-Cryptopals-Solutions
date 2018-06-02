from Crypto.Cipher import AES
import Crypto.Util.Counter
import struct

ct=("L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==").decode("base64")
key="YELLOW SUBMARINE"
nonce=0
count=0

l=((struct.pack("<Q",nonce))) #nonce+count is used as a key stream together
ltr=Crypto.Util.Counter.new(64, prefix=l, initial_value=count,little_endian=True) #rest of the 64 bits will belong to nonce this fn will be for count
obj=AES.new(key,AES.MODE_CTR,counter=ltr) #counter keyword is necessary
print(obj.decrypt(ct)) 


