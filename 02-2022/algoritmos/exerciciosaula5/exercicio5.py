#FUP para ler dois numeros. Se os numeros forem iguais, imprimir a mensagem:
#"NUMEROS IGUAIS" e encerrar a execucao; caso contrario, imprimir o de maior valor.

n1 = float(input("Digite o primeiro numero:"))
n2 = float(input("Digite o segundo numero:"))

if n1 == n2:
    print("Os numeros sao iguais.")
elif n1 > n2:
    print(n1)
else:
    print(n2)
 