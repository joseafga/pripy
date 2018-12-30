from gtts import gTTS
from glob import glob
import subprocess as s


def load(callback=None):
    """ Funcao chamada no inicio do programa

    Args:
        callback (callable, optional): funcao chamada ao termino do carregamento
    """
    # TODO: fazer uma classe para o programa
    # variaveis
    phases = []

    # abre arquivo `frases` em modo leitura
    with open('frases', 'r') as file:
        for line in file:
            phases.append([l.strip() for l in line.split(';')])

    # pega todos arquivos gravados
    recs = glob("songs/*.mp3")

    # verifica gravacoes
    for phase in phases:
        if 'songs/%s' % phase[1] not in recs:
            # TODO: gravar automaticamente
            # gravar()
            print('Gravando nova frase: %s' % phase[0])

    # chama função de callback
    if (callable(callback)):
        callback()


def gravar():
    frase = input("Digite a frase a ser gravada: ")
    arquivo = frase.replace(" ", "")
    arquivo = arquivo.lower()

    file = open('frases', 'a')
    texto = []
    texto.append(frase + ";" + arquivo + ".mp3")
    texto.append("\n")
    file.writelines(texto)
    file.close

    voz = gTTS(frase, lang="pt")
    voz.save("songs/" + arquivo + ".mp3")
    s.call(['mpg123', "songs/" + arquivo + ".mp3"])


def ler():
    print("Lendo")
    exit


def menu():
    menu = input("O que deseja fazer? (1=gravar, 2-ler) ")
    if menu == "1":
        gravar()
    elif menu == "2":
        ler()
    else:
        print("Opção invalida")


load(menu)
