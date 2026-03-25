#Declaração das variáveis 
dado1: int = 1
dado2: int = 0
#Início 
while dado1<= 6:
    for dado2 in range(1, 7, 1):
        if dado1 + dado2 == 7:
            print ("Para dar 7 é preciso tirar", dado1, "no primeiro dado e", dado2, "no segundo dado")
    dado1+=1
#Fim