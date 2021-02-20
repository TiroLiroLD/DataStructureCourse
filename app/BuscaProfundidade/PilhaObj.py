import numpy as np

class PilhaObj:

    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(capacidade, dtype=object)

    def __pilha_cheia(self):
        if self.__topo == self.__capacidade - 1:
            return True
        return False

    def vazia(self):
        if self.__topo == -1:
            return True
        return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print(f'Pilha cheia, não foi possível adicionar o valor {valor}')
            return
        self.__topo += 1
        self.__valores[self.__topo] = valor

    def desempilhar(self):
        if self.vazia():
            return -1
        removido = self.__valores[self.__topo]
        self.__topo -= 1
        return removido

    def topo(self):
        if self.vazia():
            return -1
        topo = self.__valores[self.__topo]
        return topo