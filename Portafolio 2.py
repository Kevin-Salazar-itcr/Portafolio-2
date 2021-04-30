#Ejercicios para portafolio
#Identificadores debajo del código
#=========  no sirve
"========="  "sirve"

print("""invertirLista(lista)
extremosLista(lista)
nivelesLista(lista)
eliminarDigito(num, dig)
obtenerIndicesListaVectores(v1, v2, v3)
""")

"""
invertirLista
E: una lista
S: la lista invertida (si esta vacìa, devolver 0)
R: Debe ser una lista
"""
def invertirLista(lista):
    if(isinstance(lista, list)):
        if lista==[]:
            return 0
        else:
            return invertirAux(lista, [])
    else:
        return "Error: el objeto debe ser una lista"
def invertirAux(lista, res):
    if lista==[]:
        return res
    else:
        return invertirAux(lista[:-1], res+[lista[-1]])
"==============================================================="
"""
extremosLista
E: una lista
S: Una lista que contenga al número menor y mayor de la lista (si esta vacia, devolver error)
R: El objeto debe ser una lista
"""
def mayorLista(lista):
    if lista==[]:
        return "Error"
    else:
        return mayorListaAux(lista[1:], lista[0])
def mayorListaAux(lista, res):
    if lista==[]:
        return res
    if lista[0]>res:
        return mayorListaAux(lista[1:], lista[0])
    else:
        return mayorListaAux(lista[1:], res)
def menorLista(lista):
    if lista==[]:
        return "Error"
    else:
        return menorListaAux(lista[1:], lista[0])
def menorListaAux(lista, res):
    if lista==[]:
        return res
    if lista[0]<res:
        return menorListaAux(lista[1:], lista[0])
    else:
        return menorListaAux(lista[1:], res)
###########################################
def extremosLista(lista):
    if(isinstance(lista, list)):
        if lista==[]:
            return "Error: lista vacía"
        else:
            return [menorLista(lista), mayorLista(lista)]
    else:
        return "Error: El objeto no es una lista"
"==============================================================="
"""
eliminarDigito
E: un número y un dígito
S: El mismo numero, pero sin el digito indicado
R: El número no puede ser 0
    El numero debe ser entero positivo
"""
def largo(num):
    if num>=0:
        if num<=9:
            return 1
        else:
            return 1+largo(num)
    else:
        return "Error"
def eliminarDigito(num, dig):
    if(isinstance(num, int)) and (num>=0) and (isinstance(dig, int)):
        if(dig>=0 and dig<=9):
            if num==0:
                return "Error: el número no puede ser cero"
            else:
                return eliminarAux(num, dig, 0, 0)
        else:
            return "Error: 'dig' debe ser un número entre 0 y 9"
    else:
        return "Error: digite números enteros positivos"
def eliminarAux(num, dig, res, potencia):
    if num==0:
        return res
    if num%10==dig:
        return eliminarAux(num//10, dig, res, potencia)
    else:
        res+=(num%10)*(10**potencia)
        return eliminarAux(num//10, dig, res, potencia+1)
"==============================================================="
"""
nivelesLista
E: una lista con sublistas
S: la cantidad de sublistas contenidas por objeto
Ejemplo:
>>>nivelesLista([ [[[[]]]], 2, [] ])
[4, 0, 1]
"""
def nivelesLista(lista):
    if(isinstance(lista, list)):
        if lista==[]:
            return "Error: la lista no debe estar vacía"
        else:
            return nivelesAux(lista, [], 0)
    else:
        return "Error: El objeto no es una lista"
def nivelesAux(lista, res, cont):
    if lista==[]:
        return res
    else:
        prueba=str(lista[0])
        objeto=prueba
        return revision(lista, objeto, res, cont)
def revision(lista, objeto, res, cont):
    if objeto=="":
        res+=[cont]  
        return nivelesAux(lista[1:], res, cont*0)
    else:
        if objeto[0]=="[":
            return revision(lista, objeto[1:], res, cont+1)
        else:
            return revision(lista, objeto[1:], res, cont)
"==============================================================="
"""
obtenerIndicesListaVectores
E: 3 vectores
S: una lista con los indices de cada vector cuyo valor sean cero o negativo
R: Al ser vectores, los elementos contenidos deben ser del mismo tipo
    (en este caso, 'int')
    Las 3 listas deben tener el mismo largo
"""
def esVector(lista):
    if(isinstance, lista, list):
        return vectorAux(lista)
    else:
        return "El objeto no es una lista"
def vectorAux(lista):
    if lista==[]:
        return True
    if(isinstance(lista[0], int)):
        return vectorAux(lista[1:])
    else:
        return False
def largoLista(lista):
    if lista==[]:
        return 0
    else:
        return 1+largoLista(lista[1:])
    
def obtenerIndicesListaVectores(v1, v2, v3):
    if(esVector(v1)==True):
        if(esVector(v2)==True):
            if(esVector(v3)==True):
                return verifLargo(v1, v2, v3)
            else:
                return "Error: Uno o más elementos de v3 no son números enteros"
        else:
            return "Error: Uno o más elementos de v2 no son números enteros"
    else:
        return "Error: Uno o más elementos de v1 no son números enteros"
    
def verifLargo(v1, v2, v3):
    if(largoLista(v1)==largoLista(v2)==largoLista(v3)):
        return indices(v1, v2, v3, [], [], [], [],0)
    else:
        return "Error: Las listas deben tener el mismo largo"
    
def indices(v1, v2, v3, res, i1, i2, i3, indice):
    if v1==[]: #Las 3 listas son igual de largas
        return print(res+[i1]+[i2]+[i3])
    else:
        "Aquí usé validaciones en orden 'secuencial booleano'..."
        if(v1[0]>0) and (v2[0]>0) and (v3[0]>0):   #0 and 0 and 0
            return indices(v1[1:], v2[1:], v3[1:], res, i1, i2, i3, indice+1)
        if(v1[0]>0) and (v2[0]>0) and (v3[0]<=0):  #0 and 0 and 1
            return indices(v1[1:], v2[1:], v3[1:], res, i1, i2, i3+[indice], indice+1)
        if(v1[0]>0) and (v2[0]<=0) and (v3[0]>0):  #0 and 1 and 0
            return indices(v1[1:], v2[1:], v3[1:], res, i1, i2+[indice], i3, indice+1)
        if(v1[0]>0) and (v2[0]<=0) and (v3[0]<=0): #0 and 1 and 1
            return indices(v1[1:], v2[1:], v3[1:], res, i1, i2+[indice], i3+[indice], indice+1)
        if(v1[0]<=0) and (v2[0]>0) and (v3[0]>0):   #1 and 0 and 0
            return indices(v1[1:], v2[1:], v3[1:], res, i1+[indice], i2, i3, indice+1)
        if(v1[0]<=0) and (v2[0]>0) and (v3[0]<=0):   #1 and 0 and 1
            return indices(v1[1:], v2[1:], v3[1:], res, i1+[indice], i2, i3+[indice], indice+1)
        if(v1[0]<=0) and (v2[0]<=0) and (v3[0]>0):  #1 and 1 and 0
            return indices(v1[1:], v2[1:], v3[1:], res, i1+[indice], i2+[indice], i3, indice+1)
        else:   #1 and 1 and 1
            return indices(v1[1:], v2[1:], v3[1:], res, i1+[indice], i2+[indice], i3+[indice], indice+1)
"==============================================================="
