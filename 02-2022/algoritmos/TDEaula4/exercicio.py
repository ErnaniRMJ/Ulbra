#Faça um programa que leia um valor inteiro (que representa o real, moeda nacional) e calcule
#qual o menor número possível de notas/moedas de 100, 50, 20, 10, 5, 2 e 1 em que o valor lido
#pode ser decomposto. Escrever o valor lido e a relação de notas necessárias.*


montanteInicial = int(input("Digite um valor"))

montanteDecrementado = montanteInicial 

nota100 = 100
nota50 = 50
nota20 = 20
nota10 = 10
nota5 = 5
nota2 = 2
nota1 = 1

contadorNotas = 0

while montanteDecrementado != 0:
    if montanteDecrementado >= nota100:
        montanteDecrementado -= nota100
        contadorNotas += 1
    elif montanteDecrementado >= nota50:
        montanteDecrementado -= nota50
        contadorNotas += 1
    elif montanteDecrementado >= nota20:
        montanteDecrementado -= nota20
        contadorNotas += 1
    elif montanteDecrementado >= nota10:
        montanteDecrementado -= nota10
        contadorNotas += 1
    elif montanteDecrementado >= nota5:
        montanteDecrementado -= nota5
        contadorNotas += 1
    elif montanteDecrementado >= nota2:
        montanteDecrementado -= nota2
        contadorNotas += 1
    elif montanteDecrementado >= nota1:
        montanteDecrementado -= nota1
        contadorNotas += 1
    else:
        contadorNotas = contadorNotas
        
print("O valor lido e de", montanteInicial, "E a quantidade de notas e de", contadorNotas)

