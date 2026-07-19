try:
    A = int(input("Enter a  first number: "))
    B = int(input("Enter a  second number: "))
    C = input("Enter a value: ")

    if A<0 or B<0:
        raise Exception("Negative Numbers not allowed")
    result = (A/B) +C
    print("Result:", result)
except ZeroDivisionError:
    print("Division by zero not permitted")
except TypeError as e:
    print("Invalid input:", e)
except Exception as e:
    print("Something went wrong:", e)