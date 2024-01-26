print("Enter the number of shape that you want to get the Area: ")
print("1. Circle")
print("2. Square")
print("3. Triangle")
print("4. Rectangle")


def circle(num1):
    num1 = int(input("Enter radius: "))
    area = float(3.14 * (num1)**2)
    return f"The area of circle: {area}"

def square(num1):
    num1 = int(input("Enter side: "))
    area = float(num1**2)
    return f"The are of square: {area}"

print(circle(""))
print(square(""))