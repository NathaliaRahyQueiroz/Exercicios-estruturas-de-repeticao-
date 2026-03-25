#Declaração das variáveis 
a: int = 0
b: int = 0
troca: int = 0
sequencia: int = 1
divisor: int = 0
#Início
a= int(input("Digite um valor:"))
b= int(input("Digite outro valor:"))
if b<a:
    troca = b
    b = a
    a = troca

while a<=b:
    sequencia = 1
    divisor = 0
    while sequencia<=a:
        if a % sequencia == 0:
            divisor +=1
        sequencia+=1
    if divisor == 2:
        print(a, "é primo nesse intervalo")
    a+=1
#Fim