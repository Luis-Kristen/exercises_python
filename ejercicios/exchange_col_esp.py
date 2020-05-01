# -*- coding: utf-8 -*-

def foreign_exchange_calculator(amount):
    col_to_col_rate = 0.00023
    return col_to_col_rate * amount


def run():
    print('C A L C U L A T O R  O F   E X C H A N G E S')
    print('Convierte pesos colombianos a Euros')
    print('')

    amount = float(raw_input('Ingresa la cantidad de pesos Colombianos que quieres convertir: '))
        #raw_input lee un valor que nosotros le demos
    result = foreign_exchange_calculator(amount)

    print('${} Pesos Colombianos, son ${} Euros'.format(amount, result))
    print('')

if __name__ == '__main__':
    run()