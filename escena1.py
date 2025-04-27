import time

import funciones_str
import funciones_repetidas


def desicion1(jugador:str)->int:
    '''Inicia la escena 1 recibe el nombre del jugador 
    y este tomara alguna 
    desicion y se devolvera el valor para 
    conectar con el resto de escenas'''
    
    time.sleep(5)

    print("Dejare que te acomodes en tu cabaña solitaria en el bosque tal como habias pedido," \
    " nos vemos luego si es que sobrevivis JAJAJAJAJ \n")

    print("Te han dejado solo toma una decision\n")
    desicion = 0
    i = 0
    
    while desicion !=1 and desicion !=2 and desicion !=13:
        desicion = int(input("1 Seguir acomodando" \
            "\n2 Recorrer el camapmento \n3 No hacer nada \n\n"))
        match desicion:
            case 1: 
                print("Mientras acomodas, repentinamente se va la luz, " \
                "habra que tomar alguna decision")
            case 2:
                    print("Salis afuera de la cabaña, en verdad era una cabaña solitaria " \
                    "en el medio del bosque. Se escuchan ruidos extraños pero tratas " \
                    "de no darle importancia hasta que sientes que hay alguien detras.")
            case 3:
                    i += 1
                    chances = 3
                    advertencia = "Que aburrido toma una buena decision"
                    te_lo_dije = f"Ser aburrido tiene consecuencias {jugador}. Jason " \
                    "por favor haz los honores"
                    consecuencia = "JASON TE ARRANCA LA CABEZA"
                    
                    funciones_repetidas.oportunidad(i,chances,advertencia,te_lo_dije,consecuencia)
                    if(i == chances):
                          return 0

            case 13:
                    print("¿Que hiciste......?")
                    time.sleep(2)
                    print("Esto no estaba planeado")
                    time.sleep(2)
                    print("Cargando...")
                    funciones_str.caracter_por_caracter(" ",1)
                    funciones_str.separar_caracteres("ALARMA")
                    funciones_str.caracter_por_caracter(" ",1)
                    funciones_str.separar_caracteres("COD")
                    funciones_str.caracter_por_caracter("331258", 1)
                    print(" ")
                    funciones_str.caracter_por_caracter("Jason esta aqui", 3)
                    print(" ")
                    funciones_str.separar_caracteres("HUYE")
                    time.sleep(2)
                    print("Si puedes\n")
            case _: 
                    i += 1
                    chances = 3
                    advertencia = "Cuidado con lo que pones"
                    te_lo_dije = "Usted no aprende ¿Verdad? *LLego Jason*"
                    consecuencia = "JASON TE CORTA A LA MITAD"
                    
                    funciones_repetidas.oportunidad(i,chances,advertencia,te_lo_dije,consecuencia)
                    if(i == chances):
                          return 0
    return desicion



