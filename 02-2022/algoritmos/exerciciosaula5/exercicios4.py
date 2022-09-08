#FUP que leia um numero e mostre uma menssagem indicando se este numero e par ou impar e se e positivo ou negativo.

numero = float(input("Digite um numero:"))

if (numero % 2) == 0:
   print("par")
else:
    print("impar")

if numero >= 0:
    print("positivo")
else:
    print("negativo")

