from operacoes_basicas import Operacoes


class Calculadora:
    def __init__(self):
        print('''
        ****************************************************************
        ************************** BEM VINDO! **************************
        ****************************************************************
        ''')
        Operacoes()
        self.usar_novamente()

    def usar_novamente(self):
        calcular_novamente = input('Você gostaria de utilizar a calculadora novamente? (S/N)')
        if calcular_novamente.upper() == 'S':
            Calculadora()
        elif calcular_novamente.upper() == 'N':
            print('Volte sempre! =)')
        else:
            self.usar_novamente()
