try:
    A = int(input("Enter a  first number: "))
    B = int(input("Enter second number: "))
    C = input("Enter a value: ")
    result = (A /B) + C
    print("Result:", result)

except ZeroDivisionError:
    print("Division by zero is not permitted")
except TypeError as e:
    print("Invalid datatype")
except Exception as error:
    print(error)