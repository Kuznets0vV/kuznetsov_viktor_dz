lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for elem in range(len(lst)):
    normal_view = lst[elem].split(' ')[len(lst[elem].split(' ')) -1]

    print(f'Привет,{normal_view.lower().title()}!')








