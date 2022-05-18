import random
lst = [round(random.uniform(1, 99), 2) for i in range(10)] #лень придумывать цены. решил зарандомить
print('id до сортивоки списка   ', id(lst))
lst.sort()
print('id после сортивоки списка', id(lst))
print('список отсортированный по возрастанию ', lst)
lst.reverse()
print('список отсортированный по убыванию ', lst)
print('список цен:')

for i in lst:
    a = int(i)
    b = (i - a) * 100
    print(f'{a:02}руб {round(b):02}коп,', end='')
else:
    print(f'{a:02}руб {round(b):02}коп')

print('цены пяти самых дорогих товаров:')

for i in lst[0:5]: # делаем срез по первым пяти позициям
    a = int(i)
    b = (i - a) * 100
    print(f'{a:02}руб {round(b):02}коп', end=', ')
else:
    print(f'{a:02}руб {round(b):02}коп')

