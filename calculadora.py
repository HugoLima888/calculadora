from operacoes_basicas import soma, subt, multi, divi


class Calculadora:
    def __init__(self):
        self.opcao = int(input('Selecione uma das opções disponíveis 1 - Soma, 2: Subtração,'
                               '3: Multiplicação, 4: Divisão - : '))
        self.operacao = self.opcao
        if self.operacao == 1:
            soma()
        elif self.operacao == 2:
            subt()
        elif self.operacao == 3:
            multi()
        elif self.operacao == 4:
            divi()
        else:
            raise ValueError('Operação inválida!!')