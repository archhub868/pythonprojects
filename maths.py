# A Simple Calculator
while True:
    try:
        var1 = int(input("Enter a number: "))
        var2 = int(input("Enter another number: "))

        operation = input("Choose an operation to continue: (+), (-), (/), (*), (**), (%) or 'exit' to quit: ")

        if operation == '+':

            addition = var1 + var2
            print('The addition is', addition)

        elif operation == '-':

            subtraction = var1 - var2
            print('The subtraction is', subtraction)

        elif operation == '/':

            division = var1 / var2
            print('The division is', division)

        elif operation == '*':

            multiplication = var1 * var2
            print('The multiplication is', multiplication)

        elif operation == '**':

            exponent = var1 ** var2
            print('The exponent is', exponent)

        elif operation == '%':

            modulus = var1 % var2
            print('The modulus is', modulus)

        elif operation.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break  

        else:
            print('Select a valid operation')

    except ValueError:
        print('You have not entered a valid number. Please try again.')
