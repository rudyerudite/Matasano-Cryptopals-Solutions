CAP={' ':'27','E':'26','T':'25','A':'24','O':'23','I':'22','N':'21','S':'20','R':'19','H':'18','D':'17','L':'16','U':'15',
'C':'14','M':'13','F':'12','Y':'11','W':'10','G':'9','P':'8','B':'7','V':'6','K':'5','X':'4','Q':'3','J':'2','Z':'1'}

SML={'e':'26','t':'25','a':'24','o':'23','i':'22','n':'21','s':'20','r':'19','h':'18','d':'17','l':'16','u':'15','c':'14',
'm':'13','f':'12','y':'11','w':'10','g':'9','p':'8','b':'7','v':'6','k':'5','x':'4','q':'3','j':'2','z':'1'}

#above are my two dictionaries for keeping track of the letter frequency
import binascii

k=[]

def xor(line):
	s=0
	for j in range(0,1):
		r=""
		for i in range(len(line)):
			r+=chr(ord(line[i])^j)
			s=CAP.get(r[i],0)
			if(s==0):
				s=SML.get(r[i],0)
		if(r.isprintable()):			#to be edited use anothe fn other than isprintable to check
			print(r)
			k.append(r)
		return s
c=p=x=0
#with open('ques4.txt') as f:
if(x==0):
	#for line in f:
		line='371d39121605584f48217235ee1e0602445c162e4942254c071954321d29'
		line=binascii.unhexlify(line.strip())
		c+=1
		m=xor(line)
		if(m>p):
			p=m				#to be used somewehre else
print(s[p])
