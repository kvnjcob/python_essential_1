# Functions

def input_numbers(number_count):
    while True:
        number_input = input(f"Enter the {number_count} : ")
        if number_input.isdigit():
            return number_input


def line():
    print("==================================")


def addition(num1, num2):
    number_add = num1 + num2
    print(f"Addition of {num1} + {num2} = {number_add}")


def subtraction(num1, num2):
    number_sub = num1 - num2
    print(f"Subtraction of {num1} - {num2} = {number_sub}")


def multiplication(num1, num2):
    number_mul = num1 * num2
    print(f"Multiplication of {num1} * {num2} = {number_mul}")


def division(num1, num2):
    number_div = int(num1 / num2)
    print(f"Division of {num1} / {num2} = {number_div}")


# Main
if __name__ == '__main__':

    while True:
        number1 = int(input_numbers("first number"))
        number2 = int(input_numbers("second number"))

        print("+ for Addition, " + "- for Subtraction, " + "/ for Division, " + "* for Multiplication, " +
              "q for Exit")
        choice = input("Select an option from the above : ")

        if choice == '+':
            addition(number1, number2)
            line()
        elif choice == '-':
            subtraction(number1, number2)
            line()
        elif choice == '/':
            if number2 == 0:
                print("Division by zero is impossible")
            else:
                division(number1, number2)
                line()
        elif choice == '*':
            multiplication(number1, number2)
            line()
        elif choice == 'q':
            print("===========EXIT===========")
            break
            line()
