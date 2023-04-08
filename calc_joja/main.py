from math import trunc



def calc_semente(valor_semente, area):
    return(valor_semente*area)

def plantacao_pronta(data, dias):
    return(data+(dias))

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

text = ("""
==========================
==== CALCULADORA JoJa ====
==========================

=====PROSPERE CONOSCO=====

""")


print("""
============================
== Qual tipo de aspersor? ==
============================
1-Base
2-Qualidade
3-Irídio
============================

""")
aspersor = int(input("->"))
quant_aspersor = int(input("Quantidade de aspersores: "))

if aspersor == 1:
    area = quant_aspersor*4
elif aspersor == 2:
    area = quant_aspersor*8
elif aspersor == 3:
    area = quant_aspersor*24
else:
    print("AÍ VOCÊ ME QUEBRA")

    print("""
    =============================
    ====== Qual a semente? ======
    =============================
    1-Broto de Arroz(40)
    2-Bulbo de Tulipa(20)
    3-Sementes de alho(40)
    4-Sementes de batata(50)
    5-Sementes de chirívia(20)
    6-Sementes de couve(70)
    7-Sementes de Couve-flor(80)
    8-Sementes de Jasmim-azul(30)
    9-Sementes de morango(100)
    10-Sementes de ruibarbo(100)
    ==============================
    """)
    print("""
    =====================================
    =========  Qual a semente?  =========
    =====================================
    11-Sementes de carambola(400)
    12-Sementes de Girassol(200)
    13-Sementes de Melão(80)
    14-Sementes de Miçanga(50)
    15-Sementes de milho(150)
    16-Sementes de mirtilo(80)
    17-Sementes de papoula(100)
    18-Sementes de pimenta(40)
    19-Sementes de rabanete(40)
    20-Sementes de repolho vermelho(100)
    21-Sementes de tomante(50)
    22-Sementes de trigo(10)
    ======================================
    """)


    print("""
    =====================================
    =========  Qual a semente?  =========
    =====================================
    23-Sementes de abóbora(100)
    24-Sementes de alcachofra(30)
    25-Sementes de amaranto(70)
    26-Sementes de berinjela(20)
    27-Sementes de beterraba(20)
    28-Sementes de couve chinesa(50)
    29-Sementes de fada(200)
    30-Sementes de inhame(60)
    31-Sementes de oxicoco(240)
    ======================================
    """)
    print("""
    ====================================================
    =========  Tem semente no inverno não, fi  =========
    ====================================================
    """)

semente = int(input("->"))


dia_plantacao = int(input("Dia da plantação:"))

if semente ==1:
    valor = (calc_semente(40, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 8)
    dias_coleta1 = "Coleta única"

elif semente ==2:
    valor = (calc_semente(20, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 6)
    dias_coleta1 = "Coleta única"

elif semente ==3:
    valor = (calc_semente(40, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 4)
    dias_coleta1 = "Coleta única"

elif semente ==4:
    valor = (calc_semente(50, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 6)
    dias_coleta1 = "Coleta única"

elif semente ==5:
    valor = (calc_semente(20, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 4)
    dias_coleta1 = "Coleta única"

elif semente ==6:
    valor = (calc_semente(70, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 6)
    dias_coleta1 = "Coleta única"

elif semente ==7:
    valor = (calc_semente(80, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 12)
    dias_coleta1 = "Coleta única"

elif semente ==8:
    valor = (calc_semente(30, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 7)
    dias_coleta1 = "Coleta única"

elif semente ==9:
    valor = (calc_semente(40, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 8)
    dias_coleta1 = dias_coleta(plantacao_pronta1, 4)

elif semente ==10:
    valor = (calc_semente(100, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 13)
    dias_coleta1 = "Coleta única"

elif semente ==11:
    valor = (calc_semente(400, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 13)
    dias_coleta1 = "Coleta única"

elif semente ==12:
    valor = (calc_semente(200, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 8)
    dias_coleta1 = "Coleta única"

elif semente ==13:
    valor = (calc_semente(80, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 12)
    dias_coleta1 = "Coleta única"

elif semente ==14:
    valor = (calc_semente(50, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 8)
    dias_coleta1 = "Coleta única"

elif semente ==15:
    valor = (calc_semente(150, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 14)
    dias_coleta1 = dias_coleta(plantacao_pronta1, 4)

elif semente ==16:
    valor = (calc_semente(80, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 13)
    dias_coleta1 = dias_coleta(plantacao_pronta1, 4)

elif semente ==17:
    valor = (calc_semente(100, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 7)
    dias_coleta1 = "Coleta única"

elif semente ==18:
    valor = (calc_semente(40, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 7)
    dias_coleta1 = dias_coleta(plantacao_pronta1, 3)

elif semente ==19:
    valor = (calc_semente(40, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 6)
    dias_coleta1 = "Coleta única"

elif semente ==20:
    valor = (calc_semente(100, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 9)
    dias_coleta1 = "Coleta única"

elif semente ==21:
    valor = (calc_semente(50, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 11)
    dias_coleta1 = dias_coleta(plantacao_pronta1, 4)

elif semente ==22:
    valor = (calc_semente(10, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 4)
    dias_coleta1 = "Coleta única"

elif semente ==23:
    valor = (calc_semente(100, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 13)
    dias_coleta1 = "Coleta única"

elif semente ==24:
    valor = (calc_semente(30, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 8)
    dias_coleta1 = "Coleta única"

elif semente ==25:
    valor = (calc_semente(70, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 7)
    dias_coleta1 = "Coleta única"

elif semente ==26:
    valor = (calc_semente(20, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 5)
    dias_coleta1 = dias_coleta(plantacao_pronta1, 5)
    
elif semente ==27:
    valor = (calc_semente(20, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 6)
    dias_coleta1 = "Coleta única"

elif semente ==28:
    valor = (calc_semente(50, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 4)
    dias_coleta1 = "Coleta única"

elif semente ==29:
    valor = (calc_semente(200, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 12)
    dias_coleta1 = "Coleta única"

elif semente ==30:
    valor = (calc_semente(60, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 10)
    dias_coleta1 = "Coleta única"

elif semente ==31:
    valor = (calc_semente(240, area))
    plantacao_pronta1 = plantacao_pronta(dia_plantacao, 7)
    dias_coleta1 = dias_coleta(plantacao_pronta1, 5)

elif semente ==0:
    print("""
    A área que esses {} cobrem é de {} espaços.
    """.format(quant_aspersor, area))

if dias_coleta1 == "Coleta única":
    print("""
    A área que esses {} aspersores cobrem: {} espaços. 
    Com a semente que você quer, vai custar: {} ouros.
    Plantado no dia: {}
    Plantação ficará pronta no dia: {}  
    """.format(quant_aspersor, area, valor, dia_plantacao, plantacao_pronta1))
else:
    print("""
    A área que esses {} aspersores cobrem: {} espaços. 
    Com a semente que você quer, vai custar: {} ouros.
    Plantado no dia: {}
    Plantação ficará pronta nos dias: {}  
    """.format(quant_aspersor, area, valor, dia_plantacao, dias_coleta1))

input("")