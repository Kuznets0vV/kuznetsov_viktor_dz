names = ("Иван", "Мария", "Петр", "Илья")


def thesaurus(names):
    dict_name = {}
    for name in names:
        dict_name.setdefault(name[0], [])
        dict_name[name[0]].append(name)
    return dict_name


print(thesaurus(names))
