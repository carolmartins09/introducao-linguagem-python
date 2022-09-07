import forca
import adivinhacao

def escolha_jogo():
    print("********************************")
    print("******Escolha o seu jogo!*******")
    print("********************************")

    print("(1) forca (2) adivinhação")

    jogo = int(input("Qual o jogo?"))

    if(jogo == 1):
        print ("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print ("Jogando Adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolha_jogo()
