import json
from reddit import post_image_URL
from datetime import datetime
from os import system
from sys import exit


class bcolors:

    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'


with open('orders.json') as f:
    orders = json.load(f)

d = datetime.now()
today = [d.day, d.month, d.year]

if len(orders) == 0 or orders[0]['cakeday'] != today:
    exit()

for order in orders:
    post_image_URL(order['title'], order['subreddit'], order['url'])

with open('orders.json', 'w') as f:
    f.write('[]')

system('mode con: cols=100 lines=40')
system('title ' + 'Happy Cakeday!')
system('cls')
cake = open('../src/cake.txt', 'r')
print(bcolors.OKGREEN + cake.read() + bcolors.ENDC)
print(40 * ' ' + '{}Happy Cakeday!{}'.format(bcolors.HEADER, bcolors.ENDC))
input(33 * ' ' + 'Your images have been posted')
