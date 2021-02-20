import numpy as np


class FilaCircular:

    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__inicio = 0
        self.__final = -1
        self.__numero_elementos = 0
        self.__valores = np.empty(capacidade, dtype=int)

    def __fila_vazia(self):
        return self.__numero_elementos == 0

    def __fila_cheia(self):
        return self.__numero_elementos == self.__capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print("A fila está cheia")
            return

        if self.__final == self.__capacidade - 1:
            self.__final = -1
        self.__final += 1
        self.__valores[self.__final] = valor
        self.__numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('A fila já está vazia')
            return

        temp = self.__valores[self.__inicio]
        self.__inicio += 1
        if self.__inicio == self.__capacidade:
            self.__inicio == 0
        self.__numero_elementos -= 1
        return temp

    def primeiro(self):
        if self.__fila_vazia():
            print(-1)
            return -1
        print(self.__valores[self.__inicio])
        return self.__valores[self.__inicio]

fila = FilaCircular(5)

fila.primeiro()
print("----")

fila.enfileirar(1)
fila.primeiro()
print("----")

fila.enfileirar(2)

print("----")
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)
fila.primeiro()

print("----")
fila.enfileirar(6)

print("----")
fila.desenfileirar()
fila.desenfileirar()
fila.primeiro()
print("----")

fila.enfileirar(6)
fila.enfileirar(7)
fila.primeiro()
