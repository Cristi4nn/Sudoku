from jogador import *
import matplotlib.pyplot as plt


class Log:
    """
    Classe que conterá as estatística do jogo
    """
    __atributos  = {}
    __metodos    = {'__init__','__str__','getManual','getAtributos','getMetodos','arquivo_jogadas','arquivo_erros','arquivo_save'}
    def __init__(self):
        """
            Metodo construtor
        """
        pass

    def __str__(self):
        """
            Este método, usado para representação em string, será retornada a String que contém as descrições de todos os métodos e 
            atributos das classes.
            
        """
        pass
        

    def getAtributos():
        """
            Esta função estática (chamada sempre através de Log.getAtributos()) retorna um 
            conjunto com os nomes dos atributos desta classe.
            
            (None) -> set
        """
        return __atributos
    
    def getMetodos():
        """
            Esta função estática (chamada sempre através de Log.getMetodos()) retorna um 
            conjunto com os nomes dos métodos desta classe.
            
            (None) -> set
        """
        return __metodos

    def arquivoJogadas(self,jogada):
        """
            Esta função que registra as jogadas feitas pelo usuário do sudoku, salvando-as num arquivo'.txt'
        """
        arq= Jogador().nick + '_jogadas.txt'
        
        arquivo1=open(arq,'a')
        arquivo1.write(jogada)
        arquivo1.close()
        
    def arquivoErros(self,erros):
        """
            Esta função que registra as jogadas feitas pelo usuário do sudoku, salvando-as num arquivo'.txt'
        """
        arq= Jogador().nick + '_erros.txt'
        
        arquivo1=open(arq,'a')
        arquivo1.write(erros)
        arquivo1.close()

    def arquivoSave(self,save):
        """
            Esta função que registra as jogadas feitas pelo usuário do sudoku, salvando-as num arquivo'.txt'
        """
        arq= Jogador().nick + '_save.txt'
        
        arquivo1=open(arq,'a')
        arquivo1.write(save)
        arquivo1.close()

    def getManual():
        """
            Esta função estática (chamada sempre através de Log.getManual()) retorna um 
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            
            (None) -> dict
        """
        manual = dict()
        manual['__init__']              = Log.__init__.__doc__
        manual['__str__']               = Log.__str__.__doc__
        manual['arquivoJogadas']           = Log.arquivoJogadas.__doc__
        manual['arquivoErros']     = Log.arquivoErros.__doc__
        manual['arquivoSave']     = Log.arquivoSave.__doc__
        manual['getManual']          = Log.getManual.__doc__
        manual['getAtributos']         = Log.getAtributos.__doc__
        manual['getMetodos']            = Log.getMetodos.__doc__
        return manual

        
