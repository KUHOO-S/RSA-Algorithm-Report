from art import *
def gcd(a,b): 
	if b==0: 
		return a 
	else: 
		return gcd(b,a%b) 
tprint("\nWelcom to RSA IMPLEMENTATION\n")
print("Enter the message you want to encrypt")

a =60
b = 9
a+b

print("kuhoe")


p = int(input('Enter the value of p = ')) 
q = int(input('\nEnter the value of q = ')) 
String = input('\nEnter the value of text = ') 

l=[]

ciphertextlist =[]
deciphertextlist=[] 
for i in String:
    l.append(ord(i))
print(l)
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
  
print('\nn = '+str(n)+'\n\ne = '+str(e)+'\n\nt = '+str(t)+'\n\nd = '+str(d)+'\n\ninput(data) ==>'+String+'\n\n')
for data in l:   

    Sig = pow(data,e) % n 
    ciphertextlist.append(chr(Sig))
        
    Message = pow(Sig,d) % n 
    deciphertextlist.append(chr(Message))
    
    print(' cipher text = '+str(Sig)+' decrypted text = '+str(Message)) 
print("\nFinal Cipher Text (Sig)= ")
print(''.join(ciphertextlist))
tprint("\nFinal Deciphered Text (Message)= ")
print("This is the original message")
print(''.join(deciphertextlist))
if(Message==data):
    print('message==data hence signature and data is accepted')
