import logger
import model
import view

def input_string(enter):
    while True:
        try:
            a = str(input(enter))
            return a
        except:
            view.error_value()

def input_integer(enter):
    while True:
        try:
            a = int(input(enter))
            return a
        except:
            view.error_value()


def input_operation(enter):
    while True:
        a = input(enter)
        if a in ['+', '-', '*', '/', '=']:
            return a
        else:
            view.error_value()

def operation():
    match (model.ops):
        case '+':
            model.total = model.first + model.second
        case '-':
            model.total = model.first - model.second
        case '*':
            model.total = model.first * model.second
        case '/':
            while model.second == 0:
                print('На ноль делить нельзя!')
                model.init_second()
            model.total = int(model.first / model.second)

        case _:
            view.error_value()
    logger.logger(f'{model.first} {model.ops} {model.second} = {model.total}')

def parsing():
    model.expression = model.expression.replace(' ', '')
    model.expression = model.expression.replace('/', ' / ').replace('*', ' * ').replace('+', ' + ').replace('-', ' - ')
    model.expression = model.expression.split()

def delete_element(string, i):
    string.pop(i+1)
    string.pop(i)

def string_operation(string):
    while len(string) > 1:
        if '/' in string or '*' in string:
            for i in range(len(string)):
                if string[i] == '/':
                    string[i-1] = int(string[i-1]) / int(string[i+1])
                    delete_element(string, i)
                    break
                if string[i] == '*':
                    string[i-1] = int(string[i-1]) * int(string[i+1])
                    delete_element(string, i)
                    break
        elif '+' in string or '-' in string:
            for i in range(len(string)):
                if string[i] == '+':
                    string[i - 1] = int(string[i - 1]) + int(string[i + 1])
                    delete_element(string, i)
                    break
                if string[i] == '-':
                    string[i - 1] = int(string[i - 1]) - int(string[i + 1])
                    delete_element(string, i)
                    break
    model.total_2 = string
    logger.logger(f'Выражение {model.total_expression} = {model.total_2}')