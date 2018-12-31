from gtts import gTTS
from glob import glob
from pydub import AudioSegment, playback
from multiprocessing import Process
import terminalmenu


def load(callback=None):
    """ Funcao chamada no inicio do programa

    Args:
        callback (callable, optional): funcao chamada ao termino do carregamento
    """
    # TODO: fazer uma classe para o programa, estruturar melhor
    phases = []  # redefine a variavel

    # abre arquivo `frases` em modo leitura
    with open('frases', 'r') as file:
        for line in file:
            phases.append([l.strip() for l in line.split(';')])

    # pega todos arquivos gravados
    recs = glob("sons/*.mp3")

    # verifica gravacoes
    for phase in phases:
        if "sons/%s" % phase[1] not in recs:
            # TODO: fazer assincrono
            print("Gravando nova frase: %s" % phase[0])
            text_to_file(phase[0], phase[1])

    # chama funcao de callback
    if (callable(callback)):
        callback(phases)


def text_to_file(phase, filename):
    """ Gera audio da frase atraves do Google Text to Speech

    Args:
        phase (str): frase que sera gerada
        filename (str): nome do arquivo a ser salvo com extensao

    Returns:
        Retorna uma string com caminho do arquivo gerado
    """
    path = "sons/%s" % filename  # caminho para arquivo

    # gera e salva frase pelo gTTS
    voice = gTTS(phase, lang='pt')
    voice.save(path)

    return path


def play(path):
    """ Reproduz um arquivo em formato mp3

    Args:
        path (str): caminho do arquivo
    """
    sound = AudioSegment.from_mp3(path)
    playback.play(sound)


def play_async(path):
    """ Reproduz um arquivo em formato mp3 de modo assincrono

    Args:
        path (str): caminho do arquivo
    """
    p = Process(target=play, args=(path,))
    p.start()


def gravar():
    """ Grava nova frase manualmente """
    frase = input("Digite a frase a ser gravada: ")
    filename = frase.replace(" ", "").lower() + '.mp3'
    txt = "{};{}\n".format(frase, filename)

    # adiciona texto ao arquivo
    with open('frases', 'a') as file:
        file.write(txt)

    play_async(text_to_file(frase, filename))


def menu(cmd):
    """ Menu de comandos
    Aqui é verificada a entrada do usuario e o exec comando correspondente

    Args:
        cmd (str): string do comando
    """
    if cmd == 'add':
        global main_menu  # pega menu principal para atualizar items

        gravar()
        load(main_menu.update)  # recarrega frases
    elif cmd == 'exit':
        exit(0)  # sai do programa
    elif '.mp3' in cmd:
        play_async("sons/%s" % cmd)  # toca o audio
    else:
        print('Opção inválida')


if __name__ == '__main__':
    main_menu = terminalmenu.Menu([], [
        ['+', 'Adicionar nova frase', 'add'],
        ['q', 'Sair', 'exit']
    ])

    main_menu.handler = menu
    load(main_menu.update)  # TODO melhorar isso
    main_menu.draw()
