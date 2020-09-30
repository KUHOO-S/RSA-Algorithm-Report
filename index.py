
from decimal import Decimal 

def gcd(a,b): 
	if b==0: 
		return a 
	else: 
		return gcd(b,a%b) 
p = int(input('Enter the value of p = ')) 
q = int(input('Enter the value of q = ')) 
String = input('Enter the value of text = ') 
print(String)
l=[]
ciphertextlist =[]
deciphertextlist=[] 
for i in String:
    l.append(ord(i))
print(l) 
for data in l:   

    n = p*q 
    t = (p-1)*(q-1) 

    for e in range(2,t): 
        if gcd(e,t)== 1: 
            break


    for i in range(1,10): 
        x = 1 + i*t 
        if x % e == 0: 
            d = int(x/e) 
            break
  
    ct = pow(data,e) % n 
    ciphertextlist.append(chr(ct))
        
    dt = pow(ct,d) % n 
    deciphertextlist.append(chr(dt))
    
    print('n = '+str(n)+' e = '+str(e)+' t = '+str(t)+' d = '+str(d)+' cipher text = '+str(ct)+' decrypted text = '+str(dt)) 
print(ciphertextlist)
print(deciphertextlist)
