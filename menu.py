menu = """
1.Say Hi
2.Say What?
3.Say Goodbye
"""
print(menu)
choice = input()

if choice == '1':
	print("Hi")
elif choice == '2':
	print("Why pick 2?")
elif choice == '3':
	print("Well, goodbye then.")
else:
	print("You did not pick anything.")
