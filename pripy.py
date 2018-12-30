from gtts import gTTS
from glob import glob
from pydub import AudioSegment, playback
import subprocess as s
import terminalmenu

# variaveis
phases = []


def load(callback=None):
    """ Funcao chamada no inicio do programa

    Args:
        callback (callable, optional): funcao chamada ao termino do carregamento
    """
    # TODO: fazer uma classe para o programa, estruturar melhor
    global phases
    phases = []  # redefine a variavel

    # abre arquivo `frases` em modo leitura
    with open('frases', 'r') as file:
        for line in file:
            phases.append([l.strip() for l in line.split(';')])

    # pega todos arquivos gravados
    recs = glob("songs/*.mp3")

    # verifica gravacoes
    for phase in phases:
        if "songs/%s" % phase[1] not in recs:
            # TODO: fazer assincrono
            print("Gravando nova frase: %s" % phase[0])
            text_to_file(phase[0], phase[1])

    # chama funcao de callback
    if (callable(callback)):
        callback()


def text_to_file(phase, filename):
    """ Gera audio da frase atraves do Google Text to Speech

    Args:
        phase (str): frase que sera gerada
        filename (str): nome do arquivo a ser salvo com extensao

    Returns:
        Retorna uma string com caminho do arquivo gerado
    """
    path = "songs/%s" % filename  # caminho para arquivo

    # gera e salva frase pelo gTTS
    voice = gTTS(phase, lang='pt')
    voice.save(path)

    return path


def gravar():
    frase = input("Digite a frase a ser gravada: ")
    filename = frase.replace(" ", "").lower() + '.mp3'
    txt = "{};{}\n".format(frase, filename)

    # adiciona texto ao arquivo
    with open('frases', 'a') as file:
        file.write(txt)

    sound = AudioSegment.from_mp3(text_to_file(frase, filename))
    playback.play(sound)


def ler():
    print("Lendo")
    exit(0)


def menu(cmd):
    if cmd == 'add':
        gravar()
    elif cmd == 'exit':
        exit(0)
    elif '.mp3' in cmd:
        # TODO separar funcao e executar de maneira assincrona
        sound = AudioSegment.from_mp3('songs/%s' % cmd)
        playback.play(sound)
    else:
        print('Opção inválida')


if __name__ == '__main__':
    load()  # TODO recarregar frases ao adicionar nova

    my_menu = terminalmenu.Menu(phases, [
        ['+', 'Adicionar nova frase', 'add'],
        ['q', 'Sair', 'exit']
    ])
    my_menu.handler = menu
    my_menu.draw()
