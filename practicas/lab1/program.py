#Hill Cipher
#
#author: Morales Ortega Carlos
import fileinput

#Variables a utilizar
do=[]
key=[]
plain_text=[]
matrix_key = [['',''],['','']]

# Métodos 
def key_c():
    matrix_key[0][0] = key[0]
    matrix_key[0][1] = key[1]
    matrix_key[1][0] = key[2]
    matrix_key[1][1] = key[3]
    print(matrix_key)

def cipher():
    key_c()
    

def decipher():
    print(lines)
    print("Se va a descifrar")

def limpia():
    for i in lines[0]:
        aux=i.replace('\n','')
        do.append(aux.upper() )
    do.remove('')

    for i in lines[1]:
        aux=i.replace('\n','')
        plain_text.append(aux.upper() )
    plain_text.remove('')

    for i in lines[2]:
        aux=i.replace('\n','')
        key.append( aux.upper() )
    key.remove('')

# Lectura de argumentos e inicio de programa

lines = []
for line in fileinput.input():
    lines.append(line)

# do something with the lines array
if(len(lines)==3):
    
    limpia()
    if(do[0] =='C'):
        cipher()
    elif (do[0] == 'D'):
        decipher()
    else: 
        print(do)
        print(plain_text)
        print(key)
        print("Invalid input")
else:
    print(len(lines))
    print("Invalid inputs")

