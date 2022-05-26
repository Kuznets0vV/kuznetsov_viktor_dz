dict_num = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

num = input('введите числительное на английском от 1 до 10  ')


def num_translate(num):
    if num.istitle():
        numer = num.lower()
        print(dict_num.get(numer).capitalize())
    else:
        print(dict_num.get(num))
    return dict_num.get(num)

num_translate(num)
