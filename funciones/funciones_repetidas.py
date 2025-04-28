import dialogos.dialogos_repetidos

def oportunidad(actual:int,chances:int,advertencia:str,te_lo_dije:str,consecuencia:str)->int:
    '''Entra la chance por la que vas, cuantas chances y tres textos dependientes de la situacion
    saldran impresos y retorna en 0 cuando se terminen las oportunidades'''
    if actual < chances:
        print(advertencia)
    else:
        dialogos.dialogos_repetidos.perder(te_lo_dije,consecuencia)
                                             