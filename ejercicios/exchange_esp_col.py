# -*- coding: utf-8 -*-

def foreign_exchange_calculator(amount):
    esp_to_col_rate = 4418.40
    return esp_to_col_rate * amount


def run():
    print('C A L C U L A T O R  O F   E X C H A N G E S')
    print('Convierte euros a pesos colombianos')
    print('')

    amount = float(raw_input('Ingresa la cantidad de Euros que quieres convertir: '))
        #raw_input lee un valor que nosotros le demos
    result = foreign_exchange_calculator(amount)

    print('${} Euros, son ${} pesos colombianos'.format(amount, result))
    print('')

if __name__ == '__main__':
    run()