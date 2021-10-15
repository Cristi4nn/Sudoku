import matplotlib.pyplot as plt
import numpy as np
from log import *
from jogador import *


class Estatistica:
    __atributos  = {}
    __metodos    = {'__init__','__str__','estatisticaTempo','estatisticaPartidas','estatisticaJogosCompletados','estatisticaAcertos','estatisticaErros','getManual','getAtributos','getMetodos'}
    def __init__(self):
        """
            Metodo construtor
        """
        self.arquivoJog = Jogador().nick + '_jogadas.txt'
        self.arquivoErro = Jogador().nick + '_erros.txt'
    
    def __str__(self):
        """
            Este método, usado para representação em string, será retornada a String que contém as descrições de todos os métodos e 
            atributos das classes.
            
        """
        pass

    def estatisticaTempo(self):
        """
            Função que faz um array do tempo de cada jogo; None -> array
        """
        try:
            lista = []
            arq = open(self.arquivoJog)
            arquivoLido = arq.read()
            for i in arquivoLido:
                if 'Tempo' in i:
                    lista.append(i[6:])
            array = np.array(lista)
            return array
        except FileNotFoundError:
            Log().arquivoJogadas('')

        

    def estatisticaPartidas(self):
        """
        Função que faz um array da quantidade de partidas; None -> array
        """
        try:
            lista = []
            arq = open(self.arquivoJog)
            arquivoLido = arq.read()
            for i in arquivoLido:
                if 'Partida' in i:
                    lista.append(i[7:])
            array = np.array(lista)
            arq.close()
            return array
        except FileNotFoundError:
            Log().arquivoJogadas('')



    def estatisticaJogosCompletados(self):
        """
            Função que faz um array da quantidade de jogos completados;  None -> array
        """
        try:
            lista = []
            arq = open(self.arquivoJog)
            arquivoLido = arq.read()
            for i in arquivoLido:
                if 'jogoCompletado' in i:
                    lista.append(i[14:])
            array = np.array(lista)
            arq.close()
            return array
        except FileNotFoundError:
            Log().arquivoJogadas('')


    def estatisticaAcertos(self):
        """
            Função que faz um array da quantidade de acertos por jogo; None -> array
        """
        try:
            lista = []
            arq = open(self.arquivoJog)
            arquivoLido = arq.read()
            for i in arquivoLido:
                if 'Acertos/Jogo' in i:
                    lista.append(i[11:])
            array = np.array(lista)
            arq.close()
            return array
        except FileNotFoundError:
            Log().arquivoJogadas('')


    def estatisticaErros(self):
        """
            Função que faz um array dos erros ; None -> array
        """
        try:
            lista = []
            arq = open(self.arquivoErro)
            arquivoLido = arq.read()
            array = np.array(len(arquivoLido))
            arq.close()
            return array
        except FileNotFoundError:
            Log().arquivoJogadas('')

    def getAtributos():
        """
            Esta função estática (chamada sempre através de Estatistica.getAtributos()) retorna um 
            conjunto com os nomes dos atributos desta classe.
            
            (None) -> set
        """
        return __atributos
    
    def getMetodos():
        """
            Esta função estática (chamada sempre através de Estatistica.getMetodos()) retorna um 
            conjunto com os nomes dos métodos desta classe.
            
            (None) -> set
        """
        return __metodos

    def getManual():
        """
            Esta função estática (chamada sempre através de Estatistica.getManual()) retorna um 
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            
            (None) -> dict
        """
        manual = dict()
        manual['__init__']              = Estatistica.__init__.__doc__
        manual['__str__']               = Estatistica.__str__.__doc__
        manual['estatisticaTempo']     = Estatistica.estatisticaTempo.__doc__
        manual['estatisticaJogosCompletados']           = Estatistica.estatisticaJogosCompletados.__doc__
        manual['estatisticaPartidas']           = Estatistica.estatisticaPartidas.__doc__
        manual['estatisticaAcertos']     = Estatistica.estatisticaAcertos.__doc__
        manual['estatisticaErros']     = Estatistica.estatisticaErros.__doc__
        manual['getManual']          = Estatistica.getManual.__doc__
        manual['getAtributos']         = Estatistica.getAtributos.__doc__
        manual['getMetodos']            = Estatistica.getMetodos.__doc__
        return manual


class Graficos(Estatistica):
    __atributos  = {}
    __metodos    = {'__init__','__str__','criadorDeGrafico','getManual','getAtributos','getMetodos'}
    def __init__(self):
        """
            Metodo construtor
        """
    def __str__(self):
        """
        """
        pass

    def criadorDeGrafico(self):
        try:
            dicionario = {'Tempo':Estatistica().estatisticaTempo(),'Partida':Estatistica().estatisticaPartidas(),'JogosCompletos':Estatistica().estatisticaJogosCompletados(),'Acertos':Estatistica().estatisticaAcertos(),'Erros':Estatistica().estatisticaErros()}
            escolha = input(f'Escolha o grafico dentre as opções {dicionario.keys()}.  ex: Tempo x Acertos :\n')
            opcao = escolha.split(' x ')
            fig, ax = plt.subplots()
            x = dicionario[opcao[0]]
            y = dicionario[opcao[1]]
            plt.bar(x,y,color='blue')
            plt.plot(x,y)
            plt.show()
            plt.savefig(escolha)
        except KeyError:
            print('Tente Novamente!')
    
    def getAtributos():
        """
            Esta função estática (chamada sempre através de Graficos.getAtributos()) retorna um 
            conjunto com os nomes dos atributos desta classe.
            
            (None) -> set
        """
        return __atributos
    
    def getMetodos():
        """
            Esta função estática (chamada sempre através de Graficos.getMetodos()) retorna um 
            conjunto com os nomes dos métodos desta classe.
            
            (None) -> set
        """
        return __metodos

    def getManual():
        """
            Esta função estática (chamada sempre através de Estatistica.getManual()) retorna um 
            dicionário que mapeia os nomes dos atributos e métodos às suas descrições.
            
            (None) -> dict
        """
        manual = dict()
        manual['__init__']              = Graficos.__init__.__doc__
        manual['__str__']               = Graficos.__str__.__doc__
        manual['criadorDeGrafico']     = Graficos.criadorDeGrafico.__doc__
        manual['getManual']          = Graficos.getManual.__doc__
        manual['getAtributos']         = Graficos.getAtributos.__doc__
        manual['getMetodos']            = Graficos.getMetodos.__doc__
        return manual

