#Declaração das variáveis 
c: int = 1
n: int = 0 
fatorial: int = 1
#Início
n = int(input("Digite um valor:"))
while c<=n:
    fatorial = fatorial*c
    c+=1
print(fatorial)
#Fim