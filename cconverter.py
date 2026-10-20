import json
from linecache import cache

import requests


def get_url(main_currency):
    return f'http://www.floatrates.com/daily/{main_currency}.json'


def get_cache(target_currency, cache, data):
    if not cache:
        for k, v in data.items():
            if k == 'usd' or k == 'eur':
                cache[k] = float(v['rate'])
    else:
        cache[target_currency] = float(data[target_currency]['rate'])


def convert(rate, amount: float, ):
    return round(amount * rate, 2)


if __name__ == '__main__':
    main_currency = input().lower()
    target_currency = input().lower()
    amount = float(input())
    response = requests.get(get_url(main_currency))
    data = json.loads(response.text)
    cache_currency = {}
    get_cache(target_currency, cache_currency, data)

    while True:
        print('Checking the cache...')

        if target_currency in cache_currency:
            print('Oh! It is in the cache!')
            print(f'You received {convert(cache_currency[target_currency], amount)} {target_currency.upper()}.')
        else:
            print('Sorry, but it is not in the cache!')
            get_cache(target_currency, cache_currency, data)
            print(f'You received {convert(cache_currency[target_currency], amount)} {target_currency.upper()}.')

        target_currency = input().lower()
        amount = float(input())
