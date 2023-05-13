#neste código o usuário seleciona qual lotérica quer jogar o programa gera 3 lista com números aleatórios com a quantidade existente 
#em cada loterica.

#PROGRAMA FEITO USANDO A FUNÇÃO IF E ELSE

import random
import time

#função de controle de tempo
def tempo():
    print("carregando....")
    time.sleep (6)
def tempo_sec():
    print("Lista sendo gerada..")
    time.sleep(4)

#função de linhas (estilo)
def linhas():
    print("--"*10)




#__________ CODIGO PRINCIPAL --------------

#seleção para o usuário.
lot = int(input("Escolha uma lotérica \n 1- Lotofacil \n 2-Lotomania \n 3-Megasena"))

# ---------------------------------------
linhas()
if lot == 1: #lotofacil
    print(" Opção 1 -Lotofacil selecionado")

#Função tempo de espera  da lista
tempo()
tempo_sec()

F1= random.sample(range(0,60),6)
F2 = random.sample(range(0,60),8)
F3 = random.sample(range(0,60),15)
print(f"Listas geradas com sucesso!\nLista com 6:{F1} \n Lista com 8:{F2} \n Lista com 15:{F3}")

#----------------------------------------------
linhas()
if lot == 2:#lotomania
    print("Lotomania")

tempo()


L1= random.sample(range(0,60),6)
L2 = random.sample(range(0 ,60),8)
L3 = random.sample(range(0,60),15)

print(f"Lista gerada : \n Lista com 6:{L1} \n Lista com 8:{L2} \n Lista com 15:{L3}")

#---------------------------------------
linhas()
if lot == 3:#megasena
    print("megasena")

tempo()


M1= random.sample(range(0,60),6)
M2 = random.sample(range(0, 60),8)
M3 = random.sample(range(0,60),15)

print(f"Lista com 6:{M1} \n Lista com 8:{M2} \n Lista com 15:{M3}")


  else:
        print("Nenhuma")
