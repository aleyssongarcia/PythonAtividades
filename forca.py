import random

palavras = ['python', 'java', 'javascript', 'html', 'css']

palavra_secreta = random.choice(palavras)

vidas = 6

letras_digitadas = []

while vidas > 0:
    palavra = ""
    for letra in palavra_secreta:
        if letra in letras_digitadas:
            palavra += letra
        else:
            palavra += "_"
    print("Palavra secreta: " + palavra)
    
    if palavra_secreta == palavra:
        print("Parabéns, você ganhou!")
        break
        
    letra = input("Digite uma letra: ")
    
    if letra in letras_digitadas:
        print("Você já digitou essa letra, tente outra.")
    else:
        letras_digitadas.append(letra)
        
        if letra in palavra_secreta:
            print("A letra está na palavra secreta!")
        else:
            print("A letra não está na palavra secreta.")
            vidas -= 1
    
    print("Vidas restantes: " + str(vidas))
    
    if vidas == 0:
        print("Você perdeu! A palavra secreta era " + palavra_secreta)
