#Solicite ao usuario um valor numerico, inteiro ou real, e escrever se é positivo ou negativo (considere o valor de zero como positivo)


valor = float(input("Digite um valor numérico: "))

if valor >= 0:
    print("O valor é positivo")
else:
    print("O valor é negativo")