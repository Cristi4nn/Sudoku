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
        saida = ""
        
        manualTela = Jogador.getManual()
        
        saida += 'MANUAL DA CLASSE TELA\n'
        
        for chave in manualTela:
            saida += f'{chave} : {manualTela[chave]}\n'
        saida +='\n'
        
        return saida

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

    def getManual():
        """
            Esta função estática (chamada sempre através de Jogador.getManual()) retorna um 
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            
            (None) -> dict
        """
        manual = dict()
        manual['__init__']              = Jogador.__init__.__doc__
        manual['__str__']               = Jogador.__str__.__doc__
        manual['getManual']          = Jogador.getManual.__doc__
        manual['getAtributos']         = Jogador.getAtributos.__doc__
        manual['getMetodos']            = Jogador.getMetodos.__doc__
        manual['nick']                   = '# Nome do jogador no jogo.'
        manual['pontuacaoAtual']   = '# Quantas posições o jogador já acertou até agora'
        manual['quantErros']            = '# Quantas vezes o jogador errou'
        return manual