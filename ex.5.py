my_list = [7, 5, 3, 3, 2]
application = input('Enter number:')
for index, number in enumerate(my_list):
    if int(application) < int(number):
    my_list.insert(index, application)
    my_list.append(application)
print(my_list)
