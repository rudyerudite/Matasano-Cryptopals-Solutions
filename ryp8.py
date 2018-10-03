import binascii

def detect(data):
	# The aim is to divide data into blocks and see whether there's any block similiar to it...so first find number of blocks
	n=len(data)/16
	print(" number of blocks are present :"+str(n/10))
	for i in range(n):
		s=data[i*16:(i+1)*16]
		for j in range(i+1,n):
			z=data[j*16:(j+1)*16]
			if(s==z):
					l=i
	return l
	    
data=""
with open("q8.txt") as f:
	for line in f:
		data+=binascii.unhexlify(line.strip())
k=detect(data)
print("block: "+str((k+1)/10))
