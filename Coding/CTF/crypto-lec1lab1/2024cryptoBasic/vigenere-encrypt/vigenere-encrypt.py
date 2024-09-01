from random import randrange

text_list=' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\t\n'

key=[randrange(1,97) for _ in range(randrange(15,30))]

print('key = '+str(key))

def encrypt(s,k): # k->key 
    out=''
    for i in range(len(s)):
        index=text_list.index(s[i]) # orginal index
        index*=k[i%len(k)] # index encrypt through mutiply
        index%=97
        out+=text_list[index] # abstract string
    return out

plain=open('plain.txt','r').read() # TOEFL reading passage
cipher=encrypt(plain,key)
open('cipher.txt','w').write(cipher)

# for decrypt, get the index of the encrypted_str(a=91) and the original index(b=84), (84*k)%97=91 then get k
# ∴ output*k=pow(original_index,-1,97)