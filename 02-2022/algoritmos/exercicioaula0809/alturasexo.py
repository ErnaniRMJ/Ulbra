#FUP que le a altura e o sexo de uma pessoa, calcule seu peso ideal, utilizando as seguintes formulas:

from re import M


altura = float(input("Qual a sua altura ?"))
sexo = str(input("Qual seu sexo M para masculino e F para feminino ?"))


if sexo == M :
    ideal = (72.7 * altura)-58
    print(ideal)
else:
    ideal = (62.1 * altura)-44.7
    print(ideal) 



#  escrever um programa que le o numero de um funcionario, o numero de horas trabalhadas,o valor que recebe por hora,
# o numero de filhos com idade inferiro a 14 anos, a idade, o tempo de servico do funcionario e um valor fixo de salario
# por filho. Calcular o salario bruto, o descunto do INSS(8,5% do salario bruto) e o salario familia total. 
# Calcular o IR (imposto de renda) como segue:

#      Se SB > 1.500,00 IR = 15% do SB
#      se SB > 500 e <= 1.500,00 entao IR = 8% do SB
#      Se SB <= 500,00 entao IR = 0
#  Escrever o numero do funcionario, salario bruto, total dos descontos, e salario liquido.


numero = int(input("qual seu numero ? "))
horasTrabalhadas = float(input("Horas trabalhadas ?"))
valorHora = float(input("Quanto recebe por hora ? "))
numeroFilhos = int(input("numero de filhos menores de 14 anos ?"))
idadeFunc = int(input("qual sua idade ?"))
tempoServico = float(input("tempo de trabalho ?"))
ValorSf = float(int("valor salari familia ?"))

salarioBruto = horasTrabalhadas * valorHora
inss = (8.5)
salarioLiq = salarioBruto / 100 * 8.5
salarioFamilia = 