import time

import dialogos_repetidos
import funciones_repetidas

def desicion2(desicion_anterior:int , jugador:str)->int:
    '''Recibe el numero de la desicion de la escena anterior'''
    match desicion_anterior:
        case 1:
            nueva_desicion = 0
            chances = 3
            while(nueva_desicion !=1 and nueva_desicion !=2 and nueva_desicion !=3 ):
                nueva_desicion = int("1 Quedarse en la oscuridad y esperar \n" \
                                 "2 Buscar algo para hacer luz \n" \
                                 "3 Salir a explorar \n")
                match nueva_desicion:
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case _:
                        i += 1
                        advertencia = "Cuidado con lo que pones"
                        te_lo_dije = f"Fuiate advertido {jugador}"
                        consecuencia = "JASON TE VUELA LA CABEZA DE UNA PIÑA"
                        funciones_repetidas.oportunidad(i,chances,advertencia,te_lo_dije,consecuencia)
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
                "2 Huir \n\n"))
                match nueva_desicion:
                    case 1:
                        print("¿Estas loco?, como vas a enfrentarte " \
                        "al mismisimo Jason sin siquiera un arma")
                        dialogos_repetidos.perder("Una patada " \
                        "en la cara no es suficiente")
                        return 0
                    case 2:
                        print("Huyes al bosque y por conveniencia de la trama" \
                        "casualmente haz encontrado una motocierra")
                    case _:
                        i += 1
                        advertencia = "No hay tiempo para esto," \
                        " toma una buena decision"
                        te_lo_dije = f"Te lo adverti {jugador}"
                        consecuencia = "JASON WINS FLAWESS VICTORY FATALITY"
                        funciones_repetidas.oportunidad(i,chances,advertencia,te_lo_dije,consecuencia)
                        if(i==chances):
                            return 0
        case _:
            return 0
    return nueva_desicion
        