a = input("Enter the first number:")
b = input("Enter the second number:")
operator = input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, or 4 for division: " )

if operator == 1:
	print( a + b)
elif operator == 2:
	print(a - b)
elif operator == 3:
	print(a * b)
elif operator == 4:
	print(a / b)
else:
	print("not a valid operator")
