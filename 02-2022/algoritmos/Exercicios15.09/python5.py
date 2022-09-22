# Faça um programa que receba o valor da venda, escolha a condição de
# pagamento no menu e mostre o total da venda final conforme condições a
# seguir:
#1 - Venda a Vista - desconto de 10%
#2 - Venda a Prazo 30 dias - desconto de 5%
#3 - Venda a Prazo 60 dias - mesmo preço
#4 - Venda a Prazo 90 dias - acréscimo de 5%
#5 - Venda com cartão de débito - desconto de 8%
#6 - Venda com cartão de crédito - desconto de 7%

valor = float(input("Qual o valor total da venda ? "))
condicao = int(input("digite 1 para venda avista \ndigite 2 para venda a prazo 30 dias \ndigite 3 para venda a prazo 60 dias \ndigite 4 para venda a prazo 90 dias \ndigite 5 para venda debito \ndigite 6 para venda credito  "))

if condicao == 1:
    diferenca = (valor / 100) * 10
    avista = valor - diferenca
    print("O valor de venda foi de", avista)
elif condicao == 2:
    diferenca = (valor / 100) * 5
    prazo30 = valor - diferenca
    print("O valor da venda foi de", prazo30)
elif condicao == 3:
    prazo60 = valor 
    print("O valor da venda foi de", prazo60)
elif condicao == 4:
    acrescimo = (valor / 100) * 5
    prazo90 = valor + acrescimo
    print("O valor da venda foi de", prazo90)
elif condicao == 5:
    diferenca = (valor / 100) * 8
    carDebito = valor - diferenca
    print ("O valor da venda foi de", carDebito)
elif condicao == 6:
    diferenca = (valor / 100) * 7
    carCredito = valor - diferenca
    print("O valor da venda foi de", carCredito)
else:
    print("Operacao invalida !")

