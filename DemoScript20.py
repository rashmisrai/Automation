# Exception in Python

# Exception handling is a mechanism in Python that allows you to handle errors gracefully.
# It also prevents your program from crashing.

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except Exception as e:
    print("An unexpected error occurred:", str(e))
else:
    print("Division was successful.")
finally:
    print("Execution completed.")