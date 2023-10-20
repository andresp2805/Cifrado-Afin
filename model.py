from unidecode import unidecode

def inverso_multiplicativo(a, m):
    g, x, y = euclides_extendido(a, m)
    if g != 1:
        raise ValueError("El inverso multiplicativo no existe")
    else:
        return x % m

def euclides_extendido(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = euclides_extendido(b % a, a)
        return (g, y - (b // a) * x, x)
    
def cifrar_afin(a, b, palabra):
    dic = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 
           'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    lista = []
    word = unidecode(palabra)
    word1 = word.lower()
    for i in word1:
        if i == ' ':
            lista.append(None)
        else:       
            for j in dic:
                if i == j:
                    lista.append(dic[i])
    lista2 = []
    for k in lista:
        if k == None:
            lista2.append(None)
        else:
            mod = (a*k + b)%26
            lista2.append(mod)
    lista3 = []
    for i in lista2:
        if i == None:
            lista3.append(' ')
        else:         
            for j in dic:
                if i == dic[j]:
                    lista3.append(j)   
    resultado = ''.join(lista3)
    return resultado

def decifrado(a,b, palabra):
    dic = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 
           'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    inverso_a = inverso_multiplicativo(a, 26)
    lista = []
    word = palabra.lower()
    for i in word:
        if i == ' ':
            lista.append(None)
        else:       
            for j in dic:
                if i == j:
                    lista.append(dic[i])
    lista2 = []
    for k in lista:
        if k == None:
            lista2.append(None)
        else:
            mod = (inverso_a*(k - b))%26
            lista2.append(mod)
    lista3 = []
    for i in lista2:
        if i == None:
            lista3.append(' ')
        else:         
            for j in dic:
                if i == dic[j]:
                    lista3.append(j)   
    resultado = ''.join(lista3)
    return resultado

