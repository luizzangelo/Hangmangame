#jogo da forca
# POO - programação orientada a objetos

import random
board = ['''
>>>>>>>>>>>>>>>>>>HANGMAN<<<<<<<<<<<<<<<<<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
    |
==========''', '''

+---+
|   |
O   |
    |
    |
    |
    |
==========''', '''

+---+
|   |
O   |
|   |
    |
    |
    |
==========''','''

+----+
|    |
O    |
|\   |
     |
     |
     |
==========''','''

+-----+
 |    |
 O    |
/|\   |
      |
      |
      |
==========''','''

+-----+
 |    |
 O    |
/|\   |
  \   |
      |
      |
==========''','''

+-----+
 |    |
 O    |
/|\   |
/ \   |
      |
      |
=========='''
]

print('\nPalavra: ')

print('\nLetras erradas: ')

print('\nLetras corretas: ')

print(input('\nDigite uma letra: '))

class Hangman:

#metodo construtor
    def __init__(self, word):

#metodo para adivinhar a letra
    def guess(self, letter):

#metodo para ver se acabou o jogo
    def game_over(self):

#metodo para ver se o jogador venceu
    def game_win(self):

#metodo para nao mostrar a letra
    def hide_letter(self):

#metodo para checar o status do game e imprimir o tabuleiro na tela
    def print_game_status(self):

#função para ler palavra de forma aleatoria
def rand_word():
    with open('palavras.txt', 'rt') as f:
        banco = f.readlines()
    return banco[random.randint(0, len(banco))].strip()

#execução do programa

def main():
    game = Hangman(rand_word())

    #enquanto o jogo nao tiver terminado, print do status, solicita uma letra e faz a leitura do caracter

    #verifica o status do jogo
    game.print_game_status()

    #de acordo com o status, imprime a mensagem na tela para o usuario
    if game.game_win():
        print('\nParabéns! Você Venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('\nA palavra era' +game.word)
    print('\nAgora vá estudar')

#executa o programa
if __name__ == '__main__':
    main()