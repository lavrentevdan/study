cmnd = ''
valid_answers = ['1', '2', '3', '4']
action = 0
def addition(a,b):
    return a + b
def substraction(a,b):
    return a - b
def division(a,b):
    return a / b
def multiplication(a,b):
    return a * b

while action != 5:
    print('--------------------------------------------\nВыберите действие:\n\n1 - Сложить\n2 - Вычесть\n3 - Умножить\n4 - Разделить\n5 - Выход.\n')
    cmnd = input().strip()
    if cmnd in valid_answers:
        action = int(cmnd) 
    elif cmnd == '5':
        action = 5
    else:
        input(' \nНесуществующая команда, нажмите Enter, чтобы продолжить...')
        action = 0

        

    match action:
        case 1:
            a = int(input("Первый аргумент:"))
            b = int(input("Второй аргумент:"))
            print(f'Результат - {addition(a,b)}, нажмите Enter, чтобы продолжить...')
            input()
        case 2:
            a = int(input("Первый аргумент:"))
            b = int(input("Второй аргумент:"))
            print(f'Результат - {substraction(a,b)}, нажмите Enter, чтобы продолжить...')
            input()
        case 3:
            a = int(input("Первый аргумент:"))
            b = int(input("Второй аргумент:"))
            print(f'Результат - {multiplication(a,b)}, нажмите Enter, чтобы продолжить...')
            input()
        case 4:
            a = int(input("Первый аргумент:"))
            b = int(input("Второй аргумент:"))
            print(f'Результат - {division(a,b)}, нажмите Enter, чтобы продолжить...')
            input()
        case _: pass