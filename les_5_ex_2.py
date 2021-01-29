f = open("my_file.txt", 'w')
content = my_file.read()
print(f'Количество строк в файле - {len(content)}')
for i in range(len(content)):
    print(f'Общее количество слов - {len(content)}')
my_file.close()
