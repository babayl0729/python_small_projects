def circle(num1):
    try:
        num1 = float(input("Enter radius: "))
    except ValueError:
        return "That's not a number."
    area = float(3.14 * (num1)**2)
    return f"The area of circle: {area}"

def square(num1):
    try:
        num1 = float(input("Enter side: "))
    except ValueError:
        return "That's not a number."
    area = float(num1**2)
    return f"The are of square: {area}"

def triangle(num1,num2):
    try:
        num1 = float(input("Enter height: "))
        num2 = float(input("Enter base: "))
    except ValueError:
        return "That's not a number."
    area = (num1*num2)/2
    return f"The area of triangle: {area}"

def rectangle(num1,num2):
    try:
        num1 = float(input("Enter lenght: "))
        num2 = float(input("Enter width: "))
    except ValueError:
        return "That's not a number."
    area = float(num1 * num2)
    return f"The area of rectangle: "

while True:
    print("1. Circle")
    print("2. Square")
    print("3. Triangle")
    print("4. Rectangle")
    print("5. Quit")

    number = int(input("Enter the number of shape that you want to get the Area: "))

    if number == 1:
        print("You picked circle:")
        print(circle(""))
    elif number == 2:
        print("You picked Square")
        print(square(""))
    elif number == 3:
        print("You picked Triangle")
        print(triangle("",""))
    elif number == 4:
        print("You picked Rectangle")
        print(rectangle("",""))
    elif number == 5:
        print("Goodbye...")
        break
    else:
        print("Invalid entry!")
        print("Pick 5 to quit")
    