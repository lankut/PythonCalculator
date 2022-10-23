import controller
import view

first = 0
second = 0
expression = ''
total_expression = ''
ops = ''
total = 0
total_2 = 0

# print (type(expression))

def init_string():
    global expression
    global total_expression
    expression = controller.input_string('Введите выражение (чтобы пропустить и вводить числа нажмите Enter): ')
    total_expression = expression
    if expression == '':
        return True

def init_first():
    global first
    first = controller.input_integer('Введите число: ')

def init_second():
    global second
    second = controller.input_integer('Введите число: ')

def init_ops():
    global ops
    ops = controller.input_operation('Введите операцию: ')
    if ops == '=':
        view.print_total()
        return True