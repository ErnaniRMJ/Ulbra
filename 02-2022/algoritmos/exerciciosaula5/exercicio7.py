# FUP para ler dois valores: NUM1 e NUM2, e se NUM1  for maior que NUM2 executaa soma de NUM1 e NUM2;
# caso contrario, executa uma subtracao.

num1 = float(input("Digite o primeiro numero."))
num2 = float(input("Digite o segundo numero."))

if num1 > num2:
    print(num1+num2)
else:
    print(num2-num1)
        
