# Operações realizadas pela calculadora #


def soma():
    n1 = int(input('Informe um valor: '))
    n2 = int(input('Informe um valor: '))
    resultado = n1 + n2
    print(f'A soma dos valores é: {resultado}')


def subt():
    n1 = int(input('Informe um valor: '))
    n2 = int(input('Informe um valor: '))
    resultado = n1 - n2
    print(f'A subtração dos valores é: {resultado}')


def multi():
    n1 = int(input('Informe um valor: '))
    n2 = int(input('Informe um valor: '))
    resultado = n1 * n2
    print(f'A multiplicação dos valores é: {resultado}')


def divi():
    n1 = int(input('Informe um valor: '))
    n2 = int(input('Informe um valor: '))
    resultado = n1 / n2
    print(f'A multiplicação dos valores é: {round(resultado, 2)}')