import numpy as np

class VetorNaoOrdenado:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = np.empty(self.capacidade, int)

  def imprime(self):
    if self.ultima_posicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, ' - ', self.valores[i])

  def insere(self, valor):
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
    else:
      self.ultima_posicao += 1
      self.valores[self.ultima_posicao] = valor

  def pesquisar(self, valor):
    for i in range(self.ultima_posicao + 1):
      if valor == self.valores[i]:
        return i 
    return -1

  def excluir(self, valor):
    posicao = self.pesquisar(valor)
    if posicao == -1:
      return -1
    else:
      for i in range(posicao, self.ultima_posicao):
        self.valores[i] = self.valores[i+1]
        self.ultima_posicao -= 1


class VetorOrdenado:

  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = np.empty(self.capacidade, dtype=int)

  def imprime(self):
    if self.ultima_posicao == -1:
      print('Lista vazia')
    for i in range(self.ultima_posicao + 1):
      print(f'{i}: {self.valores[i]}')

  def insere(self, valor):
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
      return -1

    posicao = 0
    for i in range(self.ultima_posicao + 1):
      posicao = i
      if self.valores[i] == valor:
        print('Valor já existente')
        return -1
      if self.valores[i] > valor:
        break
      if i == self.ultima_posicao:
        posicao += 1

    aux = self.ultima_posicao
    while aux >= posicao:
      self.valores[aux + 1] = self.valores[aux]
      aux -= 1

    self.ultima_posicao += 1
    self.valores[posicao] = valor

  def pesquisar(self, valor):
    for i in range(self.ultima_posicao + 1):
      if valor < self.valores[i]:
        return -1
      if valor == self.valores[i]:
        return i
    return -1

  def excluir(self, valor):
    posicao = self.pesquisar(valor)
    if posicao == -1:
      return -1
    for i in range(posicao, self.ultima_posicao):
      self.valores[i] = self.valores[i + 1]

    self.ultima_posicao -= 1
    
  def buscaBinaria(self, valor):
    inicio = 0
    fim = self.ultima_posicao + 1
    while inicio <= fim:
      meio = round((inicio + fim)/2)
      if self.valores[meio] == valor:
        return meio
      if self.valores[meio] < valor:
        inicio = meio + 1
      else:
        fim = meio - 1
    return -1

'''vetorOrdenado = VetorOrdenado(6)
vetorOrdenado.insere(1)
vetorOrdenado.insere(3)
vetorOrdenado.insere(4)
vetorOrdenado.insere(5)

vetorOrdenado.imprime()
print('---')

vetorOrdenado.insere(6)
vetorOrdenado.insere(8)

vetorOrdenado.imprime()
print('---')

vetorOrdenado.excluir(6)
vetorOrdenado.imprime()
print('---')

vetorOrdenado.excluir(1)
vetorOrdenado.excluir(8)
vetorOrdenado.imprime()
print('---')'''

vetorOrdenado = VetorOrdenado(20)
vetorOrdenado.insere(1)
vetorOrdenado.insere(2)
vetorOrdenado.insere(3)
vetorOrdenado.insere(4)
vetorOrdenado.insere(5)
vetorOrdenado.insere(6)
vetorOrdenado.insere(7)
vetorOrdenado.insere(8)
vetorOrdenado.insere(9)
vetorOrdenado.insere(10)
vetorOrdenado.insere(11)
vetorOrdenado.insere(12)
vetorOrdenado.insere(13)
vetorOrdenado.insere(14)
vetorOrdenado.insere(15)
vetorOrdenado.insere(16)
vetorOrdenado.insere(17)
vetorOrdenado.insere(18)
vetorOrdenado.insere(19)
vetorOrdenado.insere(20)

print (vetorOrdenado.valores)
print(vetorOrdenado.buscaBinaria(8))
print(vetorOrdenado.buscaBinaria(3))
print(vetorOrdenado.buscaBinaria(19))
