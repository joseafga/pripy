# PRIpy ❤

## O que é PRIpy?
PRIpy faz parte do **Projeto PRI**. É um programa criado em Python e visa ajudar as pessoas que estão passando por alguma necessidade fisica/mental e não consegue se comunicar com as pessoas.
Um exemplo é um pessoa que sofreu algum tipo de AVC, normalmente a pessoa apesar de ter uma confusão mental consegue fazer leituras simples, também em alguns casos **que é o caso que se baseamos este projeto** estas pessoas conseguem movimentar alguma parte do corpo, o dedo por exemplo.  
Foi ai que surgiu a ideia deste e outros softwares livres do projeto, um programa em Python que permite criar frases arbitrárias que serão selecionadas pelo usuário num menu.

## Instalação
*É recomendada a utilização de um [ambiente virtual](https://packaging.python.org/key_projects/#virtualenv) do python para a instalação das dependências, porém não é obrigatório.*

Instalando dependências com pip:

    $ pip install gtts pydub simpleaudio

Agora basta fazer o download ou clonar o repositório do PRIpy no local desejado.

    $ git clone git@github.com:projeto-pri/pripy.git

## Utilização
Para utilizar o PRIpy, ative o ambiente virtual (caso tenha utilizado para as dependências) e execute o arquivo `pripy.py`.

    $ python pripy.py

Nota: No arquivo `frases` ficam armazenados todas os sons que o programa irá ler, caso sejam adicionadas frases das quais não existam o arquivo de som correspondente, estes serão criados na inicialização do programa. É útil para a inserção de gravações personalizadas, desta forma basta indicar a frase e o arquivo correspondente numa nova linha que será reconhecido.

## Site do Projeto
https://projeto-pri.github.io/

## Dependências
* python 3
* pip install gtts
* pip install pydub simpleaudio
