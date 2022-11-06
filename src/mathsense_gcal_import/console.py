from datetime import datetime, date, timedelta
import re

import click
import requests
from bs4 import BeautifulSoup

from . import __version__
from .gcal import setup, create_event
from .config import url_unf


@click.command()
@click.version_option(version=__version__)
def main():
    """The mathsense gcal project"""
    click.echo("Hello, world!")

    todays_date = date.today()
    url = url_unf.format(todays_date)
    click.echo(url)
    
    # Scrape mathsense.com for todays sessions
    with requests.get(url, headers={"User-Agent": "XY"}) as response:
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        # Search for td objects with text ending in AM/PM
        time_element_list = soup.find_all('td', string=re.compile('.*[AP]M'))
        start_times = [element.string for element in time_element_list]

    # IF sessions found then call GCal API and create calendar events 
    if len(time_element_list) > 0:
        service = setup()
    
        for start_time in start_times:
            create_event(service, start_time)
            click.echo(start_time)

    else:
        click.echo('No sessions found')


