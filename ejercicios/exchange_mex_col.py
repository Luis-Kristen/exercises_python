# -*- coding: utf-8 -*-

def foreign_exchange_calculator(amount):
    mex_to_col_rate = 166.69
    return mex_to_col_rate * amount


def run():
    print('C A L C U L A T O R  O F   E X C H A N G E S')
    print('Convierte pesos mexicanos a pesos colombianos')
    print('')

    amount = float(raw_input('Ingresa la cantidad de pesos mexicanos que quieres convertir: '))
        #raw_input lee un valor que nosotros le demos
    result = foreign_exchange_calculator(amount)

    print('${} pesos mexicanos son ${} pesos colombianos'.format(amount, result))
    print('')

if __name__ == '__main__':
    run()