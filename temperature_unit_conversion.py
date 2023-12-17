def celcius_to_farenheit(degcelsius):
    degcelsius = float(input("enter the temperature in celsius "))
    farenheit = round(degcelsius * (9/5) + 32, 2)
    return f"farenheit: {farenheit}"

def farenheitdeg_to_celcius(degfarenheit):
    degfarenheit = float(input("enter the temperature in farenheit "))
    celcius = round((degfarenheit - 32) * 5/9, 2)
    return f"celcius: {celcius}"

def selection():
    while True:
        conversion = input("Enter F to convert Celcius to Farenheit " + 
                   "or " + "C Farenheit to Celsius: ")
        if conversion == "c":
            print(celcius_to_farenheit(0))
        elif conversion == "f":
            print(farenheitdeg_to_celcius(0))
        else:
            print("invalid entry")

        calculate_again = input("enter 'y' to do conversion or enter 'n' to quit ")
        if calculate_again == "y":
            continue
        else:
            if calculate_again == "n":
                print("Goodbye...")
                exit()

print(selection())