#Crie um algoritmo que leia dois valores numéricos e a partir disso faça para cada um deles 
#(primeiro e segundo números):

#(1) se o valor for par:
#Imprima na tela a frase O Número digitado é par.
	
#(2) se o valor for ímpar:
#Imprima na tela a frase O Número digitado é ímpar.

#(3) se o número for menor que 10:
#Imprima na tela a frase O Número é menor que 10.

#(4) se o número for maior que 10:
#Imprima na tela a frase O Número é maior que 10.

#(5) imprima na tela o quadrado de cada número:

#(6) imprima na tela o resto da divisão de cada número por 2:

#(7) imprima na tela a soma dos dois números;

n1 = float(input("digite o primeiro numero:"))
n2 = float(input("digite o segundo numero:"))
 
if (n1 % 2) == 0 and (n2 % 2) == 0:
    print("Os Números digitados sao pares")
elif (n1 % 2) == 1 and (n2 % 2) == 1:
    print("Os numeros digitados sao impares")
elif n1 < 10 and n2 < 10:
    print("Os numeros sao menores que 10")
elif n1 > 10 and n2 > 10:
    print("Os numeros sao maiores que 10")     

quadradoN1 = (n1 * n1)
quadradoN2 = (n2 * n2)
print("O quadrado dos numeros e", quadradoN1," - ",quadradoN2)

restoDivisaoN1 = n1 % 2 
restoDivisaoN2 = n2 % 2
print("O resto da divisao dos numeros por 2 e", restoDivisaoN1," - ",restoDivisaoN2)

print("A soma dos dois numeros e",(n1 + n2))