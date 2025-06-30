print("")
number1=int(input("Enter number 1 : "))
number2=int(input("Enter number 2 :"))
operation=input("Enter operation (+, -, *, /) or t to quit ")
if operation == "+":
    result = number1 + number2
    print("Result:", result)
elif operation == "-":
    result = number1 - number2
    print("Result:", result)
elif operation == "*":
    result = number1 * number2
    print("Result:", result)
elif operation == "/":
    if number2 != 0:
        result = number1 / number2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation.") 
    
if operation == "t":
    print("Exiting the calculator.")
