class Ferramentas:
    """
        Esta super classe inclui todos os métodos que podem vir a ser úteis para a
        mecânica do jogo, independente das classes criadas para o jogo específico.
    """
    __atributos  = {}
    __metodos    = {'__init__','__str__','cronometro','opcoes','getManual','getAtributos','getMetodos'}
    
    def __init__(self):
        """
            Método construtor
        """
        pass


    def __str__(self):
        """
            Este método, usado para representação em string, será retornada a String que contém as descrições de todos os métodos e 
            atributos das classes.
            
        """
        pass


    def cronometro(self):
        """
        Está função cria um cronometro que pode ser utilizado para determinar um limite de tempo ou 
        para determinar estatísticas
        """
        pass

    def opcoes(self):
        """
            Esta função determina as preferências de customização do jogador
        """
        pass

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
            Esta função estática (chamada sempre através de Ferramentas.getManual()) retorna um 
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            
            (None) -> dict
        """
        manual = dict()
        manual['__init__']              = Ferramentas.__init__.__doc__
        manual['__str__']               = Ferramentas.__str__.__doc__
        manual['cronometro']           = Ferramentas.cronometro.__doc__
        manual['opcoes']     = Ferramentas.opcoes.__doc__
        manual['getManual']          = Ferramentas.getManual.__doc__
        manual['getAtributos']         = Ferramentas.getAtributos.__doc__
        manual['getMetodos']            = Ferramentas.getMetodos.__doc__
        return manual
