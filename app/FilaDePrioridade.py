import numpy as np

class FilaDePrioridade:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print(f"Lista cheia, não foi possível adicionar {valor}")
            return

        if self.__fila_vazia():
            self.valores[self.numero_elementos] = valor
            self.numero_elementos += 1
        else:
            posicao = self.numero_elementos - 1
            while posicao >= 0:
                if valor > self.valores[posicao]:
                    self.valores[posicao + 1] = self.valores[posicao]
                else:
                    break
                posicao -= 1
            self.valores[posicao + 1] = valor
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

fila = FilaDePrioridade(5)

fila.enfileirar(10)
fila.enfileirar(50)
fila.enfileirar(30)
fila.enfileirar(40)
fila.enfileirar(20)

print(fila.primeiro())

print(fila.valores)