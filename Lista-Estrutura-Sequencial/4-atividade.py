"""
Faça um Programa que pergunte quanto você ganha por hora e o 
número de horas trabalhadas no mês. Calcule e mostre o total do 
seu salário no referido mês.
"""

salario_por_hora = float(input('Digite quanto você ganha por hora: '))
horas_trabalhadas_mes = float(input('Digite quantas horas você trabalha por mês: '))

print(f'Você recebe R${salario_por_hora * horas_trabalhadas_mes:.2f} por mês.')