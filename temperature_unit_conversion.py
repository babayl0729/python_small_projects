# This application is a temperature unit conversion
# where a user can enter either Celsius or Farenheit 
# to get converted to Celsius or Farenheit.
# The first function is where the Farenheit formula.
# The second function is where the Celsius formula.
# The third function is where the application prompt
# the user and give an option for the user to choose
# either Celsius or Farenheit.
# After the user entered a unit the application will
# prompt the user to enter the actual temperature.
# Once the user entered the actual temperature,
# the application will convert it to either Celsius
# or Farenheit. The conversion happens by calling
# the first or second function for Celsius 
# to Farenheit conversion, or Farenheit to Celsius
# conversion.

# Farenheit formula
def celcius_to_farenheit(degcelsius):
    degcelsius = float(input("Enter the temperature in Celsius to convert"
                             + " in Farenheit: "))
    farenheit = round(degcelsius * (9/5) + 32, 2)
    return f"farenheit: {farenheit}"

# Celsius formula
def farenheitdeg_to_celcius(degfarenheit):
    degfarenheit = float(input("Enter the temperature in Farenheit " 
                               + "to convert to Celsius: "))
    celcius = round((degfarenheit - 32) * 5/9, 2)
    return f"celcius: {celcius}"

# where user input the temperature unit for conversion
def selection():
    while True:
        conversion = input("Enter F to convert Celcius to Farenheit " + 
                   "\nEnter C to convert Farenheit to Celsius" +
                     "\nTemperature Unit: ")
        if conversion == "c":
            print(celcius_to_farenheit(0))
        elif conversion == "f":
            print(farenheitdeg_to_celcius(0))
        else:
            print("invalid entry")

        calculate_again = input("Enter 'y' to do another conversion or enter 'n' to quit ")
        if calculate_again == "y":
            continue
        else:
            if calculate_again == "n":
                print("Goodbye...")
                exit()

print(selection())