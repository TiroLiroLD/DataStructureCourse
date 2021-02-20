import numpy as np

class FilaDePrioridade:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=object)

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, adjacente):
        if self.__fila_cheia():
            print(f"Lista cheia, não foi possível adicionar {adjacente}")
            return

        if self.__fila_vazia():
            self.valores[self.numero_elementos] = adjacente
            self.numero_elementos += 1
        else:
            posicao = self.numero_elementos - 1
            while posicao >= 0:
                if adjacente.distancia_objetivo > self.valores[posicao].distancia_objetivo:
                    self.valores[posicao + 1] = self.valores[posicao]
                else:
                    break
                posicao -= 1
            self.valores[posicao + 1] = adjacente
            self.numero_elementos += 1


    def desenfileirar(self):
        if self.__fila_vazia():
            print("A fila está vazia")
            return

        valor = self.valores[self.numero_elementos - 1]
        self.numero_elementos -= 1
        return valor

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.numero_elementos - 1]
