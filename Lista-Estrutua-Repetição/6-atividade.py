"""
Seja criativo ao desenvolver este programa.
a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome
personalizado.
c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos
convites. Imprima o nome das pessoas que não poderão comparecer.
d. Modifique sua lista, substitua os desistentes por novos convidados.
e. Exiba um novo convite para cada pessoa que continua presente em sua lista.
"""

convidados = ['Jorge Python', 'Annie Java', 'Luis Csharp', 'Antonio Javascript', 'Francisco C++']

# codigo enviando os convites
mensagem = "Olá, você está convidado para um jantar em minha casa na próxima semana. Espero contar com sua presença!"
for convidado in convidados:
    print(f"Enviando convite para {convidado}...")
    print(mensagem)
    print()

# adicionando a desistencia e removendo o convidado.
desistencia = 'Jorge Python'
print(f"{desistencia} não poderá comparecer ao jantar.")
convidados.remove(desistencia)

#  trocando o desistente por um novo convidado.
print(f"Adicionando novo convidado...")
novo_convidado = 'Junior Golang'
convidados.append(novo_convidado)

# Reenviando os convites.
print("Enviando novos convites...")
for convidado in convidados:
    print(f"Enviando convite para {convidado}...")
    print(mensagem)
    print()