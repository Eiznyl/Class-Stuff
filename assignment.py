menu = """
1. Say 'Hello World'
2. Ask your name, and greet you.
3. Find the sum from 1 to n
4. Find the sum from 1 to n that are multiples of 3 or 5
5. Find the product from 1 to n
6. Print a multiplication table to 12
7. Play a guessing game
8. Exit
"""

while(True):
	print(menu)

	choice = input()
	
	if choice == '1':
		print('Hello World')
	elif choice == '8':
		break
	else:
		print("Invalid choice...")
	if choice == '2':
		from codeformenuthing import *
		name 

