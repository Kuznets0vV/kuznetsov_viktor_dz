def thesaurus_adv(*surnames_name):

    dict_name = {}
    for surname_name in surnames_name:
        name, surname = surname_name.split()
        dict_name.setdefault(surname[0], {})
        dict_name[surname[0]].setdefault(name[0], [])
        dict_name[surname[0]][name[0]].append(name)
    return dict_name


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов",
                    "Анна Савельева"))

