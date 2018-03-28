
import binascii
from operator import itemgetter

def hamdist(a,b):
	a=bin(int(binascii.hexlify(a),16))[2:]		#could have also used the xor approach... xor 2 strings and count the number of 1's
	b=bin(int(binascii.hexlify(b),16))[2:]

	c=i=0
	while(i<len(a) and i<len(b)):
		if(a[i]!=b[i]):
			c+=1
		i=i+1
	return c

l=bytearray("".join(list(open("q5.txt","r"))).decode("base64"))
 #converts the data of the whole file from base64 to ascii...referred https://cypher.codes/writing/cryptopals-challenge-set-1
hds=[]
for k in range(2,40):	#slicing strings as per the bytes and then finding the HD b/w 2 adjacent set of byte strings
	s1=l[:k]
	s2=l[k:k*2]
	s3=l[k*2:k*3]
	s4=l[k*3:k*4]		#in total I've taken 3 sliced parts so that the avg of 3 can be taken and extremeties cancel out?

	hd=float(hamdist(s1,s2)+hamdist(s2,s3)+hamdist(s3,s4))/3
	hds.append((k,hd/k)) #normalised hamming distance...append with the chosen key length values

print(sorted(hds,key=itemgetter(1)))

for i in range(len(hds))
	r=""
	for