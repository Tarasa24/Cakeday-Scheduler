import json
from reddit import created
from datetime import datetime
from sys import exit


def next_cakeday(arg):
    d = datetime.utcfromtimestamp(arg)

    corr = 0
    while True:
        corr += 1
        if (d.replace(year=d.year + 1) - datetime.now()).days >= 0:
            break
    d = d.replace(year=d.year + corr)

    until = 'in {} days'.format((d - datetime.now()).days)
    if (d - datetime.now()).days <= 1:
        until = 'in {} day'.format((d - datetime.now()).days)

    return [[d.day, d.month, d.year], until]


with open('../config.json') as f:
    config = json.load(f)

if config['username'] == '' or len(config['client_id']) != 14 or len(config['client_secret']) != 27:
    print('config.json | invalid data')
    exit()

cakeday_list = next_cakeday(created(config['username']))
cakeday = '{}/{}/{} ({})'.format(cakeday_list[0][0],
                                 cakeday_list[0][1],
                                 cakeday_list[0][2], cakeday_list[1])

print('Hello, {}'.format(config['username']))
print('Cakeday: {}\n'.format(cakeday))
print('Lets make our schedule order then:')

with open('orders.json', mode='r', encoding='utf-8') as ordersjson:
    feeds = json.load(ordersjson)

title = input('Title: ')
subreddit = input('r/: ')
url = input('Url: ')

with open('orders.json', mode='w', encoding='utf-8') as ordersjson:
    entry = {
        'title': title,
        'subreddit': subreddit,
        'url': url,
        'cakeday': cakeday_list[0],
        }
    feeds.append(entry)
    json.dump(feeds, ordersjson)
