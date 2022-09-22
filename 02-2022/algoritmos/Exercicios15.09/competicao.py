# FUA que leia o numero de uma conta,e a sua senha. Que mostre o saldo da conta
# se esta positiva ou negativa, e que receba um valor de saque e mostre qual o minimo de notas
# necessarias para o saque desejado.

conta = int(input("Qual o numero da conta ?"))
senha = int(input("Qual a sua senha ?"))

saldo = 50

if (saldo > 0):
    print("Seu saldo e positivo, R$ ", saldo)
elif (saldo < 0):
    print("Seu saldo e negativo, R$ ", saldo)
else:
    print("seu saldo e de 0,00 ")

saque = float(input("Qual o valor de saque ? "))
saldoaAtual = saldo - saque

print("Seu saldo agora e de R$ " , saldoaAtual)



