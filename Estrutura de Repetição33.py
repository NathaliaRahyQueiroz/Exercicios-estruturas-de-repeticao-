#Declaração das variáveis
numero: float = 0.0
resultado: float = 0.0
soma: float = 0.0
#Início
numero = int(input("Digite um valor:"))
while numero > 0:
    resultado = (1/numero)
    soma = soma + resultado
    numero-=1
print (round(soma,2))
#Fim