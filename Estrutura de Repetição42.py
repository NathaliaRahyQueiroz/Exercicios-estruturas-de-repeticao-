#Início
numerador: int = 1
denominador: int = 1
divisao: float = 0.0
soma: float = 0.0
#Início
while numerador <= 50 and denominador <=99:
    divisao = numerador / denominador
    soma = soma + divisao
    numerador +=1
    denominador +=2
print (round(soma, 2 ))
#Fim