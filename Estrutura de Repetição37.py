#Declarar 
a: int = 1 
b: int = 0
resultado: int = 0
termo: int = 0
contador: int = 0
#Inicio
termo = int(input("Digite a quantidade de termos da sequência de Fibonacci (inteiro e positivo):"))
print (1)
a = 1
b =0
if termo >1:
    while contador< (termo -1):
        resultado = a + b
        print (resultado)
        b = a
        a = resultado
        contador +=1
#Fim