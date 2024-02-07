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

rudolf = Rudolf("Rudolf","Guitar",25,"vocals")
print(rudolf.guitar1())