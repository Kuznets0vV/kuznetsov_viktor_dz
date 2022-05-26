import random
first = ["автомобиль", "лес", "огонь", "город", "дом"]
second = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
thirst = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(num, repeats=True):
    """ функция для выведения случайных шуток, num это количество шуток"""
    jokes = []
    if not repeats:
        if num > min(len(first), len(second), len(thirst)):
            return 'не получится'
        else:
            random.shuffle(first)
            random.shuffle(second)
            random.shuffle(thirst)
            for i in range(num):
                jokes.append(f'{first[i]} {second[i]} {thirst[i]}')

    else:
        for i in range(num):
            first_list = random.choice(first)
            second_list = random.choice(second)
            thirst_list = random.choice(thirst)
            jokes.append(f'{first_list} {second_list} {thirst_list}')
    return jokes
print(get_jokes(4, False))
print(get_jokes(5, False))
print(get_jokes(6, False))