def addition(x, y): 
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

print("Select an operation")
print("1 = Addition")
print("2 = Subtraction")
print("3 = Multiplication")
print("4 = Division")

while True:
    #User input
    choice = input("Enter your choice: ") 
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter the first number"))
            num2 = float(input("Enter the second number"))
        except ValueError:
            print("Error: Please enter a valid number")
            continue
        if choice == '1':
            print(f"{num1} + {num2} = {addition(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtraction(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiplication(num1, num2)}")
        elif choice == "4":
            print(f"{num1} / {num2} = {division(num1, num2)}")
        
        next_calc = input("Would you like to make another calculation?: ")
        if next_calc == "no":
            break

            
    