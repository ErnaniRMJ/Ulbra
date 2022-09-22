#-Construa um algoritmo que leia dois números e efetue a adição. Caso o valor
# somado seja maior que 20, este deverá ser apresentado somando e a ele mais
# 8; caso o valor somado seja menor ou igual a 20, este deverá ser apresentado
#subtraindo-se 5

n1 = int(input("digite o primeiro numero."))
n2 = int(input("digite o seggundo numero."))

soma = n1 + n2

if n1 + n2 > 20:
    print(soma + 8)
elif soma <= 20:
    print(soma -5)    

    
        