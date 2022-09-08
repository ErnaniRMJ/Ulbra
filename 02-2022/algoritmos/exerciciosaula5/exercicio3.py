#FUP para ler dois valores numericos e apresentar a diferenca do maior pelo menor.

valor1 = float(input("Digite o primeiro valor:"))
valor2 = float(input("Digite o segundo valor:"))

if valor1 > valor2:
    diferenca = valor1 - valor2
    print(diferenca)
else:
    diferenca = valor2 - valor1
    print(diferenca)
    