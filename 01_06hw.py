import requests

lst = []
usd = []
response = requests.get('https://bank.gov.ua/ua/markets/exchangerates')
response_text = response.text
response_parse = response_text.split('<td class="hidden-sm" data-label="Код цифровий"><span class="value">')


for _ in response_parse:
    if _.startswith('840'):
        for __ in _.split('<td data-label="Офіційний курс"'):
            if __.startswith('>'):
                for ___ in __:
                    if ___.isdigit():
                        usd.append(___)
                    elif ___ == ',':
                        usd.append('.')

usd = float(''.join(usd))
n = input('Введите количество валюты в гривнах: ')
def trans(a, b):
    return int(a)/round(b,2)

print('Ваша валюта в долларах:', round(trans(n, usd), 2))



# response_parse = response_text.split('<td class="hidden-sm" data-label="Код цифровий"><span class="value">')
# for _ in response_parse:
#     if _.startswith('840'):
#         for __ in _.split('</span>'):
#             if __.startswith('840'):
#                 response_parse = response_text.split('<td data-label="Офіційний курс">')
#                 for _1 in response_parse:
#                     for __1 in _1.split('</td>'):
#                         lst.append(__1)



# usd_exc = lst[0]
# print(usd_exc)

