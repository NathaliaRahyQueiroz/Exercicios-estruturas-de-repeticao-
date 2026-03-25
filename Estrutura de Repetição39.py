#Declaração de variáveis 
casas: int = 1
quantidade: int = 0
resultado: int  = 0
#Início 
while casas <= 64:
    if quantidade ==0:
        quantidade = 1
    else:
        quantidade = quantidade *2
    casas +=1
    resultado= resultado + quantidade
print ("A quantidade de grãos contidos é de:", resultado)
#Fim