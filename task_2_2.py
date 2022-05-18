
lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
lst_2 = []
i = 0
for value in lst:
    if value.isdigit():
        lst_2.insert(int(i), '"')
        lst_2.append(value.zfill(2))
        lst_2.insert(int(i) + 2, '"')
        i += 2
    elif value[0] in '+':
        lst_2.insert(int(i), '"')
        lst_2.append(value.zfill(3))
        lst_2.insert(int(i) + 2, '"')
        i += 2
    else:
        lst_2.append(value)
    i += 1

print(' '.join(lst_2))