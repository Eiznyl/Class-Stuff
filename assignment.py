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
	elif choice == '2':
		user = input('Enter your name:')
		print('Hello', user)
	elif choice == '3':
		n = int(input("Enter preferred number:"))
		sum1 = 0
		while(n > 0):
			sum1 = sum1 + n
			n = n - 1
		print("Calculated sum:", sum1)


 

		

