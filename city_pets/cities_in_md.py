city = ["Rockville", "Germantown", "Gaithersburg", "Frederick", "Boyds",
        "Silver Spring", "Redland", "Montgomery Village", "Dundolf",
        "Baltimore", "California", "Bethesda", "Potomac", "Friendship Heights"]

growingup = input("In which city in MD you grew up? ")
city_you_grew = growingup.lower()

def city_you_grew_up(city_you_grew):
    if city_you_grew == "rockville":
        return f"{city[0]}"
    elif city_you_grew == "germantown":
        return f"{city[1]}"
    elif city_you_grew == "gaithersburg":
        return f"{city[2]}"
    elif city_you_grew == "frederick":
        return f"{city[3]}"
    elif city_you_grew == "boyds":
        return f"{city[4]}"
    elif city_you_grew == "silver spring":
        return f"{city[5]}"
    elif city_you_grew == "redland":
        return f"{city[6]}"
    elif city_you_grew == "montgomery village":
        return f"{city[7]}"
    elif city_you_grew == "dundolf":
        return f"{city[8]}"
    elif city_you_grew == "baltimore":
        return f"{city[9]}"
    elif city_you_grew == "california":
        return f"{city[10]}"
    elif city_you_grew == "bethesda":
        return f"{city[11]}"
    elif city_you_grew == "potomac":
        return f"{city[12]}"
    elif city_you_grew == "friendship heights":
            return f"{city[13]}"
    return "City is not in the list-"
        
    