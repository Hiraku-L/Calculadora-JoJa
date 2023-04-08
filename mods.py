from math import trunc


def calc_semente(valor_semente, area):
    return(valor_semente*area)

def plantacao_pronta(data, dias):
    return(data+(dias-1))

def dias_coleta(plantacao_pronta, producao):
    plantacao_pronta = int(plantacao_pronta)
    produção= int(producao)
    c = 0
    resultado = [plantacao_pronta]
    producao_corrigida =produção-1+c
    dias = 28-plantacao_pronta
    contador = 0
    quantas_produções = trunc(dias/producao_corrigida)
    for c in range(0, quantas_produções):
        resultado.append((resultado[contador]+producao_corrigida))
        contador= contador+1
    return(resultado)

print(dias_coleta(20,4))