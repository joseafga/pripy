"""
menu

Menu Interativo para o PRIpy

:copyright: © 2018 by Projeto PRI <https://projeto-pri.github.io>.
:license: MIT, see LICENSE for more details.
"""
import os


class Menu():
    """ Menu do programa

        Args:
        items (list): lista com os items exibidos
        options (list): lista com as opcoes do sistema

    Attributes:
        items (list): lista com os items exibidos
        options (list): lista com as opcoes do sistema
        actions (dict): dicionario com identificacao e comando a ser executado
    """

    def __init__(self, items, options):
        self.items = items
        self.options = options

    def clear(self):
        """ Limpa a tela """
        os.system('clear')

    def handler(self, cmd):
        """ Manipula o comando selecionado
        Este metodo deve ser sobreescrito por uma funcao especifica

        Args:
            cmd (str): comando selecionado pelo usuario
        """
        pass

    def choice(self, txt=" > "):
        """ Permite entrada do usuario

        Args:
            txt (str, optional): texto que sera exibido antes da entrada
        """
        choice = input(txt)  # entrada do usuario

        os.system('clear')

        # TODO validar
        if choice == '':
            self.draw()
        # passa comando para funcao manipuladora
        else:
            try:
                self.handler(self.actions[choice])
                self.draw()  # volta para menu

            except KeyError:
                print("Opção inválida.\n")
                self.draw()

        return choice

    def draw(self):
        """ Desenha menu com items """
        self.clear()
        self.actions = {}  # redefine variável
        i = 1  # redefine interator

        # exibe items
        for item in self.items:
            print(" [{:^3}] {}".format(i, item[0]))
            self.actions[i] = item[1]
            i += 1

        # exibe items do sistema
        for item in self.options:
            print(" [{:^3}] {}".format(item[0], item[1]))
            self.actions[item[0]] = item[2]
        self.choice()
