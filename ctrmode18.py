from Crypto.Cipher import AES
import Crypto.Util.Counter
import struct
ct=("L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==").decode("base64")
key="YELLOW SUBMARINE"
nonce=0	#understand it is as nonce+intial counter
nonce=struct.pack("<Q",nonce).encode("hex") #applying little endian format || o/wise arg gives error
print (nonce)
ctr=Crypto.Util.Counter.new(128, initial_value=nonce) #when not usinng this prompting error counter must be a callable object
obj=AES.new(key,AES.MODE_CTR,counter=ctr) #counter keyword is necessary
print(obj.decrypt(ct)) #not giving me out the  whole text correctly Yo, VIP Let's ki�g�[�~g�ﲇ�Bh�*�	�!����5��8�e��


