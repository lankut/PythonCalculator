import logger
import model


def error_value():
    logger.logger('Ошибка ввода данных')
    return print('Ошибка ввода данных')

def print_total():
    return print(f'Результат: {model.total}')

def print_total_2():
    return print(f'Результат: {model.total_2}')