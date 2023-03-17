# 2 - Soma/multiplicação/divisão/modulo

def soma(x, y):
   return x + y

def modulo(x, y):
   return x % y

def multiplicacao(x, y):
   return x * y

def divisao(x, y):
   return x / y

print("Selecione a operação.")
print("1.Somar")
print("2.Modulo")
print("3.Multiplicar")
print("4.Dividir")

escolha = input("Digite sua escolha (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == '1':
   print(num1,"+",num2,"=", soma(num1,num2))

elif escolha == '2':
   print(num1,"-",num2,"=", modulo(num1,num2))

elif escolha == '3':
   print(num1,"*",num2,"=", multiplicacao(num1,num2))

elif escolha == '4':
   print(num1,"/",num2,"=", divisao(num1,num2))
else:
   print("Escolheu errado mano")
