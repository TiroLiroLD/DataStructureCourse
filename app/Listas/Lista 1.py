import numpy as np

class Pilha:
    
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__valores = np.empty(capacidade, dtype=str)
        self.__quantidade = 0

    def tamanho_max(self):
        return self.__capacidade

    def tamanho(self):
        return self.__quantidade

    def vazia(self):
        return self.__quantidade == 0

    def cheia(self):
        return self.__quantidade == self.__capacidade
    
    def pop(self):
        if self.vazia():
            return
        
        self.__quantidade -= 1
        return self.__valores[self.__quantidade]
    
    def push(self, valor):
        if self.cheia():
            return

        self.__valores[self.__quantidade] = valor
        self.__quantidade += 1

    def print(self):
        for i in range(self.__quantidade):
            print(self.__valores[i])

    def top(self):
        return self.__valores[self.__quantidade - 1]

    def __add__(self, other):
        self.push(other)

    def igual(self, pilha):
        if self.tamanho() != pilha.tamanho():
            return False
        pilha1 = self
        while not pilha.vazia():
            if pilha1.pop() != pilha.pop():
                return False
        return True

class Lista1:

    def __init__(self):
        self.espelho = 'C'
        self.separador = 'D'

    def define_separador(self, caractere):
            self.separador = caractere

    def define_espelho(self, caractere):
        self.espelho = caractere

    def compara_multiplos_pares(self, string):
        pares = self.separa_pares(string)
        for i in pares:
            if not self.par_espelhado(i):
                return False
        return True

    def separa_pares(self, string):
        par = ""
        pares = []
        for i in string:
            if i == self.separador:
                pares.append(par)
                par = ""
                continue
            par += i
        pares.append(par)
        return pares

        
    def par_espelhado(self, string):
        pilha = self.transforma_pilha(string)
        par_frases = self.separa_frases(pilha)
        par_espelhado = self.espelha_par(par_frases)
        return par_espelhado[0].igual(par_espelhado[1])

    def transforma_pilha(self, string):
        pilha = Pilha(len(string))
        for i in string:
            pilha.push(i)
        return pilha

    def separa_frases(self, pilha):
        if pilha.vazia():
            return
        pilha_frase_1 = Pilha((pilha.tamanho_max()))
        pilha_frase_2 = Pilha((pilha.tamanho_max()))
        while not pilha.vazia():
            #if pilha.vazia():
            #    print("Expressão inválida")
            if pilha.top() == self.espelho:
                pilha.pop()
                break
            pilha_frase_1.push(pilha.pop())
        while not pilha.vazia():
            pilha_frase_2.push(pilha.pop())
        return [pilha_frase_1, pilha_frase_2]

    def espelha_par(self, par):
        frase2 = Pilha(par[1].tamanho_max())
        while not par[1].vazia():
            frase2.push(par[1].pop())
        return [par[0], frase2]



lista1 = Lista1()

print(lista1.par_espelhado("aaaCaaa"))
print(lista1.par_espelhado("aaaCbbb"))
print(lista1.par_espelhado("aaaCaab"))
print(lista1.par_espelhado("aaaCaa"))
print("=====")
print(lista1.compara_multiplos_pares("aCaDbCb"))
print(lista1.compara_multiplos_pares("aCaDbCb"))
print(lista1.compara_multiplos_pares("aCaDbCa"))

pilha = Pilha(5)

pilha.print()

pilha.pop()

pilha.push(5)
pilha.push(3)
pilha.push(2)
pilha.push(9)

pilha.print()

pilha + 2

print(pilha.top())
