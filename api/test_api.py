import sys
from controller.api_commands import *

if __name__ == '__main__':

	try:
		command = sys.argv[1]
		attr = sys.argv[2]

		if command == 'search_key':
			print search_key(attr)

		if command == 'search_specific':
			print(search_specific(command,attr))

	except Exception as e:	
		print("Error: {0}".format(e))