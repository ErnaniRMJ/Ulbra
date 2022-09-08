#Dados dois numeros A e B, some 100 ao maior numero e imprima.

n1 = float(input("digite o primeiro numero:"))
n2 = float(input("digite o segundo numero:"))

if(n1 > n2):
    n1 = n1 + 100
    print(n1)
else:
    n2 = n2 + 100
    print(n2)

