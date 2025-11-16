num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operations = input("Choose the operation (+, -, *, /):")

match operations :
    case "+" :
        results = num1 + num2
        print(f"The results is {results}")
    case "-":
        results = num1 - num2
        print(f"The results is {results}")
    case "*":
        results = num1 * num2
        print(f"The results is {results}")
    case "/":
        results = num1 / num2
        print(f"The results is {results}")
    case _ :
        print("Invalid operation selected. ")

