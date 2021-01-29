f = open("my_file.txt", 'w')
line = input('Enter text \n')
        if line == '':
            break
        f.write(line + '\n')

