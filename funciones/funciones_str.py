import time


def salto_puntitos(cantidad_saltos:int):
        '''Imprime lineas de "...." segun cuantas quiera'''
        j = 0
        while( j < cantidad_saltos):
            time.sleep(0.25)
            print("....")
            j +=1

def caracter_por_caracter(palabra:str,suspenso:int):
    '''Imprime caracter por
    caracter de una palabra 
    separados de tanto saltos 
    con "...." (suspenso) como quiera'''
    i = 0
    for i in range(i,len(palabra)):
        time.sleep(0.5)
        if palabra[i] == " ":
            salto_puntitos(suspenso-(suspenso-1))
            continue
        print(palabra[i])
        i += 1
        if i < len(palabra):
            salto_puntitos(suspenso)
    

def separar_caracteres(palabra:str):
    '''Separa los caracteres de una 
    palabra en espacios y la imprimie'''
    palabra_espaciada = ""
    for k in palabra:
            palabra_espaciada += k + " "
    print(palabra_espaciada)


#SECTOR DE PRUEBAS NO OLVIDAR DEJARLOS COMENTADOS 
#UNA VEZ TERMINADAS

# caracter_por_caracter("HOLAAADREA",3)
# separar_caracteres("HOLA")
