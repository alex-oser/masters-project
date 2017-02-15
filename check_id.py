from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'

def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1XFbYrXx1wPUwBUz2IdrpDr4KfvlG17p6BgQjA9N1TBc/edit
    """

    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', developerKey = 'AIzaSyCvaAkTFdsO2aV9By0T-4rSRB_qjm54-Mo',
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1vbxWC9lv1ceJZVyQWCpdAfGwt4DH6tL3QxLfOvrdCMk'
    rangeName = 'B:B'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])
    print(values)

if __name__ == '__main__':
    main()

