# you must use Pythonista on iOS to use this script (link in readme)
# import the clipboard and view it

import clipboard as cb

cbget = cb.get()
cleared = ''


if cbget == '':
	print('There is no text on the clipboard!')

# ask to delete the clipboard if there is text detected
else:
	print(cbget)
	
	print("""
-------
Do you want to delete this text?

Yes/No""")

	user_input = input(": ")

	if user_input == "yes":
		cb.set(cleared)
		print("\nAll clear!")
	elif user_input == "Yes":
		cb.set(cleared)
		print("\nAll clear!")
	else:
		print('\nThanks for using!')
