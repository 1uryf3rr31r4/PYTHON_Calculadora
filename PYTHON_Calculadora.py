import math
from logging import exception

def dividir(num1, num2):
    try:
        return f'{num1/num2}={num1/num2}'
    except ZeroDivisionError:
        return 'O denominador deve ser diferente de zero.'
    except TypeError:
        return 'Insira um valor válido'