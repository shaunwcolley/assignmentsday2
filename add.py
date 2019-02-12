num1 = input("What's the first number you'd like to add? > ")
num2 = input("Now, what is the second number? > ")
num1 = float(num1)
num2 = float(num2)
def add(x, y):
    result = x + y
    return result
result_for_user = add(num1, num2)
print(f"The result is {result_for_user}.")
