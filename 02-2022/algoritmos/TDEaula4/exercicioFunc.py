#Faça um programa que leia um valor inteiro (que representa o real, moeda nacional) e calcule
#qual o menor número possível de notas/moedas de 100, 50, 20, 10, 5, 2 e 1 em que o valor lido
#pode ser decomposto. Escrever o valor lido e a relação de notas necessárias.*


montanteInicial = int(input("Digite um valor"))
 

nota100 = 100
nota50 = 50
nota20 = 20
nota10 = 10
nota5 = 5
nota2 = 2
nota1 = 1

def calculoDeNotas(montante):
    contadorNotas = 0

    while montante != 0:
        if montante >= nota100:
            montante -= nota100
            contadorNotas += 1
        elif montante >= nota50:
            montante -= nota50
            contadorNotas += 1
        elif montante >= nota20:
            montante -= nota20
            contadorNotas += 1
        elif montante >= nota10:
            montante -= nota10
            contadorNotas += 1
        elif montante >= nota5:
            montante -= nota5
            contadorNotas += 1
        elif montante >= nota2:
            montante -= nota2
            contadorNotas += 1
        elif montante >= nota1:
            montante -= nota1
            contadorNotas += 1
        else:
            contadorNotas = contadorNotas

    return contadorNotas 


quantidadeNotas = calculoDeNotas(montanteInicial)
print("O valor lido e de", montanteInicial, "E a quantidade de notas e de", quantidadeNotas)