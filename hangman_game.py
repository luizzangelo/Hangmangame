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

class Hangman:

    #metodo construtor
    def __init__(self, word):
        self.word = word
        self.letra_errada = []
        self.letra_certa = []

    #metodo para adivinhar a letra
    def guess(self, letter):
        if letter in self.word and letter not in self.letra_certa:
            self.letra_certa.append(letter)
        elif letter not in self.word and letter not in self.letra_errada:
            self.letra_errada.append(letter)
        else:
            return False
        return True

    #metodo para ver se acabou o jogo
    def game_over(self):
        return self.game_win() or (len(self.letra_errada)==6)

    #metodo para ver se o jogador venceu
    def game_win(self):
        if '_' not in self.hide_letter():
            return True
        return False

    #metodo para nao mostrar a letra no tabuleiro
    def hide_letter(self):
        rtn =''
        for letter in self.word:
            if letter not in self.letra_certa:
                rtn += '_'
            else:
                rtn += letter
        return rtn

    #metodo para checar o status do game e imprimir o tabuleiro na tela
    def print_game_status(self):
        print(board[len(self.letra_errada)])
        print('\nPalavra: ' + self.hide_letter())
        print('\n Letras erradas: ',)
        for letter in self.letra_errada:
            print(letter,)
        print ()
        print('Letras corretas: ',)
        for letter in self.letra_certa:
            print(letter,)
        print ()

#função para ler palavra de forma aleatoria
def rand_word():
    with open('palavras.txt', 'rt') as f:
        bank = f.readlines()
    return bank[random.randint(0,len(bank))].strip()

#execução do programa

def main():
    game = Hangman(rand_word())

    #enquanto o jogo nao tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.game_over():
        game.print_game_status()
        entrada = input('\nDigite uma letra: ')
        game.guess(entrada)

    #verifica o status do jogo
    game.print_game_status()

    #de acordo com o status, imprime a mensagem na tela para o usuario
    if game.game_win():
        print('\nParabéns! Você Venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('\nA palavra era' + game.word)
    print('\nAgora vá estudar')

#executa o programa
if __name__ == '__main__':
    main()