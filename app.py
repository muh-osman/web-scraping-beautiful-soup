import requests
from bs4 import BeautifulSoup
import csv


# link = input('pls enter the link: ')
link = 'https://www.yallakora.com/match-center/?date=12/22/2022'

html = requests.get(link)

def main(html):
    src = html.content
    print(src)

main(html)