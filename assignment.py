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
	elif choice == '5':
		n = int(input("Enter preferred number:"))
		pro1 = 1
		while(n > 0):
			pro1 = pro1 * n
			n = n - 1
		print("Calculated product:", pro1)
	elif choice == '6':
		for i in range(1, 13):
			for j in range(1, 13):
				print(i*j, end='')
				print(' ' *(10-(len(str(i*j)))), end='')
			print('\n')
	elif choice == '4':
		num = int(input('Enter preferred number:'))
		sum1 = 0
		for i in range(0,num + 1):
        		if not i % 5 or not i % 3:
                		sum1 = sum1 + i
		print(sum1)


	

 

		

