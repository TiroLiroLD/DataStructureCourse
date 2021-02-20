import numpy as np


class Pilha:

    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.chararray(capacidade, unicode=True)

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
        self.__topo += 1
        self.__valores[self.__topo] = valor

    def desempilhar(self):
        if self.vazia():
            print('A pilha está vazia, não há o que remover')
            return -1
        removido = self.__valores[self.__topo]
        print(f'{removido} foi removido do topo da Pilha')
        self.__topo -= 1
        return removido

    def ver_topo(self):
        if self.vazia():
            return -1
        topo = self.__valores[self.__topo]
        print(f'{topo} está no topo da Pilha')
        return topo

    def topo(self):
        if self.vazia():
            return -1
        topo = self.__valores[self.__topo]
        return topo

def confere_expressao(expressao):
    agrupadores = {"{": "}",
                   "[": "]",
                   "(": ")",
                   "<": ">"}
    pilhaExpressao = Pilha(len(expressao))
    pilhaAgrupadores = Pilha(len(expressao))
    for i in expressao:
        pilhaExpressao.empilhar(i)
    while not pilhaExpressao.vazia():
        if pilhaExpressao.topo() in agrupadores.values():
            pilhaAgrupadores.empilhar(pilhaExpressao.desempilhar())
        elif pilhaExpressao.topo() in agrupadores.keys():
            if pilhaAgrupadores.topo() == agrupadores.get(pilhaExpressao.desempilhar()):
                pilhaAgrupadores.desempilhar()
            else:
                print('Expressão inválida')
                return False
        else:
            pilhaExpressao.desempilhar()
    if not pilhaAgrupadores.vazia():
        print("Expressão inválida")
        return False
    print("Expressão válida")
    return True


pilha = Pilha(5)

pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4)
pilha.empilhar(5)

pilha.ver_topo()

confere_expressao("{abc()}<{}ddddd>")
