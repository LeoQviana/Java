import random

palavra= ['uva','banana','kiwi','melancia', 'acerola', 'abacate', 'abacaxi','caqui','goiaba','jambo']
palavra_secreta=random.choice(palavra)
palavra_escondida= '_' * len(palavra_secreta)
letras_escolhidas=[]
chances=10

print('-=-'*20)
print('                     JOGO DA FORCA')
print('-=-'*20)
print("                     Vamos começar!")
print("A palavra é:")

while True:
    print(palavra_escondida)
    print("Qual letra você acha que a palavra tem?")
    letra=str(input('\n'+"Digite uma letra:"))

    if letra in letras_escolhidas:
        print("Você ja usou essa letra!")
        continue
    letras_escolhidas.append(letra)
    if letra in palavra_secreta:
        secreta = ""
        for x in range(len(palavra_secreta)):
            if palavra_secreta[x] == letra:
                secreta += letra
            else:
                secreta += palavra_escondida[x]
        palavra_escondida=secreta
    else:
        print("A letra não está na palavra.")
        chances -= 1
        print(f"Você tem {chances} tentativas.")
        if chances == 0:
            print(f"Você perdeu a palavra era {palavra_secreta}")
            break
    if palavra_escondida == palavra_secreta:
        print("PARABÉNS VOCÊ ACERTOU, MIZERAVI")
        break