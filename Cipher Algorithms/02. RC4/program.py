#author: Morales Ortega Carlos
import fileinput

# Variable
lines = []

################################################################################
def KSA(S,ascii_key):
    keylength = len(ascii_key)      #Length of key
    j=0
    for i in range (256):
        j = (j + S[i] + ascii_key[i % keylength]) % 256
        S[i] , S[j] = S[j] , S[i]   #SWAP 

def PRGA(S):
    i=0
    j=0
    #We use a generator function for every time we need 
    #the PRGA algorithm
    while True:
        i = (i+1) % 256
        j = (j + S[i]) % 256
        S[i] , S[j] = S[j] , S[i]   #SWAP
        K= S[(S[i] + S[j]) % 256]   
        yield format(K, '02X')      #We use yield for pause/continue
                                    #and get 'K' in HEX


def RC4(ascii_key):
    S= [i for i in range (256)]     #Fill vector S[0]=0 ... S[255]=255
    KSA(S, ascii_key)               #KSA Algorithm
    return PRGA(S)

def RC4_encrypt(key, plain_text):
    ascii_key = [ord(char) for char in key] #ASCII value char by char
                                            #of our key
    
    keystream = RC4(ascii_key)

    encrypted_text= ""
    for char in plain_text:
        keystream_byte = next(keystream)    #Continue geerating keystream
        encrypted = ord(char) ^ int(keystream_byte, 16) #Plaintext XOR Final K
        encrypted_text += format(encrypted, '02X')  #Convert HEX and fill 0 if its the case

    print(encrypted_text)

def start(): #This function put the inputs in a list without \n
    key=[]
    plain_text=[]


    for i in lines[0]:
        aux=i.replace('\n','')
        key.append(aux)
    if '' in key:
        key.remove('')
    

    for i in lines[1]:
        aux=i.replace('\n','')
        plain_text.append(aux)
    #for the case that after enter the key didin´t press "enter"
    if '' in plain_text:
        plain_text.remove('')

    RC4_encrypt(key, plain_text)


################################################################################
# Main
################################################################################
# Input reading and start of the program
for line in fileinput.input():
    lines.append(line)

# do something with the lines array
if(len(lines)==2):  
    start()
else:
    print("Invalid inputs")
