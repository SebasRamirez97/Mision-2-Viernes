import time

import dialogos.dialogos_repetidos
import funciones.funciones_repetidas

def desicion2(desicion_anterior:int , jugador:str)->int:
    '''Recibe el numero de la desicion de la escena anterior'''
    match desicion_anterior:
        case 1:
            i = 0
            j = 0
            nueva_desicion = 0
            chances = 3
            while(nueva_desicion !=2 and nueva_desicion !=3 ):
                nueva_desicion = int(input("1 Quedarse en la oscuridad y esperar. \n" \
                                 "2 Buscar algo para hacer luz. \n" \
                                 "3 Salir a explorar. \n"))
                match nueva_desicion:
                    case 1:
                        j += 1
                        sugerencia = f"{jugador} creo que has esperado un buen tiempo no hay señales de que vuelva la luz, "\
                        "toma otra decision.\n"
                        if j >= 2:
                            sugerencia = f"Cuidado {jugador} puede ser peligroso quedarse tanto tiempo en la oscuridad, "\
                            "busca otra manera.\n"
                        es_tarde = "Has esperado demasiado, ya es tarde, no hay escapatoria."
                        consecuencia = f"NADIE SUPO MAS NADA DE {jugador.upper()}"
                        funciones.funciones_repetidas.oportunidad(j,chances,sugerencia,es_tarde,consecuencia)
                        if(j==chances):
                            return 0
                    case 2:
                        pass
                    case 3:
                        pass
                    case _:
                        i += 1
                        advertencia = "Esa no es una opcion, no hay tiempo"
                        te_lo_dije = f"Te dije que no habia tiempo, Jason esta detras de ti"
                        consecuencia = "JASON TE VUELA LA CABEZA DE UNA PIÑA"
                        funciones.funciones_repetidas.oportunidad(i,chances,advertencia,te_lo_dije,consecuencia)
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
                        situacion = "¿Estas loco?, ¿como vas a enfrentarte " \
                        "al mismisimo Jason cuerpo a cuerpo?\n" \
                        "*Intentas darle una patada en la cara*" 
                        final = "TE TROPIEZAS Y QUIEBRAS EL CUELLO MUERTE"
                        dialogos.dialogos_repetidos.perder(situacion,final)
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
                        funciones.funciones_repetidas.oportunidad(i,chances,advertencia,te_lo_dije,consecuencia)
                        if(i==chances):
                            return 0
        case _:
            return 0
    return nueva_desicion
        