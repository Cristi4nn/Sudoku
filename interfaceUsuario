import os

class InterfaceUsuario:
    """
        Super classe que inclui todos os métodos e atributos que são úteis para qualquer interação                          
        que pode ser feita com o usuário.
    """
    __atributos  = {}
    __metodos    = {'__init__','__str__','pause','salva','novoJogo','limpaTela','getManual','getAtributos','getMetodos'}


    def __init__(self):
        """
            Metodo construtor.
        """
        pass

    def __str__(self):
        """
            Este método, usado para representação em string, será retornada a String que contém as descrições de todos os métodos e 
            atributos das classes.
            
        """
        saida = ""
        
        manualTela = InterfaceUsuario.getManual()
        
        saida += 'MANUAL DA CLASSE TELA\n'
        
        for chave in manualTela:
            saida += f'{chave} : {manualTela[chave]}\n'
        saida +='\n'
        
        return saida
    
    # Tabela com todos os caracteres reconhecidos pelo console do Windows.
    tabelaCaracteres = {chr(x) : x for x in range(256)}


    def pause():
        """
        Função que pausa o jogo
        """
    
    def salvar():
        """
        Função que salva os dados do jogo até o momento
        """
        pass

    def novoJogo():
        """
        Função que cria um novo jogo
        """
        pass

    def limpaTela():
        """
            Função que limpa toda a tela.
        """
        os.system('cls')

    def getAtributos():
        """
            Esta função estática (chamada sempre através de InterfaceUsuario.getAtributos()) retorna um 
            conjunto com os nomes dos atributos desta classe.
            
            (None) -> set
        """
        return __atributos
    
    def getMetodos():
        """
            Esta função estática (chamada sempre através de InterfaceUsuario.getMetodos()) retorna um 
            conjunto com os nomes dos métodos desta classe.
            
            (None) -> set
        """
        return __metodos

    def getManual():
        """
            Esta função estática (chamada sempre através de InterfaceUsuario.getManual()) retorna um 
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            
            (None) -> dict
        """
        manual = dict()
        manual['__init__']              = InterfaceUsuario.__init__.__doc__
        manual['__str__']               = InterfaceUsuario.__str__.__doc__
        manual['pause']           = InterfaceUsuario.pause.__doc__
        manual['salvar']     = InterfaceUsuario.salvar.__doc__
        manual['novoJogo']             = InterfaceUsuario.novoJogo.__doc__
        manual['limpaTela']            =InterfaceUsuario.limpaTela.__doc__
        manual['getManual']          = InterfaceUsuario.getManual.__doc__
        manual['getAtributos']         = InterfaceUsuario.getAtributos.__doc__
        manual['getMetodos']            = InterfaceUsuario.getMetodos.__doc__
        return manual
