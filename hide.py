#/bin/env python3
import string

#convert key string to offset array
def convertKey(key):
    return [string.ascii_letters.find(c) for c in key]

#encode a text
#key must be an array of offsets used to roll each character in message 
#as in the Vigenere Cipher
def encode(text,key):
    cipher=""
    alph=string.ascii_letters
    for i,c in enumerate(text):
        cid=alph.find(c)
        k=key[i % len(key)]
        newid=(cid + k) % len(alph)
        cch=alph[newid]
        cipher+=cch
    return cipher

#decode a text encoded with the encode function
def decode(text,key):
    key = [ -x for x in key ] 
    return encode(text,key)


#test the encode/decode functions
def main():
    key="secret"
    plain="Thiscommunicationissecret"
    key=convertKey(key)
    encoded= encode(plain,key)
    print(f"Encoded message = {encoded}")
    print(f"Decoded message = {decode(encoded,key)}")



if __name__=="__main__":
    main()
