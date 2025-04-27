import time

import escena1
import escena2

jugador = input("Bienvenido al campamento Crystal Lake donde nada puede malir sal." \
" Eh.. salir mal, es lo primero que sale mal. \n¿Cual es tu nombre?\n")

time.sleep(0.5)

print(f"Que tal {jugador}, no quiero ser portador de malas noticias" \
" justo has llegado en la temporada de homicidios, la buena noticia es" \
" que si tomas las deciciones correctas puede ser que sobrevivas. \n")

valor = escena1.desicion1(jugador)
escena2.desicion2(valor,jugador)



                
                

    




