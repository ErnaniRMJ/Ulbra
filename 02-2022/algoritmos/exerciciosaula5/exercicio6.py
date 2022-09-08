#FUP para ler e escrever tres numeros. Se o primeiro numero for positivo, imprimir sua raiz quadrada, caso
#contrario, imprimir o seu quadrado; se o segundo numero for maior que 10 e menor que 100, imprimir a mensagem: 
#"numero esta entre 10 e 100 - intervalo permitido"; se o terceiro numero for menor que o segundo, 
# calcular e escrever a diferenca entre eles, caso contrario, calcular e escrever a soma entre eles.

import math


n1 = float(input("didite o primeiro numero"))
n2 = float(input("didite o segundo numero"))
n3 = float(input("didite o terceiro numero"))

if n1 > 0:
    print(math.sqrt(n1))
else:
    print(n1*n1)

if n2 > 10 and n2 < 100:
    print("numero esta entre 10 e 100 - intervalo permitido")

if n3 < n2:
    diferenca = n2 - n3
    print(diferenca)
else:
    soma = n3 + n2
    print(soma)
