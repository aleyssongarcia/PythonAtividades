"""
Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior
deles.
"""
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

while valor1 == valor2:
    print("Os valores não podem ser iguais. Digite novamente.")
    valor2 = float(input("Digite o segundo valor: "))

if valor1 > valor2:
    print("O maior valor é:", valor1)
else:
    print("O maior valor é:", valor2)