print("Калькулятор")
name = input("Введите имя")
print("Здравствуйте, " + name + "!")
print("Доступные операции: '+', '-', '/', '/', '%', '**', '*',.")
while True:
    operation = input("Введите операции: ")
    if operation not in [ '+', '-', '/', '/', '%', '**', '*',]:
        print("Неверный ввод.")
    break
while True:
    name1 = int(input("Введите первое число: "))
    name2 = int(input("Введите второе число: "))
    if operation == '+':
        result = name1 + name2
        print("Ответ: " + str(result))
    if operation == '-':
        result = name1 - name2
        print("Ответ: " + str(result))
    if operation == '*':
        result = name1 * name2
        print("Ответ: " + str(result))
    if operation == '/':
        result = name1 / name2
        print("Ответ: " + str(result))
    if operation == '//':
        result = name1 // name2
        print("Ответ: " + str(result))
    if operation == '%':
        result = name1 % name2
        print("Ответ: " + str(result))
    if operation == '**':
        result = name1 ** name2
        print("Ответ: " + str(result))
    break
        