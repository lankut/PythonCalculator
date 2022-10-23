import controller
import model
import view

while True:
    if model.init_string():
        break
    controller.parsing()
    controller.string_operation(model.expression)
    view.print_total_2()

model.init_first()
while True:
    if model.init_ops():
        break
    model.init_second()
    controller.operation()
    view.print_total()
    model.first = model.total