
from sys import path


def here():
    '''
    Returns path of this file.
    '''
    return path[0]


def open_base(file, mode="r", kontent=""):
    '''
    Opens file in this folder with following parameters: mode (r,w,a), kontent (preferably string).
    r: open and return rows of a file.
    w, a: write file with kontent. Returns kontent.
    '''
    with open(here()+file, mode, encoding="utf8") as base:
        if mode == "r":
            output = base.readlines()
        else:
            base.write(kontent)
            output = kontent
    return output


def open_currencies(mode="r", kontent=""):
    '''
    Open file currencies.
    '''
    currency_tab = open_base("\currencies.txt", mode, kontent)
    return currency_tab


def currlist():
    data_raw = open_currencies()
    data = []
    for row in data_raw:
        data.append(row[:-2].rsplit(";"))
    return data


def currency_names():
    currencies = []
    data = currlist()
    for currency in data:
        currencies.append(f"{currency[0]} ({currency[1]})")
    return currencies


def currdikt():
    dikt = {}
    data = currlist()
    for currency in data:
        dikt[f"{currency[0]} ({currency[1]})"] = currency[2:]
    return dikt


if __name__ == "__main__":
    print(currency_names())
    currency = 'dolar amerykański (USD)'
    print(currency)
    result = float(currdikt()[currency][1])
    print(result)
    print(type(result))
