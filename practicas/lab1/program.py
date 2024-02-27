#Hill Cipher
#
#author: Morales Ortega Carlos
import fileinput, math

#Variables a utilizar
lines = []

letras={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,
        'L':11,'M':12,'N':13,'Ñ':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,
        'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}

################################################################################
def do_matrix(to_matrix):
    
    matrix=[]
    aux=[]
    for i in range (2):
        aux=[]
        for j in range (2):
            aux.append(letras.get(to_matrix[2 * j + i]))
        matrix.append(aux)
    return matrix

def do_vector(to_matrix):
    
    vector=[]
    for i in range(0,len(to_matrix),2):
        aux_vector=[]
        for j in range (2):
            aux_vector.append(letras.get(to_matrix[i+j]))
        vector.append(aux_vector)
    return vector

def mxv(matrix, vector):
    
    resultado=[]
    for aux in vector: 
        aux_resultado=[]
        for i in range (2):
            mod=0
            for j in range (2):
                mod += matrix[i][j] * aux[j]
            aux_resultado.append(mod % 26) 
        resultado.append(aux_resultado)
    
    return resultado

def msg(matrix):
    message = ''
    for vector in matrix:
        for x in vector:
            for key,value in letras.items():
                if x==value:
                    message+=key
    
    return message

def cipher(key, plain_text):
    matrix_key= do_matrix(key)
    aux_vector= do_vector(plain_text)
    final=mxv(matrix_key,aux_vector)
    d=msg(final)
    print(d)
    

def decipher():
    print(lines)
    print("Se va a descifrar")

def start(): #This method put the inputs in list withou \n
    do=[]
    key=[]
    plain_text=[]

    for i in lines[0]:
        aux=i.replace('\n','')
        do.append(aux.upper() )
    do.remove('')

    for i in lines[1]:
        aux=i.replace('\n','')
        plain_text.append(aux.upper() )
    plain_text.remove('')
    if(len(plain_text)%2!=0):
        plain_text.append('X')
    print(plain_text)

    for i in lines[2]:
        aux=i.replace('\n','')
        key.append( aux.upper() )
    key.remove('')

    if(do[0] =='C'):
        cipher(key,plain_text)
    elif (do[0] == 'D'):
        decipher()
    else: 
        print("Invalid input")
################################################################################
    
# Input reading and start of the program

for line in fileinput.input():
    lines.append(line)

# do something with the lines array
if(len(lines)==3):  
    start()
else:
    print("Invalid inputs")

