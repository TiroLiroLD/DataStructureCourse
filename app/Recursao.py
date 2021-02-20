def soma(n):
    if n == 0:
        return 0
    return n + soma(n-1)

def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n-1)

def potencia(a, b):
    if b == 1:
        return a
    return a * potencia(a, b-1)

print(fatorial(5))

print(potencia(2,80))