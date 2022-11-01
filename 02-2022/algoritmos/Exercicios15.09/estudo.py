#-Construa um algoritmo que leia dois números e efetue a adição. Caso o valor
# somado seja maior que 20, este deverá ser apresentado somando e a ele mais
# 8; caso o valor somado seja menor ou igual a 20, este deverá ser apresentado
#subtraindo-se 5




#num1 = int(input("digite o primeiro numero "))
#num2 = int(input("digite o segundo numero "))

#soma = num1 + num2
#if soma > 20:
 #   print(soma + 8)
#elif soma <= 20:
    #print (soma - 5)


# Faça um algoritmo para entrar com código, sexo e idade de uma pessoa. Se a
# pessoa for do sexo feminino e tiver menos que 25 anos, imprimir código e
# mensagem: ACEITA. Caso contrário, imprimir código e a mensagem: NÃO
# ACEITA    


#sexo = input("qual seu sexo, (F)feminino ou (M)masculino ?")
#idade = int(input("Qual sua idade ?"))

#if sexo == "F" or "f" and idade < 25:
#    print("aceita")
#else:
#    print("nao aceita")

# Faça um algoritmo que verifique a validade de uma senha fornecida pelo
# usuário. A senha válida é o número 1234. OBS: Se a senha informada
# pelo usuário for inválida, a mensagem ACESSO NEGADO deve ser exibida.
# Se for a correta, a mensagem "ACESSO PERMITIDO" deverá ser exibida.

#senha = int(input("qual a sua senha ?"))

#if senha == 1234:
#    print("acesso permitido")
#else:
#    print("acesso negado")

# Faça um algoritmo para reajustar o salário de acordo com a função. Se for
# técnico, aumentar o salário 50%, se for gerente, aumentar 30% e se for outro
# cargo, aumentar 20%.

#funcao = int(input("qual sua funcao? 1 p/ tecnico, 2 p/gerente ou 3 p/ outra funcao !"))
#salario = float(input("Qual seu salario ?"))

#if funcao == 1:
#    salarioFinal = salario * 1.5
#    print(" seu reajuste fico em R$" , salarioFinal)
#elif funcao == 2:
#    salarioFinal = salario * 1.3
#    print("seu rejuste fico em R$ ", salarioFinal)
#elif funcao == 3:
#    salarioFinal = salario * 1.2
#    print("seu reauste ficou em R$", salarioFinal)
#else:
#    print("opcao invalida !!!")    


# Faça um programa que receba o valor da venda, escolha a condição de
# pagamento no menu e mostre o total da venda final conforme condições a
# seguir:
#1 - Venda a Vista - desconto de 10%
#2 - Venda a Prazo 30 dias - desconto de 5%
#3 - Venda a Prazo 60 dias - mesmo preço
#4 - Venda a Prazo 90 dias - acréscimo de 5%
#5 - Venda com cartão de débito - desconto de 8%
#6 - Venda com cartão de crédito - desconto de 7%


#valor = float(input("Qual o valor total da venda ? "))
#condicao = int(input("digite 1 para venda avista \ndigite 2 para venda a prazo 30 dias \ndigite 3 para venda a prazo 60 dias \ndigite 4 para venda a prazo 90 dias \ndigite 5 para venda debito \ndigite 6 para venda credito  "))

#if condicao == 1:
#    diferenca = (valor / 100) * 10 
#    avista = valor - diferenca
#    print("O valor da venda foi de R$",avista)
#elif condicao == 2:
#    diferenca = (valor / 100) * 5
#    prazo30 = valor - diferenca
#    print("O valor da venda foi de R$",prazo30)
#elif condicao == 3:
#    print(" O valor da venda foi de ",valor)
#elif condicao == 4:
#    acrecimo = (valor / 100) * 5
#    prazo90 = valor + acrecimo
#    print("o valor da venda foi de R$", prazo90)
#elif condicao == 5:
#    diferenca = (valor / 100) * 8
#    debito = valor - diferenca
#    print("O valor da venda foi de R$ ",debito)
#elif condicao == 6:
#    diferenca =(valor / 100) * 7
#    credito = valor - diferenca
#    print("O valor da venda foi de R$ ",credito)



# Construa um algoritmo que leia um número inteiro de 1 a 7 e informe o dia da
# semana correspondente, sendo domingo o dia de número 1. Se o número não
# corresponder a um dia da semana, mostre uma mensagem de erro.


