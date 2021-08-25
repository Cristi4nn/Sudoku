from interfaceUsuario import *

class Tela(InterfaceUsuario):
    """
        Esta classe representa a tela que é mostrada ao usuário. Todas as possíveis telas
        usadas são objetos da classe Tela ou de subclasses dela.
    """
    __atributos  = {'titulo', 'opcoes'}
    __metodos    = {'__init__','__str__','desenhaTela','getOpcaoEscolhida','getManual','getAtributos','getMetodos'}
    
    def __init__(self, titulo, opcoes):
        """
            Método construtor. Recebe o título da tela e as opções a serem mostradas na
            tela.
            
            (str,list) -> Tela
        """
        self.titulo = titulo    # Representa o título da tela
        self.opcoes = opcoes    # Representa a lista de opções do usuário
    
    def __str__(self):
        """
            Método de representação em String.
            
            (Tela) -> str
        """
        return None
    
    def desenhaTela(self):
        """
            Esta função atualiza a tela no console após ocorrer alguma modificação, 
            limpando a tela e em seguida printando sua versão em string.
            
            (Tela) -> None
        """
        InterfaceUsuario.limpaTela()
        print(self)
    
    def getOpcaoEscolhida(self):
        """
            Esta função lê a opção escolhida pelo usuário a partir do console e retorna
            a escolha.
            
            (Tela) -> int
        """
        
        return -1
    
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
            Esta função estática (chamada sempre através de Tela.getManual()) retorna um 
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            
            (None) -> dict
        """
        manual = dict()
        manual['__init__']              = Tela.__init__.__doc__
        manual['__str__']               = Tela.__str__.__doc__
        manual['desenhaTela']           = Tela.desenhaTela.__doc__
        manual['getOpcaoEscolhida']     = Tela.desenhaTela.__doc__
        manual['getManual']             = Tela.getManual.__doc__
        manual['getAtributos']          = Tela.getAtributos.__doc__
        manual['getMetodos']            = Tela.getMetodos.__doc__
        manual['titulo']                = '# Representa o título da tela'
        manual['opcoes']                = '# Representa a lista de opções do usuário'
        return manual

def main():
    manual = Tela.getManual()
    for key in manual:
        print(key, " : ", manual[key])

if __name__=='__main__':
    main()
