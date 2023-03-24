# crie um prohgrama que receba o nome,
# a idade de um aluno e suas 3 notas e que calcule a media.
# se a media for acima de 7.0, apresente na tela
#" parabens", você passou por media!
#se ele não atingiu a media, apresente,
# " é deu ruim, tenta novamente"

nome = input("Qual seu nome? ")
idade = int(input("qual sua idade? "))

numeros = [float(input("digite a sua nota: ")) for x in range(3)]

media = sum(numeros) / 3

if media >= 7:
    print(f'Parabens {nome}, você passsou com media {media}')
else:
    print(f"poxa {nome}, deu ruim, tente novamente")