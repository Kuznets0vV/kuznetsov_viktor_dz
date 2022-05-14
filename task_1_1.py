sec = input('введите количество секунд')
second = int(sec) % 30758400000
day = second // 86400
second %= 86400
hour = second // 3600
second %= 3600
minutes = second // 60
second %= 60
if 30758400000 >= int(sec) >= 86400:
    print(day, 'дн', hour, 'час', minutes, 'мин', second, 'сек')
elif 86400 >= int(sec) >= 3600:
    print(hour, 'час', minutes, 'мин', second, 'сек')
elif 3600 >= int(sec) >= 60:
    print(minutes, 'мин', second, 'сек')
elif int(sec) < 60:
    print(second, 'сек')
else:
    print('больше тысячи лет')
