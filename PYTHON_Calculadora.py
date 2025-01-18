import math
from logging import exception

def menu_principal():
    print('Calculadora'.center(65,'='))
    opcoes()
    print('='*65)

def dividir(num1, num2):
    try:
        return f'{num1/num2}={num1/num2}'
    except ZeroDivisionError:
        return 'O denominador deve ser diferente de zero.'
    except TypeError:
        return 'Insira um valor válido'