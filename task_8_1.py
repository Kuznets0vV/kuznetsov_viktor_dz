import re
mail = re.compile(r'([a-z0-9_\.]+)@([a-z0-9]+\.[a-z]+)')
def email_parse(email):
    received_info = mail.findall(email)
    if received_info:
        name, addr = received_info[0]
    else:
        raise ValueError(f'wrong email: {email}')
    print(name, addr)


email_parse('someone@geekbrains.ru')
email_parse('someone@geekbrainsru')