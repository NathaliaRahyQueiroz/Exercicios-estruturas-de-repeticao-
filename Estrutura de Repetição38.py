#Declararação das variáveis 
numero: float = 0.0
maior: float = 0.0
menor: float = 0.0
contador: int = 0 
#Início 
numero = float(input("Digite um valor (positivo):"))
if numero >=0:
    maior = numero
    menor = numero
    while contador < 4:
        numero = float(input("Digite um valor (positivo):"))
        while numero <0:
            numero = float(input("Digite um valor (apenas positivo):"))
        if numero >= 0:
            if numero > maior:
                maior = numero 
            if numero < menor:
                menor = numero 
        contador += 1
    print ("Maior valor:", maior, "Menor valor:", menor)
#Fim