def textline(foo, bar):
	print(' ', end='')
	for i in range(len(foo)):
		print(bar, end='')
	print()

def textbox(foo):
	textline(foo, '_')
	print('<', end='')
	print(foo, end='')
	print('>')
	textline(foo, '_')

bar = input("Enter your message:")
textbox(bar)

fin = open('moose.py')

for line in fin:
	print(line, end='')




