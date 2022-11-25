# tests/test_console.py
import pytest
import click.testing

from mathsense_gcal_import import gcal
from datetime import date

def test_setup_succeeds():
    setup_out = gcal.setup()
    print(setup_out)
    assert setup_out

def test_build_event():
    event = gcal.build_event('10:30 AM')
    print(event['start']['dateTime'])
    start_datetime = event['start']['dateTime']
    end_datetime = event['end']['dateTime']
    start_date, start_time = start_datetime.split('T')
    end_date, end_time = end_datetime.split('T')
    start_time_pass = start_time == '10:30:00'
    start_date_pass = start_date == str(date.today())
    end_time_pass = end_time == '11:00:00'
    end_date_pass = end_date == str(date.today())
    
    assert start_time_pass and start_date_pass and end_time_pass and end_date_pass

test_setup_succeeds()
test_build_event()
