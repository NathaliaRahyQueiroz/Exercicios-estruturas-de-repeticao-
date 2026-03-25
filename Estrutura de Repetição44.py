#Declaração das variáveis 
contador: int = 1
expoente: int = 0
base: int = 0
potencia: int = 1
#Início
base = int(input("Digite o valor da base da potência:"))
expoente = int(input("Digite o valor do seu expoente:"))

for contador in range(1, (expoente+1), 1):
    potencia = potencia * base
print ("O resultado da potência é igual a:", potencia)
#Fim