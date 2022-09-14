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

    #