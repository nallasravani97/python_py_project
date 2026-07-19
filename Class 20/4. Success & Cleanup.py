while True:
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a number: "))
        result = num1 / num2
    except ValueError:
        print("Invalid input! please enter a number")
    except ZeroDivisionError:
        print("Error! Division by zero is not allowed")
    else:
        print("Result is ", result)
        break
    finally:
        print("Execution attempt finished")
