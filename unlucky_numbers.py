# This application will loop from the range of 1 to 20
# and it will output the unlucky numbers which is 4 and 13,
# and it will show the odd and even numbers.
# To accomplish this, I used a for loop to loop on the numbers
# that ranges 1 to 21. I also used conditional so if the numbers
# are unlucky, odd, or even it will show in the console.

for x in range(1,21):
    if x == 4 or x == 13:
        print(f"{x} is UNLUCKY!")
    elif x%2 != 0:
        print(f"{x} is odd")
    else:
        print(f"{x} is even")