#Declaração das variáveis 
a: int = 0
b: int = 0
troca: int = 0
soma: int = 0

#Início
a= int(input("Digite um valor:"))
b= int(input("Digite outro valor:"))

if a>b:
    troca = b
    b = a
    a = troca


while a<=b:
    if a%2 ==1:
        soma = soma + a
    a+=1
print (soma)

#Fim