tabuleiro= [[0,0,0],
            [0,0,0],
            [0,0,0]]

def ganhou():
    for x in range(3):
        soma=tabuleiro[x][0]+tabuleiro[x][1]+tabuleiro[x][2]
        if soma==3 or soma==-3:
            return 1
    for y in range(3):
        soma=tabuleiro[0][y]+tabuleiro[1][y]+tabuleiro[2][y]
        if soma==3 or soma==-3:
            return 1
    diagonal1=tabuleiro[0][0]+tabuleiro[1][1]+tabuleiro[2][2]
    diagonal2=tabuleiro[0][2]+tabuleiro[1][1]+tabuleiro[2][0]
    if diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3:
        return 1

    return 0

def menu():
    continuar=1
    while continuar:
        print("JOGO DA VELHA")
        escolha=int(input("0. Sair \n"+
                            "1. Jogar!\n"))
        if escolha==1:
            game()
            continue
        elif escolha==0:
            print("Saindo...")
            break
        else:
            print("Apenas 0 ou 1!")

def exibe():
    for x in range(3):
        for y in range(3):
            if tabuleiro [x][y]==0:
                print("_", end=' ')
            if tabuleiro [x][y]==1:
                print("X", end=' ')
            elif tabuleiro [x][y]==-1:
                print("O", end=' ')

        print()
def game():
    jogada=0

    while ganhou() == 0:
        print("\n Jogador",jogada%2+1)
        exibe()
        linha= int(input("\nLinha:"))
        coluna=int(input("Coluna"))

        if tabuleiro[linha -1][coluna-1]==0:
            if(jogada%2+1)==1:
                tabuleiro[linha-1][coluna-1]=1
            else:
                tabuleiro[linha-1][coluna-1]=1
        else:
            print("Esse lugar ja está preenchido")
            jogada-=1

        if ganhou():
            print("Jogador",jogada%2+1,"ganhou após",jogada+1,"rodadas")
        jogada+=1

menu()
