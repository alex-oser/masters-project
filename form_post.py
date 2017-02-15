import requests
import re

# from cmd import Cmd

# class MyPrompt(Cmd):

#     def do_hello(self, args):
#         """Says hello. If you provide a name, it will greet you with it."""
#         if len(args) == 0:
#             name = 'stranger'
#         else:
#             name = args
#         print "Hello, %s" % name

#     def do_quit(self, args):
#         """Quits the program."""
#         print "Quitting."
#         raise SystemExit


# if __name__ == '__main__':
#     prompt = MyPrompt()
#     prompt.prompt = '> '
#     prompt.cmdloop('Starting prompt...')

def post_to_form(info):

	payload = {
			'entry.1818803079': 'test-id',
			'entry.762012872': info
			}
	url = "https://docs.google.com/forms/d/e/1FAIpQLSefOHAw57UxyOzOFDhzRhWbZ2eRfU6SM_b5UEdH33QiakdkEA/formResponse"

	requests.post(url, data=payload)

def cmd_loop():

	in_command_loop = True
	print('Type help for options')
	while in_command_loop:
		info = raw_input('>').strip()
		if info == 'help':
			print('help for options\nexit to quit program\nSwipe ID card to get data')
		elif info == 'exit':
			in_command_loop = False
		elif re.match("^;\d{5}=\d{11}\?$", info):
			print('About to post ID data')
			post_to_form(info)
		else:
			print "Error"

if __name__ == '__main__':
	cmd_loop()
	        


