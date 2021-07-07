import requests
import lxml.html as html
import os
import datetime
from selenium import webdriver 



HOME_URL = 'http://toscrape.com/'

XPATH_LINK_TO_ARTICLE = '//body/div/div[2]/div/p/a[1]/@href'
XPATH_CARTAS = '//body[@id="default"]/div/div/div/aside/div/ul/li/ul/li/a/text()'

def parse_click(link, today):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)

            try:
                cartas = parsed.xpath(XPATH_CARTAS)[0]
                cartas = cartas.replace('\n', '')
            except IndexError:
                return

            with open(f'{today}/{cartas}.txt', 'w', encoding='utf-8') as f:
                f.write(cartas)
                f.write('\n')
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)


def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_click = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            #print(links_to_click)

            today = datetime.date.today().strftime('%d-%m-%a')
            if not os.path.isdir(today):
                os.mkdir(today)

            for link in links_to_click:

                parse_click(link, today)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parse_home()


if __name__ == '__main__':
    run()
