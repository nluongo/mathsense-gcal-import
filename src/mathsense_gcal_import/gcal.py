from datetime import datetime, date, timedelta
import os.path
import pickle

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from .config import calendar_id

SCOPES = ['https://www.googleapis.com/auth/calendar']

time_zone = 'America/New_York'
event_skeleton = {
    'summary': 'Tutoring',
    'description': 'mathsense.com/tablet',
    'start' : {
        'dateTime' : datetime.now(),
        'timeZone' : time_zone,
    },
    'end' : {
        'dateTime' : datetime.now(),
        'timeZone' : time_zone,
    },
}
format = '%I:%M %p'

def setup():
    """Initializes connections with Google Calendar API"""
    
    # Google Calendar setup taken wholesale from quickstart.py
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is created automatically when the authorization flow completes for the first time
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        #Save the credentials for next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    try:
        service = build('calendar', 'v3', credentials=creds)
        return service
    except HttpError as error:
        print(f'An error occurred: {error}')

def build_event(start_time: str):
    """ 
    Creates an event object in gcal required format with the given start time

    :param str start_time: The start time of the session eg "10:30 AM"
    :return dict: Event info dictionary
    """

    start_time = datetime.strptime(start_time, format)
    start_time = datetime.combine(date.today(), start_time.time())
    time_delta = timedelta(minutes=30)
    end_time = start_time + time_delta

    event = event_skeleton
    event['start']['dateTime'] = start_time.isoformat()
    event['end']['dateTime'] = end_time.isoformat()

    return event

def send_event_to_calendar(service, event):
    """
    Send event object to gcal to be created

    :param service: gcal service object
    :param event: Event info dictionary
    """

    event = service.events().insert(calendarId=calendar_id, body=event).execute()
    print('Event created')
