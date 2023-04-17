"""
As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se
forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs
compradas, calcule e escreva o custo total da compra.
"""

quantidade_maca = int(input('Quantas maçãs deseja comprar: '))
if quantidade_maca >= 12:
    print(f'{quantidade_maca} maçãs custam R${quantidade_maca * 1.00:.2f}')
else:
    print(f'{quantidade_maca} maçãs custam R${quantidade_maca * 1.30:.2f}')