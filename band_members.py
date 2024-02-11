class Member:
    def __init__(self,name,instrument,age):
        self.name = name
        self.instrument = instrument
        self.age = age
    
    def __repr__(self):
        return f"{self.name} is in {self.instrument}."
    
    def vox(self,vocals):
        return f"{self.name} also in {vocals}."
    
    def age_gaps(self):
        return f"{self.name} age is {self.age}."

class Rudolf(Member):
    def __init__(self, name, instrument, age,voice):
        super().__init__(name, instrument, age)
        self.voice = voice

    def guitar1(self):
        return f"{self.name} plays the {self.instrument}."
    
    def bk_up(self):
        return f"{self.name} also does the back up {self.voice}."
    
    def age_num1(self):
        return f"{self.name} age is {self.age}"
    
class Fender(Member):
    def __init__(self, name, instrument, age):
        super().__init__(name, instrument,age)
    
    def guitar2(self):
        if self.name == "Fender":
            return f"that's {self.name} and he plays {self.instrument}."
        else:
            print("Not it!")
    
    def age_num2(self):
        if self.age >= 18:
            return f"{self.name} is {self.age} he's allowed to drink!"
        else:
            return f"you're underage! you need an X mark!" 

class Punk(Member):
    def __init__(self, name, instrument, age, influence):
       super().__init__(name,instrument,age)
       self.influence = influence
    
    def lars(self):
        if self.name == "Lars" and self.instrument == "bass":
            return f"it's {self.name} and he has {self.instrument}!"
        return f"Nope! it's not it!"
    
    def influence1(self):
        if self.influence == "post punk" or self.influence == "experimental":
            return f"he like's {self.influence}! he's in!"
        return "You're not the right one!"



rudolf = Rudolf("Rudolf","Guitar",25,"vocals")
print(rudolf.guitar1())

fender = Fender("Fender","Lead Guitar",18)
print(fender.guitar2())
print(fender.age_num2())

larss = Punk("Lars","bass",19,"experimental")
print(larss.lars())
print(larss.influence1())