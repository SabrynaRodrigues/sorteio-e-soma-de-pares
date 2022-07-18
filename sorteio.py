# SORTEIO
from random import randint


def sorteio(list):
    print('The numbers drawn are:')
    for c in range(0,5):
        list.append(randint(1,10))


# SOMAR
def somar(list):
    soma = 0
    for n in list:
        if n % 2 == 0:
            soma += n
    print(f'By summing the even values of the list:{list}, we get the value {soma}.')



# PROGRAMA PRINCIPAL
numbers = list()
sorteio(numbers)
print(numbers)
print('-✦' * 7)
somar(numbers)