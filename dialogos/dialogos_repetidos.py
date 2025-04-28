import funciones.funciones_str
def perder(te_lo_dije:str,consecuencia:str):
    '''Recibe dos textos y los imprime junto a un mensaje de fin de juego'''
    print(te_lo_dije)
    funciones.funciones_str.separar_caracteres(consecuencia)
    funciones.funciones_str.separar_caracteres("GAME OVER")

