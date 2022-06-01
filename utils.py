from datetime import datetime
import requests
import xmltodict


def currency_rates(currency):
    url = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    currency_str = url.text
    curr_find = currency_str.find(currency)  # ищем название валюты
    if curr_find != -1:
        index_str = currency_str.find('<Value>', curr_find)
        pre_result = float(currency_str[index_str + 7:index_str + 14].replace(',', '.'))
        """    Можно было и первую часть сделать через xmltodict,
        но решил попробовать строками  """
        data_dict = xmltodict.parse(url.content)  # парсим в словарь и добираемся до значения даты
        val = data_dict['ValCurs']
        data = val['@Date']
        data_time = datetime.strptime(data, '%d.%m.%Y')  # перевожу из строки в дату
        return f'{pre_result} {data_time}'
    else:
        return f'None'





print(currency_rates(input('введите курс валюты в сокращенном виде например USD  ')))
