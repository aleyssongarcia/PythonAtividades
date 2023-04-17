"""
Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após,
calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também
testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo',
senão escrever a mensagem 'Saldo Negativo'.
"""

conta = int(input("Digite o número da conta do cliente: "))
saldo = float(input("Digite o saldo atual: "))
debito = float(input("Digite o valor do débito: "))
credito = float(input("Digite o valor do crédito: "))

saldo_atual = saldo - debito + credito

print("O saldo atual da conta é:", saldo_atual)

if saldo_atual >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")