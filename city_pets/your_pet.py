pet = ["dog", "cat", "fish", "iguana", "racoon", "squirel", "pig", "spider"]

mypet = input("What pet do you have? ")
your_pet = mypet.lower()

def pets(your_pet):
    if your_pet == "dog":
        return f"{pet[0]}"
    elif your_pet == "cat":
        return f"{pet[1]}"
    elif your_pet == "fish":
        return f"{pet[2]}"
    elif your_pet == "iguana":
        return f"{pet[3]}"
    elif your_pet == "racoon":
        return f"{pet[4]}"
    elif your_pet == "squirel":
        return f"{pet[5]}"
    elif your_pet == "pig":
        return f"{pet[6]}"
    elif your_pet == "spider":
        return f"your pet is a {pet[7]}"
    return "Pet is not in the list"
        