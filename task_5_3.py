from itertools import zip_longest
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Дима', 'Федя'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

iterator = zip_longest(tutors, klasses[:len(tutors)], fillvalue='NONE') # если имен больше чем классов то выведет NONE

for i in iterator:
    print(i)

