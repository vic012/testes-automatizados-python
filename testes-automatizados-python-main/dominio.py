import sys

class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []

    @property
    def lances(self):
        return self.__lances

class Avaliador:

    def __init__(self):
        #Pega as informações dos floats do sistema operacional (Menor)
        self.maior_lance = sys.float_info.min
        #Pega as informações dos floats do sistema operacional (Maior)
        self.menor_lance = sys.float_info.max

    #Na linha Estou especificando na classe o parâmetro que ele deve receber
    def avalia(self, leilao: 'É esperado itens da classe Leilao'):
        for lance in leilao.lances:
            if (lance.valor > self.maior_lance):
                self.maior_lance = lance.valor
            elif (lance.valor < self.menor_lance):
                self.menor_lance = lance.valor
