# Crie um programa em Python que solicite um numero do usuário, 
# depois some este numero com 1357, multiplique por 8, divida por 5 e eleve ao quadrado.

numero = int(input("Digite um Numero: "))
soma = numero + 1357
multiplicacao = soma * 8
divisao = multiplicacao / 5
quadrado = divisao ** 2
print(int(quadrado))

# ou pode substituir o print ignorar a linha 5,6,7,8,9 e colocar:
# print(int((((numero + 1357))* 8)/5)**2)