# Construa um algoritmo que leia um número inteiro de 1 a 7 e informe o dia da
# semana correspondente, sendo domingo o dia de número 1. Se o número não
# corresponder a um dia da semana, mostre uma mensagem de erro.

diaSemana = int(input("Digite o numero correspondente ao dia da semana !"))

domingo = 1
segunda = 2
terca = 3
quarta = 4
quinta = 5
sexta = 6
sabado = 7

if diaSemana == domingo:
    print("Domingo")
elif diaSemana == segunda:
    print("Segunda")
elif diaSemana == terca:
    print("terca")
elif diaSemana == quarta:
    print("Quarta")
elif diaSemana == quinta:
    print("sexta")
elif diaSemana == sexta:
     print("Sabado")
else:
    print("Opicao invalida !")
