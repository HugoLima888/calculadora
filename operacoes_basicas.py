# Operações realizadas pela calculadora #

class Operacoes:
    def __init__(self):
        self.seleciona_opcao()

    def __int__(self):
        pass

    def seleciona_opcao(self):
        self.opcao = int(input('Escolha uma das opções disponíveis 1 - Soma, 2: Subtração,'
                               '3: Multiplicação, 4: Divisão - : '))
        self.operacao = self.opcao
        if self.operacao == 1:
            self.soma()
        elif self.operacao == 2:
            self.subt()
        elif self.operacao == 3:
            self.multi()
        elif self.operacao == 4:
            self.divi()
        else:
            raise ValueError('Operação inválida!!')

    def soma(self):
        n1 = int(input('Informe um valor: '))
        n2 = int(input('Informe um valor: '))
        resultado = n1 + n2
        print(f'A subtração dos valores é: {resultado}')

    def subt(self):
        n1 = int(input('Informe um valor: '))
        n2 = int(input('Informe um valor: '))
        resultado = n1 - n2
        print(f'A subtração dos valores é: {resultado}')

    def multi(self):
        n1 = int(input('Informe um valor: '))
        n2 = int(input('Informe um valor: '))
        resultado = n1 * n2
        print(f'A multiplicação dos valores é: {resultado}')

    def divi(self):
        n1 = int(input('Informe um valor: '))
        n2 = int(input('Informe um valor: '))
        resultado = n1 / n2
        print(f'A multiplicação dos valores é: {round(resultado, 2)}')