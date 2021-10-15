from log import *
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
    
    # Tabela com todos os caracteres reconhecidos pelo console do Windows.
    tabelaCaracteres = {chr(x) : x for x in range(256)}

    def menu(self):
        """
            Função que oferece opçoes para o usuário
        """

        print('Bem vindo ao Sudoku!')
        print('Escolha uma opção:')
        print('1) Novo Jogo')
        print('2) Carregar Jogo ou Salvar jogo atual')
        print('3) Estatísticas do jogo')
        print('4) Sair')


    def jogada(self):
        """
           Faz a jogada do 'jogador', ou seja, insere o valor escolhido na posição 'pos' 
        """
        while True:
            try:
                linha = int(input('Informe a posição da linha (1 a 9)'))
                coluna = int(input('Informe a posição da coluna (1 a 9)'))
                pos = [linha,coluna]
            except ValueError:
                print('Linha ou Coluna Inválida. Tente Novamente!')
                Log().arquivoErros(self,'ValueError')
            except CommandError:
                print('Comando Inválido. Tente Novamente!')
                Log().arquivoErros(self,'CommandError')



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
