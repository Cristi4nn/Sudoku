class Jogador:
    """
        Esta classe representa as informações do jogador.
    """
    __atributos  = {'nick', 'pontuacaoAtual','quantErros'}
    __metodos    = {'__init__','__str__','getManual','getAtributos','getMetodos'}

    
    def __init__(self, nick = 'Jogador',pontuacaoAtual=0, quantErros=0):
        self.nick = nick                        # Nome do jogador no jogo.
        self.pontuacaoAtual = pontuacaoAtual    # Quantas posições o jogador já acertou até agora
        self.quantErros = quantErros            # Quantas vezes o jogador errou
        
    def __str__(self):
        """
            Este método, usado para representação em string, será retornada a String que contém as descrições de todos os métodos e 
            atributos das classes.
            
        """
       pass

    def getAtributos():
        """
            Esta função estática (chamada sempre através de Jogador.getAtributos()) retorna um 
            conjunto com os nomes dos atributos desta classe.
            
            (None) -> set
        """
        return __atributos
    
    def getMetodos():
        """
            Esta função estática (chamada sempre através de Jogador.getMetodos()) retorna um 
            conjunto com os nomes dos métodos desta classe.
            
            (None) -> set
        """
        return __metodos
