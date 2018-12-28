from gtts import gTTS
import subprocess as s


def gravar():
    frase=input("Digite a frase a ser gravada: ")
    arquivo=frase.replace(" ", "")
    arquivo=arquivo.lower()

    file = open('frases', 'a')
    texto = []
    texto.append(frase+";"+arquivo+".mp3")
    texto.append("\n")
    file.writelines(texto)
    file.close


    voz = gTTS(frase, lang="pt")
    voz.save("songs/"+arquivo+".mp3")
    s.call(['mpg123',"songs/"+arquivo+".mp3"])

def ler():
    print("Lendo")
    exit

def menu():
    menu=input("O que deseja fazer? (1=gravar, 2-ler) ")
    if menu == "1":
        gravar()
    elif menu == "2":
        ler()
    else:
        print("Opção invalida")

menu()