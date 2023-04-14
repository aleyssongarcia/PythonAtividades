"""
1 - Escreva um algoritimo para imprimir os numeros de 1 (inclusive) a 10 (inclusive) em ordem crescente.
"""

x = 1
while x < 11:
    print(x)
    x += 1

"""
2 - Faça um programa que converta metros para centimetros.
"""

metros = float(input("Informe um numero em metros: "))
centimetros = metros * 100

print(f'{centimetros} cm' )


"""
Solicite ao usuario um valor numerico, inteiro ou real, e escrever se é positivo ou negativo (considere o valor de zero como positivo)
"""

numero = float(input("Digite um valor numérico: "))

if valor >= 0:
    print("O valor é positivo")
else:
    print("O valor é negativo")