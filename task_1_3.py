percent = [i for i in range(1, 101)]
for pers in percent:
        if pers % 10 == 1 and pers != 11:
            print(pers, 'процент')
        elif pers % 10 == 2:
            print(pers, 'процента')
        elif pers % 10 == 3:
            print(pers, 'процента')
        elif pers % 10 == 4:
            print(pers, 'процента')
        else:
            print(pers, 'процентов')
