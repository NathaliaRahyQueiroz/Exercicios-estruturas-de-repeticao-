#Declaração das variáveis 
c: int = 0
n: int = 0
tabuada: int = 0
#Início
n= int(input("Digite um valor para gerar sua tabuada:"))
while c<10:
    c += 1
    tabuada = n * c
    print(tabuada)
#Fim