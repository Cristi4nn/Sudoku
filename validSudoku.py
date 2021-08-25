class ValidSudoku:
    """
    Esta Classe cria uma coleção de grades válida para o sudoku que seram necessários para
    a gameplay.
    """

    __atributos  = {}
    __metodos    = {'__init__','__str__','getManual','getAtributos','getMetodos'}

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
        saida = ""
        
        manualTela = ValidSudoku.getManual()
        
        saida += 'MANUAL DA CLASSE TELA\n'
        
        for chave in manualTela:
            saida += f'{chave} : {manualTela[chave]}\n'
        saida +='\n'
        
        return saida

    def getAtributos():
        """
            Esta função estática (chamada sempre através de ValidSudoku.getAtributos()) retorna um 
            conjunto com os nomes dos atributos desta classe.
            
            (None) -> set
        """
        return __atributos
    
    def getMetodos():
        """
            Esta função estática (chamada sempre através de ValidSudoku.getMetodos()) retorna um 
            conjunto com os nomes dos métodos desta classe.
            
            (None) -> set
        """
        return __metodos

    def getManual():
        """
            Esta função estática (chamada sempre através de ValidSudoku.getManual()) retorna um 
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            
            (None) -> dict
        """
        manual = dict()
        manual['__init__']              = ValidSudoku.__init__.__doc__
        manual['__str__']               = ValidSudoku.__str__.__doc__
        manual['getManual']          = ValidSudoku.getManual.__doc__
        manual['getAtributos']         = ValidSudoku.getAtributos.__doc__
        manual['getMetodos']            = ValidSudoku.getMetodos.__doc__
        return manual
