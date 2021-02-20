import numpy as np

class Deque:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = 0
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, int)

    def cheio(self):
        return self.numero_elementos == self.capacidade

    def vazio(self):
        return self.numero_elementos == 0

    def insere_inicio(self, valor):
        if self.cheio():
            print("Deque cheio")
            return

        if self.vazio():
            self.valores[self.inicio] = valor
            self.numero_elementos += 1
            return

        self.inicio -= 1
        if self.inicio == - 1:
            self.inicio = self.capacidade - 1
        self.valores[self.inicio] = valor
        self.numero_elementos += 1

    def insere_final(self, valor):
        if self.cheio():
            print("Deque cheio")
            return

        if self.vazio():
            self.valores[self.final] = valor
            self.numero_elemetos += 1
            return

        self.final += 1
        if self.final == self.capacidade:
            self.final = 0
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def remove_inicio(self):
        if self.vazio():
            print("Deque vazio")
            return
        self.inicio += 1
        if self.inicio == self.capacidade:
            self.inicio = 0
        self.numero_elementos -= 1

    def remove_final(self):
        if self.vazio():
            print("Deque vazio")
            return
        self.final -= 1
        if self.final == -1:
            self.final = self.capacidade - 1
        self.numero_elementos -= 1

    def mostra_inicio(self):
        if self.vazio():
            return
        return self.valores[self.inicio]

    def mostra_final(self):
        if self.vazio():
            return
        return self.valores[self.final]


deque = Deque(5)
deque.insere_inicio(1)
deque.insere_inicio(2)
deque.insere_inicio(3)
deque.insere_final(4)
deque.insere_final(5)
print(deque.valores)

print(deque.mostra_inicio())
print(deque.mostra_final())

deque.remove_final()
print(deque.valores)
print(deque.mostra_inicio())
print(deque.mostra_final())

deque.remove_inicio()
print(deque.valores)
print(deque.mostra_inicio())
print(deque.mostra_final())

deque.remove_inicio()
deque.remove_inicio()
deque.remove_inicio()
deque.remove_final()
deque.remove_final()
deque.remove_final()
print(deque.valores)
print(deque.mostra_inicio())
print(deque.mostra_final())
deque.remove_inicio()
deque.remove_inicio()
deque.remove_final()
deque.remove_final()
