"""
Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples
e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que
nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.
"""

# nota = [float(input("Digite sua nota: "))for x in range(2)]
# media = sum(nota) / 2

nota1 = float(input("Digite sua 1ª nota: "))
nota2 = float(input("Digite sua 2º nota: "))
media = (nota1 + nota2) / 2
if (media) >= 6:
    print(f'Você foi aprovado com media {media}')
else:
    print(f'infelizmente você foi reprovado com média {media}')