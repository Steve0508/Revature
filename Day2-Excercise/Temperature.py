choice = input("Convert to (C)elsius or (F)ahrenheit? ")
temp = float(input("Enter temperature: "))

if choice.lower() == 'c':
    print("In Celsius:", (temp - 32) * 5/9)
else:
    print("In Fahrenheit:", temp * 9/5 + 32)
