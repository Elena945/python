product = []
institution = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analitics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
    for a in features.keys():
        user_data = input(a)
        institution[a] = int(user_data) if (a == 'цена' or a == 'количество') else user_data
        analitics[a].append(institution[a])
    product.append((num, institution.copy))
    print('product analitics:')
    for key, value in analitics.items():
        print(key, value)
