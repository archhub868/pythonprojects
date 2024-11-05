
'''name = input('what is your name ? ')
color = input('What is your favourite color ? ')
print(name, 'likes' , color)'''

'''weight_lbs = input('what is your weight(lbs)? ')
weight_kg = float(weight_lbs) * 2.2
print('your weight is ', weight_kg, 'kg')'''

# Operator Precedence
'''x =  (2+3) * 10 - 3
print(x) '''

# Math functions
'''import math
print(math.gcd(60 , 20 ,40))'''

# Control Statements

'''Price = 100000
has_good_credit = False
if has_good_credit:
    down_payment = 0.1 * Price
    print(f"Down payment is {down_payment}")
else:
 down_payment = 0.2 * Price
print(f"Down payment is {down_payment}")'''

# Comparison Operators

'''name =input('Enter Your Name: ')
if len(name) < 3:
   print(f"{name} should be more than 3 characters ")
elif len(name) > 10:
   print(f"{name} should be less than 10 characters ")
else:
 print(f"{name} Looks good ")'''

# Weight Converter
'''weight = int(input('Enter Weight: '))
unit = input('Lbs or Kgs: ')
if unit.upper() == 'LBS':
    weight_in_kg = weight * 0.45
    print(f'{weight} Lbs is equal to {weight_in_kg} Kgs')
else:
    weight_in_lbs = weight / 0.45
    print(f'{weight} Kgs is equal to {weight_in_lbs} Lbs')
    '''
# Number guess game
'''secret_number = 10
n = 0
while n < 3:
    guess = int(input('Guess a number: '))
    n += 1
    if guess == secret_number:
        print('You Got it Right Nigga')
        break
else:
    print("Come on Man, You're Better Than this")
'''
# A simple calculator

try:
    x = int(input('Enter the first number to begin: '))
    y = int(input('Insert the second number to find out what happens: '))

    operation = input('This is where the magic goes: (+) or (-) or  (*)  or  (/): ')

    if operation == '+':
        print("'Let's perform some addition magic")
        sum = x + y
        print(f'The sum is = ({sum})') 
    elif operation == '*':
        print('You have selected the product sign now wait for the magic')
        multiplication = x * y
        print(f'The product of the two numbers is = ({multiplication})')
    elif operation == '/':
        print('You have selected the division sign now wait for the magic')
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

