#of the form b=a^x mod p
#split x=i*m+j
#g**im * g*j eqv to b mod p
#g**im eqv to b*g^-j mod p
import math
from Crypto.Util.number import *

a,b,p=map(int, raw_input().split())
m=int(math.sqrt(p-1)+1)

l=[]
for i in range(0,m):#why is the limit m?
	l.append(pow(a,i*m,p))#root m number of possibilities

for j in range(0,m):
	for k in range(m):
		if((pow(b*inverse(pow(a,j),p),1,p)) in l):
			break
	break
x=j*m+k
print(x)
