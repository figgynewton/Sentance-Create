Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> listMessage = []
>>> message = input('Enter first word of your message: ').strip()
Enter first word of your message: the
>>> while message != 'done!':
	listMessage.append(message)
	message = input('Please enter the next word of your message or type done! when complete ').strip()

	
Please enter the next word of your message or type done! when complete cat
Please enter the next word of your message or type done! when complete ran
Please enter the next word of your message or type done! when complete home
Please enter the next word of your message or type done! when complete quickly
Please enter the next word of your message or type done! when complete done!
>>> print(' '.join(listMessage).capitalize()+'.')
The cat ran home quickly.
>>> 
