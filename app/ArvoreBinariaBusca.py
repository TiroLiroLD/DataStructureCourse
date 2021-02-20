class No:

    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def mostra_no(self):
        print(self.valor)

class ArvoreBinariaBusca:

    def __init__(self):
        self.raiz = None
        self.ligacoes = []

    def inserir(self, valor):
        novo = No(valor)
        if self.raiz == None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                pai = atual
                if valor < atual.valor:
                    atual = atual.esquerda
                    if atual == None:
                        pai.esquerda = novo
                        self.ligacoes.append(str((pai.valor)) + " -> " + str(novo.valor))
                        return
                else:
                    atual = atual.direita
                    if atual == None:
                        pai.direita = novo
                        self.ligacoes.append(str((pai.valor)) + " -> " + str(novo.valor))
                        return

arvore = ArvoreBinariaBusca()

insere = [53, 30, 14, 39, 9, 23, 34, 49, 72, 61, 84, 79]
for i in insere:
    arvore.inserir(i)

print(arvore.raiz.valor)
print(arvore.raiz.esquerda.valor)
print(arvore.raiz.direita.valor)
