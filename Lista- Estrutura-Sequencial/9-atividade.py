"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um 
algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
1. Para homens: (72.7*h) - 58
2. Para mulheres: (62.1*h) - 44.7
"""

altura = float(input('Digite sua altura: '))

print(f'Se você for homem seu peso ideal é {(72.7*altura)-58:.2f} \n'
      f'Se você for mulher seu pedo ideal é {(62.1*altura)-44.7:.2f}')
