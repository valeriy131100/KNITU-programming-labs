# Написать приложение «Калькулятор».
# Предусмотреть отдельный ввод математической операции между вводом двух чисел.
# Программа должна включать обработку исключительной ситуации деления на ноль.


def сумма(a, b):
    return a + b


def разность(a, b):
    return a - b


def произведение(a, b):
    return a * b


def частное(a, b):
    return a / b


операции = {'+': сумма, '-': разность, '*': произведение, '/': частное}
c, op, d = int(input()), input(), int(input())
print('Ответ: ', операции.get(op)(c, d))