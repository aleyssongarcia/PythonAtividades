"""
Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em
ordem crescente.
"""

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

while valor1 == valor2:
    print("Os valores não podem ser iguais. Digite novamente.")
    valor2 = float(input("Digite o segundo valor: "))
if valor1 > valor2:
    print(valor2, valor1,sep=" / ")
else:
    print(valor1, valor2, sep=" / ")