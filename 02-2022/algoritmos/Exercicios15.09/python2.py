# Faça um algoritmo para entrar com código, sexo e idade de uma pessoa. Se a
# pessoa for do sexo feminino e tiver menos que 25 anos, imprimir código e
# mensagem: ACEITA. Caso contrário, imprimir código e a mensagem: NÃO
# ACEITA

sexo = input("Qual o seu sexo? digite F ou M.")
idade = int(input("Qual a sua idade ?"))

if sexo == "F" or sexo == "f" and idade < 25:
    print("ACEITA !")  
else:
    print("NAO ACEITA")
