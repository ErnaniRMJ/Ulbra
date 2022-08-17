from computador import Computador

computador1 = Computador("Microsoft", "Celeron")
computador1.ligar()

print(computador1.marca)
print(computador1.modelo)

computador2 = Computador("Apple", "MacBook")
computador2.ligar()

#1. Faça um algoritmo que resolva as seguintes expressões aritméticas considerando A=2,
#B=5 e C=10. Mostre o resultado na tela da expressão

#a. A+B*C/A
#b. (A+B)*C/A
#c. (A+B*C)/A

a = 2
b = 5
c = 10

valorA = a+b*c/a
valorB = (a+b)*c/a
valorC = (a+b*c)/a

print(valorA)
print(valorB)
print(valorC)


#2Faça um algoritmo que leia dois números reais e imprima a soma e a média aritmética
#desses números.

def soma(numero1, numero2):
  print(numero1 + numero2)
  print((numero1 + numero2)/2)

n1 = float(input("digite um numero\n"))
n2 = float(input("digite o segundo numero\n"))

soma(n1, n2)


#3Faça um algoritmo que leia um número inteiro e imprima seu antecessor e seu
#sucessor.

def imprimirNumeros(numero):
  antecessor = numero - 1
  sucessor  = numero +1

  print(antecessor)
  print(sucessor)

n1f3 = int(input("digite um numero\n"))

imprimirNumeros(n1f3)


#4Faça um algoritmo para calcular a média aritmética entre três números quaisquer.

def media3Numeros(numero1, numero2, numero3):
  media = (numero1 + numero2 + numero3)/3
  print("A media dos 3 numero e",media)


n1f4 = float(input("digite o primeiro numero\n"))
n2f4 = float(input("digite o segundo numero\n"))
n3f4 = float(input("digite o terceiro numero\n"))

media3Numeros(n1f4, n2f4, n3f4)


#5Faça um algoritmo (FUA) que lê o número de um funcionário, seu número de horas
#trabalhadas e o valor que recebe por hora. O algoritmo deve calcular e mostrar o salário
#deste funcionário.)

def salarioFuncionario(codigo, horas, valorHora):
  salario = (horas*valorHora)*30
  print('Funcionario',codigo,"recebe R$",salario,"mensais.")

codigofunc = int(input("digite seu codigo\n"))
horasTra = float(input("digite suas horas trabalhadas\n"))  
valorHoras = float(input("quanto voce recebe por hora?\n"))

salarioFuncionario(codigofunc, horasTra, valorHoras)
  
#6FUA para ler dois inteiros (variáveis A e B) e efetuar as operações de adição,
#subtração, multiplicação e divisão de A por B apresentando ao final os quatro resultados
#obtidos.


def resultadoOperacoes(a, b):
  adicao = a+b
  subtracao = a-b
  multiplicacao = a*b
  divisao = a/b 

  print("A soma de 'a' + 'b' e",adicao)
  print("A subtracao de 'a' - 'b' e",subtracao)
  print("A multiplicacao de 'a' * 'b' e",multiplicacao)
  print("A divisao de a 'a' / 'b' e",divisao)

a1 = int(input("digite um numero\n"))  
b2 = int(input("digite o segundo numero\n"))


resultadoOperacoes(a1, b2)



#7FUA para calcular a área de um triângulo, exibindo o resultado. A base e a altura são
#dados que devem ser lidos como entrada.

def trianguloArea(altura, base):
  area = base*altura/2
  print("O resultado da area do triangulo e ",area)

altura1 = float(input("Digite a altura do triangulo\n"))
base1 = float(input("digite a base do triangulo\n"))

  
trianguloArea(altura1, base1)


#8Uma loja de animais precisa de um algoritmo para calcular os custos de criação de
#coelhos. O custo é calculado com a fórmula CUSTO=(NRO_COELHOS*0.70)/18+10. O
#algoritmo tem como entrada o número de coelhos, devendo fornecer, como saída, o custo.

def numeroDeCoelhos(coelhos):
  custo =(coelhos*0.70)/18+10
  print("O custo dos coelhos e ",custo)

nroCoelhos = int(input("digite o numero de coelhos\n"))

numeroDeCoelhos(nroCoelhos)  


#9F.U.A para calcular o valor de lucro que um vendedor tem em um produto, com base
#em seu preço de custo e o preço de venda.


def valorDeLucro(precoDeCusto,precoDeVenda):
  lucro = precoDeVenda - precoDeCusto
  print("O lucro sera de ",lucro)

custo = float(input("digite o preco de custo\n"))
venda = float(input("digite preco de venda\n"))

valorDeLucro(custo, venda)  


#10F.U.A que leia o preço de um produto e a quantidade comprada e exiba para o usuário
#o preço que ele tem que pagar pela compra.


def valorDeCompra(quantidade,precoProduto):
  preco = quantidade * precoProduto
  print("O valor que o usuario tera que pagar e",preco)

quantidade1 = int(input("digite a quantidade de produtos\n"))  
precoProd = float(input("digite o valor do produto\n"))

valorDeCompra(quantidade1, precoProd)


#11F.U.A que leia dois números e calcule qual é o resto da divisão do 1o pelo 2o número.
#Exiba na tela este valor final.

def restoDaDivisao(numero1, numero2):
  resto = numero1 % numero2
  print("O resto da divisao e",resto)

numeroA = float(input("digite o primeiro numero\n"))
numeroB = float(input("digite o segundo numero\n"))


restoDaDivisao(numeroA, numeroB)



#12F.U.A que leia dois números e calcule qual é o valor inteiro da divisão do 2o pelo 1o
#número. Exiba na tela este valor final.

def valorInteiro(primeiroNumero,segundoNumero):
  valorFinal = segundoNumero // primeiroNumero
  print("O valor inteiro da divisao sera",valorFinal)

nro1 = int(input("digite o primeiro numero\n"))
nro2 = int(input("digite o segundo numero\n"))


valorInteiro(nro1, nro2)

