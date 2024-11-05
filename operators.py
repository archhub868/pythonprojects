#Logic operators

'''print(56 < 100 and 45 <23)
print(56 < 100 or 45 < 23)
print(not(56 < 100 or 45 < 23))'''

temperature = 77

if temperature < 45:
    print("The Temperature is Fairly warm")

else:
    print("The Temperature will cook ya!")

#A Program that returns the Smallest number between three numbers

x = 34
y = 40
z = 10

if z < y and z < x:
    print(z, "is the smallest")
elif y < x and y < z:
    print(x, "is the smallest")
else:
    print(z, "is the smallest")

#Program to check if number is odd or even

num = 13

if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

#While Loop
count = 100
while count >=90:
    print(count)
    count -= 1

#For loop
for x in range(2,7):
    print(x)

for number in range(10,15,4):
    print(number)

#Lists
cars = ["Audi", "Toyota", "Mercedes"]
for car in cars:
    print(car)

#Break

'''secret_number = 10
n = 0
while n < 3:
    guess = int(input('Guess a number: '))
    n += 1
    if guess == secret_number:
        print('You Got it Right')
        break
else:
    print("Come on Man, You're Better Than this")'''

'''n = 30
while n <= 37:
    print(n)

    if n == 35:
        break
    n += 1'''

#Continue
accessories = ["BT Speaker", "Power Bank", "Headphones"]
for y in accessories:
    if y == "Power Bank":
        continue
    print(y)

