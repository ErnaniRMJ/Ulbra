# Faça um algoritmo que verifique a validade de uma senha fornecida pelo
# usuário. A senha válida é o número 1234. OBS: Se a senha informada
# pelo usuário for inválida, a mensagem ACESSO NEGADO deve ser exibida.
# Se for a correta, a mensagem "ACESSO PERMITIDO" deverá ser exibida.

senha = int(input("Qual sua senha ?"))

if senha == 1234:
    print("ACESSO PERMITIDO !")
else:
    print("ACESSO NEGADO !")