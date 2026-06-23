# Calculator v1

print("Welcome to calculator")

num1 = int(input("Enter first number: "))
operator = input("Enter operator: ")
num2 = int(input("Enter second number: "))


if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/" and num2 != 0:
    print(num1 / num2)
else:
    print("Cannot divide by zero")




