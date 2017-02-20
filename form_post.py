from __future__ import print_function
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import requests, re, httplib2, os

def post_to_form(info, student_id):
	try:
		payload = {
				'entry.1818803079': student_id,
				'entry.762012872': info
				}
		url = "https://docs.google.com/forms/d/e/1FAIpQLSefOHAw57UxyOzOFDhzRhWbZ2eRfU6SM_b5UEdH33QiakdkEA/formResponse"
		requests.post(url, data=payload)
		return 1
	except:
		return 0

def check_id(student_id):

    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', developerKey = 'AIzaSyCvaAkTFdsO2aV9By0T-4rSRB_qjm54-Mo',
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1vbxWC9lv1ceJZVyQWCpdAfGwt4DH6tL3QxLfOvrdCMk'
    rangeName = 'B:C'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = list(result.get('values', []))
    for v in values:
    	if v[1] == student_id:
    		return v[0]
    for v in values:
    	pass   	
   	return False

def cmd_loop():

	in_command_loop = True
	while in_command_loop:
		print('> Please swipe student ID card or type help for options')
		info = raw_input('>>> ').strip()
		if info == 'help':
			print('help - display options\nexit - quit program\nSwipe ID card to get data')
		elif info == 'exit':
			in_command_loop = False
		elif re.match("^;\d{5}=\d{11}\?$", info):
			student_id = check_id(info)
			if student_id:
				print('Card recognized as:', student_id)
			else:
				print('Your card was not recognized, please enter you student ID or type "cancel"')
				student_id = raw_input('>>> ').strip()
				if student_id == 'cancel':
					continue
			success = post_to_form(info, student_id)
			if success:
				print('> Success!')
		else:
			print("Error: Invalid Input")



if __name__ == '__main__':
	cmd_loop()
	        


