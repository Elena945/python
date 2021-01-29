def summary():
    try:
        with open('file.txt', 'w') as file:
            line = input('Введите числа через пробел \n')
            file.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()
