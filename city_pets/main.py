# This application contains 3 files. cities_in_md.property
# contains vafrious cities from MD and where it will ask 
# the user to enter his/her city he/she grew up. The next
# file is your_pet.py where it will ask the user to enter
# what kind of pet he/she has. The 3rd file is the main 
# file where it will output the results from the user.
# The other output combines the city where the user
# grew and his/her pet which become the user's pet's city.

from cities_in_md import city_you_grew_up,city_you_grew
from your_pet import pets,your_pet

print(city_you_grew_up(city_you_grew))
print(pets(your_pet))
print("Your pet's city name is:\n" + city_you_grew_up(city_you_grew) + pets(your_pet))







   

