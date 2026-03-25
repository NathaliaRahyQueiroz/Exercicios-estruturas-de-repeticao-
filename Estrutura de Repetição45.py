#Declaração das variáveis 
numerador: int  = 1
divisão: float = 0.0
resultado: float = 0.0
#Início
while numerador <= 15:
    divisão = numerador/(numerador **2)
    if numerador %2 == 0:
        resultado = resultado - divisão
    else:
        resultado = resultado + divisão
    numerador +=1
print (round(resultado,2))
#Fim