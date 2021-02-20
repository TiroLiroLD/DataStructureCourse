import numpy as np

class No():
    def __init__(self, valor):
        self.valor = valor
        self.next = None

    def set_next(self, next):
        self.next = next

    def mostra_no(self):
        print(self.valor)


class ListaEncadeada():
    def __init__(self):
        self.primeiro = None
        self.numero_elementos = 0

    def insere_inicio(self, valor):
        novo = No(valor)
        novo.next = self.primeiro
        self.primeiro = novo

    def mostrar(self):
        atual = self.primeiro
        while atual is not None:
            atual.mostra_no()
            atual = atual.next

    def excluir_inicio(self):
        temp = self.primeiro
        if self.primeiro is not None:
            self.primeiro = self.primeiro.next
        return self.primeiro

lista = ListaEncadeada()

lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista.mostrar()

lista.excluir_inicio()
lista.excluir_inicio()
lista.excluir_inicio()
lista.excluir_inicio()
lista.excluir_inicio()
lista.excluir_inicio()
lista.mostrar()