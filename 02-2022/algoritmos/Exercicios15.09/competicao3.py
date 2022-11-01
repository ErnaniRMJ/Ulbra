# Faca um algoritmo que leia dois numeros inteiro ou flutuante e que pergunte qual a operacao aritmetica
# que ele usara, com essas informacoes faca o calculo e imprima na tela a operacao aritmetica.

# 1 Entre com o primeiro numero
# 2 Entre com o segunmdo numero
# 3 Entre com a operacao artitmetica desejada em string que levara para as funcoes ifs
# 4 Faca o calculo com os numeros digitados e com a operacao aritmetica escolhida
# 5 Faca o resulultado negativo
# 6 Exiba na tela o calculo que resultou.
# 7 Exiba na tela a soma negativa
# 8 Exemplo (-10)+(-20)= -30 

num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))
func = input("Digite a operacao desejada:")
soma = 'soma'
subtracao = 'subtracao'
multiplicacao = 'multiplicacao'
divisao = 'divisao'
result_negat = (-num1)+(-num2)

if func == 'soma':
    calc_soma = num1 + num2
    print(f'Resultado:{calc_soma}')
elif func == 'subtracao':
    calc_sub = num1 - num2
    print(f'Resultado:{calc_sub}')
elif func == 'multiplicacao':
    calc_mult = num1 * num2
    print(f'Resultado:{calc_mult}')
elif func == 'divisao':
    calc_div = num1/num2
    print('Resultado{}'.format(f'{calc_div:.2f}'))
print('Oresultado negativo da soma dos doisnumeros e :{}'.format(f'{result_negat:.0f}'))