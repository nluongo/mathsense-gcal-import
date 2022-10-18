import datetime
import re

import click
import requests
from bs4 import BeautifulSoup

from . import __version__

URL_UNF = 'http://mathsense.com/myapps/studentlog/instructor/myday?{}&instructorid=[NAL]-Nicholas&zoomid=Needham-Conexed&pagepop=1'

@click.command()
@click.version_option(version=__version__)
def main():
    """The mathsense gcal project"""
    click.echo("Hello, world!")
        
    date = datetime.date.today()
    url = URL_UNF.format(date)
    print(date)
    print(url)
    
    with requests.get(url, headers={"User-Agent": "XY"}) as response:
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        print(soup)
        print(soup.title)
        print(len(soup.find_all('td', string=re.compile('.*PM'))))
        time_element_list = soup.find_all('td', string=re.compile('.*PM'))
        for element in time_element_list:
            print(element.string)
