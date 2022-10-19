import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar']

def setup():
    """Initializes connections with Google Calendar API"""
    
    print(os.getcwd())
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
        service = build('calendar', 'v3', credentials=cred)
        print(service)
        print('Did it')
        return service
    except HttpError as error:
        print(f'An error occurred: {error}')
