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
    def __init__(self, palavra): #inicia a classe
        self.palavra = palavra
        self.letra_errada = []
        self.letra_certa = []

    #metodo para adivinhar a letra
    def guess(self, letra):
        if letra in self.palavra and letra not in self.letra_certa: #se a letra tiver na palavra e a letra nao estiver na lista de letra certa vai adicionar na lista de letra certa
            self.letra_certa.append(letra)
        elif letra not in self.palavra and letra not in self.letra_errada: #se a letra nao tiver na palavra e a letra nao estiver na lista de letra errada vai adicionar na lista de letra errada
            self.letra_errada.append(letra)
        else:
            return False
        return True

    #metodo para ver se acabou o jogo
    def game_over(self):
        return self.game_win() or (len(self.letra_errada)==6) #quando a lista estiver com 6 itens na lista errada, perdemos

    #metodo para ver se o jogador venceu
    def game_win(self):
        if '_' not in self.hide_letter(): #quando nao tiver mais underline vencemos o jogo
            return True
        return False

    #metodo para nao mostrar a letra no tabuleiro
    def hide_letter(self):
        rtn =''
        for letra in self.palavra: #pra cada letra na sequencia de letras
            if letra not in self.letra_certa: #se a letra nao estiver na palavra, preenche com underline
                rtn += '_'
            else:
                rtn += letra #se estiver preenche com a letra
        return rtn

    #metodo para checar o status do game e imprimir o tabuleiro na tela
    def print_game_status(self):
        print(board[len(self.letra_errada)]) #vai trazer cada etapa da forca, quando estiver vazia, trás o primeiro elemento da lista board, e assim sucessivamente
        print('\nPalavra: ' + self.hide_letter()) #pela primeira vez so chama underline
        print('\n Letras erradas: ')
        for letra in self.letra_errada: #para cada letra na lista de letras erradas, imprime a lista
            print(letra)
        print () #print linha vazia
        print('Letras corretas: ')
        for letra in self.letra_certa: #para cada letra na lista de letras certas, imprime a lista
            print(letra)
        print () #print linha vazia

#função para ler palavra de forma aleatoria
def rand_word():
    with open('palavras.txt', 'rt') as f:
        banco = f.readlines()
    return banco[random.randint(0,len(banco))].strip()

#execução do programa

def main():

    #objeto
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
        print('\nA palavra era ' + game.palavra)
    print('\nAgora vá estudar')

#executa o programa
if __name__ == '__main__':
    main()