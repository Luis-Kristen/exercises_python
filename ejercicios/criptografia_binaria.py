# -*- coding: utf-8 -*-

cifrada = []

def cifrar(palabra, *self):
    tabla=[]
    for i in range(0, len(palabra)):
        letra = palabra[i]
        letraBi=str(ord(letra))
        tabla.append(letraBi)

    print("Su codigo es: ")
    print(tabla)
    return tabla
    
def decifrar(numero):
    tabla = []
    mensajeOculto = ""
    tabla = numero.split(",")
    for i in range(0, len(tabla)):
        letra = int(tabla[i])
        letraBi=chr(letra)
        mensajeOculto += letraBi
    print("su mensaje es: ")
    print(mensajeOculto)

def run():
    
    while True:
    
        command = str(input('''
            ¿Que deseas hacer?

            [d]ecifrar
            [c]ifrar
            [s]alir
        '''))
    
        if command == 'c':
            mensaje = str(input("Escribe tu mensaje: "))

            cifrada = cifrar(mensaje)
        elif command == 'd':

            if len(cifrada)==0:
                palabra3 = str(input("Escribe tus numeros separados por comas,: "))
                decifrar(palabra3)
            else:
                command2 =  str(input(
                    '''
                    ¿Deseas decifrar el codigo anterior?

                    [s]i
                    [n]o
                    
                    '''
                ))

                if command2=='s':
                    codigo=""
                    for i in range(0, len(cifrada)):
                        if i==len(cifrada)-1:
                            codigo+=cifrada[i]
                        else:
                            codigo+=cifrada[i]+","

                    decifrar(codigo)

                else:
                    palabra3 = str(input("Escribe tus numeros separados por comas,: "))
                    decifrar(palabra3)
        else:
            exit()


if __name__ == "__main__":
    print("*** CRIPTOGRAFIA CON BINARIOS  ***")
    print("")
    run()