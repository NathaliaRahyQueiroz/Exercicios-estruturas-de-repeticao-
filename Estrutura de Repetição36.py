#Declaração das variáveis 
numero: int = 0
c: int = 1
fatorial: int = 1
soma: float = 1.0

#Início
numero = int(input("Digite um número:"))
while c<=numero:
    fatorial = fatorial *c
    c+=1
    soma = soma + (1/fatorial)
print (round(soma, 2))
#Fim