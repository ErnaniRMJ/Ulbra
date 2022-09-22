# Faça um algoritmo para reajustar o salário de acordo com a função. Se for
# técnico, aumentar o salário 50%, se for gerente, aumentar 30% e se for outro
# cargo, aumentar 20%.

funcao = int(input("Digite 1 para tecnico, digite 2 para gerente ou digite 3 para outra funcao."))
salario = float(input("Qual seu salario ?"))

if funcao == 1:
    salarioFinal = salario * 1.5
    # salarioFinalregra3 = salario + (salario / 100) * 50
    print("seu reajuste ficou em R$",salarioFinal)
elif funcao == 2:
    salarioFinal = salario * 1.3
    print("seu reajuste ficou em R$",salarioFinal)
elif funcao == 3:
    salarioFinal = salario * 1.2
    print("seu reajuste ficou em R$",salarioFinal)
else:
    print("opcao invalida !")
