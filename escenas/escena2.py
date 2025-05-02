import time

import dialogos.dialogos_repetidos
import funciones.funciones_repetidas
from funciones.funciones_str import saltito

def desicion2(desicion_anterior:int , jugador:str)->int:
    '''Recibe el numero de la desicion de la escena anterior y 
    devuelve 0 en los casos de muerte o el numero de la nueva desicion multiplicado con la anterioor'''
    match desicion_anterior:
        case 1:
            i = 0
            j = 0
            k = 0
            nueva_desicion = 0
            chances = 3
            while(nueva_desicion !=2):
                nueva_desicion = int(input("1 Quedarse en la oscuridad y esperar. \n" \
                                 "2 Buscar algo para hacer luz. \n" \
                                 "3 Salir a explorar."))
                saltito()
                match nueva_desicion:
                    case 1:
                        j += 1
                        sugerencia = f"{jugador} creo que has esperado un buen tiempo no hay señales de que vuelva la luz, "\
                        "toma otra decision."
                        saltito()
                        if j >= 2:
                            sugerencia = f"Cuidado {jugador} puede ser peligroso quedarse tanto tiempo en la oscuridad, "\
                            "busca otra manera."
                            saltito()
                        es_tarde = "Has esperado demasiado, ya es tarde, no hay escapatoria."
                        consecuencia = f"NADIE SUPO MAS NADA DE {jugador.upper()}"
                        funciones.funciones_repetidas.oportunidad(j,chances,sugerencia,es_tarde,consecuencia)
                        saltito()
                        if(j==chances):
                            return 0
                    case 2:
                        print("Has encontrado una linterna, es seguro salir a explorar")
                        return desicion_anterior*nueva_desicion
                    case 3:
                        k += 1
                        if k == 1:
                            print(f"{jugador} recorda que no hay luz no creo que sea buena idea salir a oscuras.")
                            saltito()
                        else:
                            print("Parece que hay alguien valiente aqui, pero cuidado " \
                            "es sencillo confundir valentia con estupidez.")
                            saltito()
                            return desicion_anterior*nueva_desicion                       
                    case _:
                        i += 1
                        advertencia = "Esa no es una opcion, no hay tiempo"
                        te_lo_dije = f"Te dije que no habia tiempo, Jason esta detras de ti"
                        consecuencia = "JASON TE VUELA LA CABEZA DE UNA PIÑA"
                        funciones.funciones_repetidas.oportunidad(i,chances,advertencia,te_lo_dije,consecuencia)
                        saltito()
                        if(i == chances):
                            return 0
            
        case 2:
            nueva_desicion = int(input())
        case 13:
            i = 0
            chances = 3
            nueva_desicion = 0
            time.sleep(1)
            while nueva_desicion != 1 and nueva_desicion != 2: 
                nueva_desicion = int(input("Hay poco tiempo decide: \n" \
                "1 Enfrentarlo \n" \
                "2 Huir"))
                saltito()
                match nueva_desicion:
                    case 1:
                        situacion = "¿Estas loco?, ¿como vas a enfrentarte " \
                        "al mismisimo Jason cuerpo a cuerpo?" \
                        "*Intentas darle una patada en la cara*" 
                        final = "TE TROPEZAS Y TE QUEBRAS EL CUELLO MUERTE"
                        dialogos.dialogos_repetidos.perder(situacion,final)
                        saltito()
                        return 0
                    case 2:
                        print("Huyes al bosque y por conveniencia de la trama" \
                        "casualmente haz encontrado una motocierra")
                        saltito()
                        return desicion_anterior*nueva_desicion
                    case _:
                        i += 1
                        advertencia = "No hay tiempo para esto," \
                        " toma una buena decision"
                        te_lo_dije = f"Te lo adverti {jugador}"
                        consecuencia = "JASON WINS FLAWESS VICTORY FATALITY"
                        funciones.funciones_repetidas.oportunidad(i,chances,advertencia,te_lo_dije,consecuencia)
                        saltito()
                        if(i==chances):
                            return 0
        case _:
            return 0

        