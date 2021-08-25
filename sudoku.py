"""
    Sudoku.
      "O sudoku é um jogo baseado na colocação lógica de números. O objetivo do jogo é a colocação de números de 1 a 9 
      em cada uma das células vazias numa grade de 9x9, constituída por 3x3 subgrades chamadas regiões. 
      quebra-cabeça contém algumas pistas iniciais, que são números inseridos em algumas células, 
      de maneira a permitir uma indução ou dedução dos números em células que estejam vazias. 
      Cada coluna, linha e região só pode ter um número de cada um dos 1 a 9." - Fonte: https://pt.wikipedia.org/wiki/Sudoku

      Dada a descrição simples do jogo, algumas opções são escolhas do usuário:
      - Tipo de jogo: até completar toda a grade ou por tempo (padrão até completar a grade)
      - Dificuldade: fácil, difícil (padrão fácil)


        Exemplo de uma grade completa:
    
      ->      8 9 2  | 7 3 6  | 1 4 5
              7 1 5  | 9 8 4  | 3 6 2
               6 4 3  | 1 5 2  | 9 7 8
              - - - - - - - - - - - - - 
              1 3 7  | 6 2 9  | 5 8 4
              2 8 4  | 3 7 5  | 6 1 9
              5 6 9  | 4 1 8  | 2 3 7
              - - - - - - - - - - - - - 
              4 7 1  | 5 9 3  | 8 2 6
              9 2 6  | 8 4 1  | 7 5 3
              3 5 8  | 2 6 7  | 4 9 1

        Incialmente a GRADE terá algumas posições livres onde o JOGADOR irá decidir que valor irá
        inserir nessas posições.
        Quando o jogo estiver completo, o jogo termina e o vencedor recebe uma mensagem positiva.
    """
# Document properties
__author__ = ['Cristian_Andrade','Ramiro_Reis']
__copyright__ = 'Copyright_2021'
__credits__ = __author__
__license__ = 'GPL'
__version__ = '1.0.0'
__maintainer__ = 'Cristian_Andrade' # Responsável por manter o programa funcionando
__email__ = 'ihuunter@poli.ufrj.br'
__status__ = 'Production'

from interfaceUsuario import *
from ferramentas import *
from tela import *
from grade import *
from jogador import *
from log import *
from validSudoku import *

class Sudoku(Ferramentas):
    """
        Esta classe representa a funcionalidade do jogo em si. Aqui são conectadas todas
        as classes de forma a criar os métodos responsáveis pela mecânica do jogo.
    """
    __atributos  = {'dificuldade', 'ateCompletar'}
    __metodos    = {'__init__','__str__','jogada','terminou','vencedor','getManual','getAtributos','getMetodos'}

    def __init__(self,dificuldade=True,ateCompletar=True):
        """
            O construtor cria um novo jogo a partir das configurações passadas:
            
            - 
            - Tipo de jogo: até completar toda a grade ou por tempo (padrão até completar a grade)
            - Dificuldade: fácil, difícil (padrão fácil)
        """
        self.dificuldade = dificuldade          # Dificuldade: fácil, difícil (padrão fácil)
        self.ateCompletar = ateCompletar        # Tipo de jogo: até completar toda a grade ou por tempo (padrão até completar a grade)

    
    def __str__(self):
        """
            Este método, usado para representação em string, será retornada a String que contém as descrições de todos os métodos e 
            atributos das classes.
            
        """
        saida = ""
        
        manualTela = Sudoku.getManual()
        
        saida += 'MANUAL DA CLASSE TELA\n'
        
        for chave in manualTela:
            saida += f'{chave} : {manualTela[chave]}\n'
        saida +='\n'
        
        return saida
    
    def jogada(self,pos,valor):
        """
           Faz a jogada do 'jogador', ou seja, insere o valor escolhido na posição 'pos' 
        """
        pass
    
    def terminou(self):
        """
            Retorna 'True' se o jogo estiver completo e 'False' caso contrário
        """
        return None
    
    def vencedor(self):
        """ 
                asa
        """
        pass

    def getAtributos():
        """
            Esta função estática (chamada sempre através de Sudoku.getAtributos()) retorna um 
            conjunto com os nomes dos atributos desta classe.
            
            (None) -> set
        """
        return __atributos
    
    def getMetodos():
        """
            Esta função estática (chamada sempre através de Sudoku.getMetodos()) retorna um 
            conjunto com os nomes dos métodos desta classe.
            
            (None) -> set
        """
        return __metodos

    def getManual():
        """
            Esta função estática (chamada sempre através de Sudoku.getManual()) retorna um 
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            
            (None) -> dict
        """
        manual = dict()
        manual['__init__']              = Sudoku.__init__.__doc__
        manual['__str__']               = Sudoku.__str__.__doc__
        manual['jogada']           = Sudoku.jogada.__doc__
        manual['terminou']     = Sudoku.terminou.__doc__
        manual['vencedor']             = Sudoku.vencedor.__doc__
        manual['getManual']          = Sudoku.getManual.__doc__
        manual['getAtributos']         = Sudoku.getAtributos.__doc__
        manual['getMetodos']            = Sudoku.getMetodos.__doc__
        manual['dificuldade']                 = '# Dificuldade: fácil, difícil (padrão fácil)'
        manual['ateCompletar']                = '# Tipo de jogo: até completar toda a grade ou por tempo (padrão até completar a grade)'
        return manual
