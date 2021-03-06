from requests import get
def currency_rates(currency):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = get(url)
    html_words = str(response.content)

    if currency == "usd" or currency == "USD" or currency == "Usd":
        indx_1 = html_words.find("USD")  # 2213
        str_0 = html_words[2213:]
        indx_2 = str_0.find("Value")
        str_1 = str_0[91:95]
        str_1 = str_1.replace(',', '.')
        rub = float(str_1)
        print(rub)

    elif currency == "euro" or currency == "EURO" or currency == "Euro":
        indx_1 = html_words.find("EUR") #2380
        str_0 = html_words[indx_1:]
        indx_2 = str_0.find("Value") + 6
        str_1 = str_0[indx_2:indx_2 + 5]
        str_1 = str_1.replace(',', '.')
        rub = float(str_1)
        print(rub)

    else:
        print(None)
