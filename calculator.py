# A simple calculator

try:
    x = int(input('Enter the first number to begin: '))
    y = int(input('Insert the second number to find out what happens: '))

    operation = input('This is where the magic goes: (+) or (-) or  (*)  or  (/): ')

    if operation == '+':
        print("'Let's perform some addition magic")
        add = x + y
        print(f'The sum is = ({add})')
    elif operation == '*':
        print('You have selected the product sign now wait for it')
        multiplication = x * y
        print(f'The product of the two numbers is = ({multiplication})')
    elif operation == '/':
        print('You have selected the division sign now wait for it')
        division = x / y
        print(f'The Division of the two numbers is = ({division})')
    elif operation == '-':
        print('You have selected the minus sign and this is what happens')
        minus = x - y
        print(f'The difference btn the two numbers is = ({minus})')
    else:
        print('Give me an operation to work with')
except ValueError:
    print('You have not entered a correct value')
