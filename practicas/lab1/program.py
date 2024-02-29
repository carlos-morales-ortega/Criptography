"""
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░              ░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░       ░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
"""
#author: Morales Ortega Carlos
import fileinput, math

#Variables
lines = []

#We use a dicctionary in order to associate a letter with a key
letters={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,
        'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,
        'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}

################################################################################
########## FUNCTIONS
################################################################################

def do_matrix(to_matrix): #This functions convert a given list into a matrix 2x2
    matrix=[]
    aux=[]

    #   [1][3],[2][4] 
    for i in range (2):
        aux=[]
        for j in range (2):
            aux.append(letters.get(to_matrix[2 * j + i]))
        matrix.append(aux)
    return matrix

def do_vector(to_matrix): #This function convert a list into a matrix used as vectors per row
    vector=[]
    # [[00,01],[10,11],[20,21]...]
    for i in range(0,len(to_matrix),2):
        aux_vector=[]
        for j in range (2):
            aux_vector.append(letters.get(to_matrix[i+j]))
        vector.append(aux_vector)
    return vector

def det_key(matrix): #This function obtains the determinant of a 2x2 matrix
    det=0
    det=(matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0])       #simply operations
    if det == 0:
        print("Error")

    return det

def mod26(val): #This function solves equation x*y % 26 = 1
    for i in range (1,27,1):
        if(val*i) % 26 == 1:
            return i

def adj_matrix(matrix): #This function obtins de adj of a matrix
    adj = []
    adj = [ [matrix[1][1], -matrix[0][1]],              # simply operations
            [-matrix[1][0], matrix[0][0]] ]
    return adj

def do_inv(det, adj):   #This function obtains the inverse we use
                        # det (already with mod) and the adj
    
    inv=[]
    for i in range(2):
        aux=[]
        for j in range(2):
            aux.append(det*adj[i][j] % 26)              # simply operations
        inv.append(aux)
    
    return inv

def mxv(matrix, vector): # This function obtains the multiply of matrix key and each of the vectors
                            # we got the result with their mod 26
    resultado=[]
    for aux in vector: 
        aux_resultado=[]
        for i in range (2):
            mod=0
            for j in range (2):
                mod += matrix[i][j] * aux[j]
            aux_resultado.append(mod % 26) 
        resultado.append(aux_resultado)
    #We obtain a matrix of vectors
    return resultado

def msg(matrix): #This function convert the matrix of vector into letters
                    # and save it as a string for output
    message = ''
    for vector in matrix:
        for x in vector:
            for key,value in letters.items():
                if x==value:
                    message+=key
    
    return message

def cipher(key, plain_text): #In this function we call all the functions in order to encrypt
    matrix_key= do_matrix(key)
    aux_vector= do_vector(plain_text)
    final=mxv(matrix_key,aux_vector)
    d=msg(final)
    print(d)
    

def decipher(key, plain_text): #In this function we call all the functions in order to decrypt
    matrix_key= do_matrix(key)
    aux_det_key= det_key(matrix_key)
    adj_key = adj_matrix(matrix_key)

    aux= mod26(aux_det_key)
    aux_final= do_inv(aux,adj_key)

    aux_vector=do_vector(plain_text)
    final=mxv(aux_final,aux_vector)
    d=msg(final)
    print(d)

def start(): #This function put the inputs in list without \n
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
    

    for i in lines[2]:
        aux=i.replace('\n','')
        key.append( aux.upper() )
    #for the case that after enter the key didin´t press "enter"
    if '' in key:
        key.remove('')

    #Guarantee valid options
    if(do[0] =='C'):
        cipher(key,plain_text)
    elif (do[0] == 'D'):
        decipher(key,plain_text)
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

