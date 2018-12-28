import sys

#Importando bibliotecas.
#Biblioteca sys permite nós utilizarmos coisas do sistema operacional.

argumentos = sys.argv #arg1 é o método, arg2 é n1, arg3 é n2

def soma(n1, n2):
    result = float(n1) + float(n2)
    return result

def sub(n1, n2):
    result = float(n1) - float(n2)
    return result

if argumentos[1] == 'soma':
    resp = soma(argumentos[2], argumentos[3])
    print(resp)
elif argumentos[1] == 'sub':
    resp = sub(argumentos[2], argumentos[3])
    print( resp)