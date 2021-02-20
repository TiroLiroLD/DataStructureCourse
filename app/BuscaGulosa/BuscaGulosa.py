class Vertice():
    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo
        self.visitado = False
        self.adjacentes = []
        self.distancia_objetivo = distancia_objetivo

    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)
    
    def mostra_adjacentes(self):
        for adjacente in self.adjacentes:
            if adjacente.custo is not None:
                print(adjacente.vertice.rotulo + ": " + adjacente.custo)
            else:
                print(adjacente.vertice.rotulo)
        
class Adjacente():
    def __init__(self, vertice, custo = None):
        self.vertice = vertice
        self.custo = custo

class Grafo():
    arad = Vertice('Arad', 366)
    zerind = Vertice('Zerind', 374)
    oradea = Vertice('Oradea', 380)
    sibiu = Vertice('Sibiu', 253)
    timisoara = Vertice('Timisoara', 329)
    lugoj = Vertice('Lugoj', 244)
    mehadia = Vertice('Mehadia', 241)
    dobreta = Vertice('Dobreta', 242)
    craiova = Vertice('Craiova', 160)
    rimnicu = Vertice('Rimnicu', 193)
    fagaras = Vertice('Fagaras', 178)
    pitesti = Vertice('Pitesti', 98)
    bucharest = Vertice('Bucharest', 0)
    giurgiu = Vertice('Giurgiu', 77)

    arad.adiciona_adjacente(Adjacente(zerind, 75))
    arad.adiciona_adjacente(Adjacente(sibiu, 140))
    arad.adiciona_adjacente(Adjacente(timisoara, 118))

    zerind.adiciona_adjacente(Adjacente(arad, 75))
    zerind.adiciona_adjacente(Adjacente(oradea, 71))

    oradea.adiciona_adjacente(Adjacente(zerind, 71))
    oradea.adiciona_adjacente(Adjacente(sibiu, 151))

    sibiu.adiciona_adjacente(Adjacente(oradea, 151))
    sibiu.adiciona_adjacente(Adjacente(arad, 140))
    sibiu.adiciona_adjacente(Adjacente(fagaras, 99))
    sibiu.adiciona_adjacente(Adjacente(rimnicu, 80))

    timisoara.adiciona_adjacente(Adjacente(arad, 118))
    timisoara.adiciona_adjacente(Adjacente(lugoj, 111))

    lugoj.adiciona_adjacente(Adjacente(timisoara, 111))
    lugoj.adiciona_adjacente(Adjacente(mehadia, 70))

    mehadia.adiciona_adjacente(Adjacente(lugoj, 70))
    mehadia.adiciona_adjacente(Adjacente(dobreta, 75))

    dobreta.adiciona_adjacente(Adjacente(mehadia, 75))
    dobreta.adiciona_adjacente(Adjacente(craiova, 120))

    craiova.adiciona_adjacente(Adjacente(dobreta, 120))
    craiova.adiciona_adjacente(Adjacente(pitesti, 138))
    craiova.adiciona_adjacente(Adjacente(rimnicu, 146))

    rimnicu.adiciona_adjacente(Adjacente(craiova, 146))
    rimnicu.adiciona_adjacente(Adjacente(sibiu, 80))
    rimnicu.adiciona_adjacente(Adjacente(pitesti, 97))

    fagaras.adiciona_adjacente(Adjacente(sibiu, 99))
    fagaras.adiciona_adjacente(Adjacente(bucharest, 211))

    pitesti.adiciona_adjacente(Adjacente(rimnicu, 97))
    pitesti.adiciona_adjacente(Adjacente(craiova, 138))
    pitesti.adiciona_adjacente(Adjacente(bucharest, 101))

    bucharest.adiciona_adjacente(Adjacente(fagaras, 211))
    bucharest.adiciona_adjacente(Adjacente(pitesti, 101))
    bucharest.adiciona_adjacente(Adjacente(giurgiu, 90))

    """

class Orion:
    bellatrix = Vertice("Bellatrix")
    mintaka = Vertice("Mintaka")
    rigel = Vertice("Rigel")
    saiph = Vertice("Saiph")
    alnitak = Vertice("Alnitak")
    alnilam = Vertice("Alnilam")
    betelgeuse = Vertice("Betelgeuse")
    meissa = Vertice("Meissa")

    bellatrix.adiciona_adjacente(Adjacente(mintaka))
    bellatrix.adiciona_adjacente(Adjacente(betelgeuse))
    bellatrix.adiciona_adjacente(Adjacente(meissa))

    mintaka.adiciona_adjacente(Adjacente(bellatrix))
    mintaka.adiciona_adjacente(Adjacente(alnilam))
    mintaka.adiciona_adjacente(Adjacente(rigel))

    rigel.adiciona_adjacente(Adjacente(mintaka))
    rigel.adiciona_adjacente(Adjacente(saiph))

    saiph.adiciona_adjacente(Adjacente(rigel))
    saiph.adiciona_adjacente(Adjacente(alnitak))

    alnitak.adiciona_adjacente(Adjacente(saiph))
    alnitak.adiciona_adjacente(Adjacente(alnilam))
    alnitak.adiciona_adjacente(Adjacente(betelgeuse))

    alnilam.adiciona_adjacente(Adjacente(alnitak))
    alnilam.adiciona_adjacente(Adjacente(mintaka))

    betelgeuse.adiciona_adjacente(Adjacente(alnitak))
    betelgeuse.adiciona_adjacente(Adjacente(bellatrix))
    betelgeuse.adiciona_adjacente(Adjacente(meissa))

    meissa.adiciona_adjacente(Adjacente(betelgeuse))
    meissa.adiciona_adjacente(Adjacente(bellatrix))

    betelgeuse.mostra_adjacentes()"""

import numpy as np
from FilaOrdenadaObj import FilaDePrioridade

class BuscaProfundidade:
    def __init__(self, inicio):
        self.inicio = inicio
        self.inicio.visitado = True
        self.fila = FilaDePrioridade(20)
        self.fila.enfileirar(inicio)
        self.passos = 1
        self.found = False

    '''def busca(self, no_busca):
        topo = self.pilha.topo()
        if topo == no_busca:
            print(self.passos)
            return
        for adjacente in topo.adjacentes:
            if not adjacente.vertice.visitado:
                self.passos += 1
                self.pilha.empilhar(adjacente.vertice)
                adjacente.vertice.visitado = True
                self.busca(no_busca)
        self.pilha.desempilhar()    '''
    

    def busca2(self, no_busca):
        topo = self.fila.primeiro()
        print(f'Topo:{topo.rotulo}')
        if self.found:
            return
        if topo == no_busca:
            print(self.passos)
            self.found = True
            return
        for adjacente in topo.adjacentes:
            if self.found:
                return
            print(f'Topo:{topo.rotulo}\n{adjacente.vertice.rotulo} já foi visitada? {adjacente.vertice.visitado}')
            if not adjacente.vertice.visitado:
                self.passos += 1
                self.fila.enfileirar(adjacente.vertice)
                adjacente.vertice.visitado = True
                print(f'Empilha {adjacente.vertice.rotulo}')
                self.busca2(no_busca)
        print(f'Desempilha {self.fila.desenfileirar().rotulo}\n')

grafo = Grafo()

busca = BuscaProfundidade(grafo.arad)

busca.busca2(grafo.bucharest)