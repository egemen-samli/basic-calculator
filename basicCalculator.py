
def nth_root(x, n):
    if n == 0:
        return "Error! Division by zero"
    elif x < 0 and n % 2 == 0:
        return "Error! Cannot take even roots of negative numbers"
    return x ** (1 / n)

def calculator():

    while True:
        print("Select an operation")
        print("ADD for add")
        print("SUB for subtract")
        print("MUL for multiply")
        print("DIV for divide")
        print("EXP for exponentiation")
        print("NRT for Nth root of x")
        print("EXT for exit")

        selection = input("Enter selected operation: ")

        if selection == "EXT":
            print("Exiting calculator :/")
            break

        if selection in ("ADD", "SUB", "MUL", "DIV", "EXP"):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Enter numbers only")
                continue

            if selection == "ADD":
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif selection == "SUB":
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif selection == "MUL":
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif selection == "DIV":
                if num2 == 0:
                    print("Error! Division by zero")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
            elif selection == "EXP":
                print(f"Result: {num1} ^ {num2} = {num1 ** num2}")
        
        elif selection == "NRT":
            try:
                num1 = float(input("Enter base number (x): "))
                num2 = float(input("Enter the root (n): "))
                result = nth_root(num1, num2)
                print(f"Result: {num1}^(1/{num2}) = {result}")
            except ValueError:
                print("Invalid input! Enter numbers only")

        else:
            print("Invalid selection! Please enter a valid option.")

if __name__ == "__main__":
    calculator()