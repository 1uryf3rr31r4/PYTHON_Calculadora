import math
from logging import exception

def menu_principal():
    print('Calculadora'.center(65,'='))
    opcoes()
    print('='*65)

def opcoes():
    print('1 - Opções Aritiméticas')
    print('2 - Funções Logarítimitcas e Potência')
    print('3 - Funções Trigonométricas')
    print('4 - Outras Opções')
    print('5 - Sair')

def opcoes_1():
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Voltar')

def opceos_2():
    print('1 - Quadrado')
    print('2 - Cubo')
    print('3 - Potência')
    print('4 - Log10')
    print('5 - Log')
    print('6 - Voltar')

def opcoes_3():
    print('1 - Seno')
    print('2 - Cosseno')
    print('3 - Tangente')
    print('4 - Voltar')

def opcoes_4():
    print('1 - Fatorial')
    print('2 - Voltar')


def dividir(num1, num2):
    try:
        return f'{num1} / {num2} = {num1/num2}'
    except ZeroDivisionError:
        return 'O denominador deve ser diferente de zero.'
    except TypeError:
        return 'Insira um valor válido'

def menu_1():
    opcao=0
    while opcao!=5:
        opcao=int(input('>> '))
        if opcao in range(1,5):
            num1=float(input('Numero 1: '))
            num2=float(input('Numero 2: '))
            if opcao==1:
                print(f'{num1} + {num2} = {num1+num2}')
            elif opcao==2:
                print(f'{num1} - {num2} = {num1-num2}')
            elif opcao==3:
                print(f'{num1} x {num2} = {num1*num2}')
            else:
                print(dividir(num1, num2))
        else:
            if opcao!=5:
                print('Opção Inválida')

def main():
    escolha=''
    while escolha!=5:
        menu_principal()
        escolha=input('>> ')
        if escolha in list('1234'):
            if escolha=='1':
                opcoes_1()
                print('=' * 65)
                menu_1()
                print('=' * 65)
        elif escolha==5:
            print('Fim do Programa')
        else:
            print('Opção Inválida')

main()