from validSudoku import * 

class Grade:
    """
        Esta classe representa a coleção de posições da grade do sudoku e é responsável pelo controle da grade em si
    """
    __atributos  = {'numPreSelecionados', 'opcoes'}
    __metodos    = {'__init__','__str__','verificaPosicao','verificaValor','apagar','gradeCompleta','maxErros','getManual','getAtributos','getMetodos'}
    
    def __init__(self, numPreSelecionados=""):
        """
            A partir de uma matriz de números pré selecionados, será criadas posição livres aleatóriamente, onde as posições não livres
            são imutáveis.
        """
        self.numPreSelecionados = numPreSelecionados      # Uma matriz de números pré selecionados
        
        
    def __str__(self):
        """
            Este método, usado para representação em string, será retornada a String que contém as descrições de todos os métodos e 
            atributos das classes.
            
        """
        saida = ""
        
        manualTela = Grade.getManual()
        
        saida += 'MANUAL DA CLASSE TELA\n'
        
        for chave in manualTela:
            saida += f'{chave} : {manualTela[chave]}\n'
        saida +='\n'
        
        return saida

    def verificaPosição(self,pos):
        """
            Esta função verifica se a posição escolhida 'pos' é uma posição livre para inserir,
            retornando 'True' caso seja e 'False' caso contrário. 
        """
        return None
        
    def verificaValor(self,pos,valor):
        """
            Esta função verifica se o 'valor' inserido na posição 'pos' está no lugar certo
            verificando linha, coluna e subgrade, 
            retornando 'True' se for e 'False' caso contrário.
            
        """
            # A ideia é que o valor seja inserido de qualquer forma, mas aparece uma mensagem de que o valor
            # está na posição errada caso na posição escolhida não seja o valor inserido
            # não sendo inserido valor apenas se for uma posição não livre
        return None
    
    def apagar(self,pos):
        """ 
            Função que apaga o valor inserido de uma determina posição 'pos',
            exceto se for uma posição imutável.
        """
        pass

    def gradeCompleta(self):
        """ 
            Esta função retorna 'True' se a grade estiver completa.
        """
    
    def maxErros(self):
        """
            Esta fnção verifica se o jogador atingiu um limite máximo de erros
            permitidos por partida, retorna 'True' caso tenha atingido e 'False' caso contrário
        """
        return None

    def getAtributos():
        """
            Esta função estática (chamada sempre através de Tela.getAtributos()) retorna um 
            conjunto com os nomes dos atributos desta classe.
            
            (None) -> set
        """
        return __atributos
    
    def getMetodos():
        """
            Esta função estática (chamada sempre através de Tela.getMetodos()) retorna um 
            conjunto com os nomes dos métodos desta classe.
            
            (None) -> set
        """
        return __metodos

    def getManual():
        """
            Esta função estática (chamada sempre através de Grade.getManual()) retorna um 
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            
            (None) -> dict
        """
        manual = dict()
        manual['__init__']              = Grade.__init__.__doc__
        manual['__str__']               = Grade.__str__.__doc__
        manual['verificaPosicao']           = Grade.verificaPosição.__doc__
        manual['verificaValor']     = Grade.verificaValor.__doc__
        manual['apagar']             = Grade.apagar.__doc__
        manual['gradeCompleta']          = Grade.gradeCompleta.__doc__
        manual['maxErros']         = Grade.maxErros.__doc__
        manual['getAtributos']          = Grade.getAtributos.__doc__
        manual['getMetodos']            = Grade.getMetodos.__doc__
        manual['getManual']            = Grade.getManual.__doc__
        manual['numPreSelecionados']   = '# Uma matriz de números pré selecionados'
        return manual
