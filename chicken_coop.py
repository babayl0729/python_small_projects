# We want to keep track of how many eggs 
# each individual Chicken lays, and at the 
# same time we want to track the total 
# number of eggs all hens have laid. 

class Chicken:
    total_eggs = 0
    def __init__(self,species,name):
        self.species = species
        self.name = name
        self.egg = 0

    def lay_egg(self):
        self.egg += 1
        Chicken.total_eggs += 1
        return self.egg

c1 = Chicken("Al ice", "Partridge Silkie")
c2 = Chicken("Amelia", "Speckle d Sussex")

print(c1.name, c1. species, c1.egg)
print(c2.name, c2. species, c2.egg)

print(Chicken.total_eggs)
print(c1.lay_egg())
print(Chicken.total_eggs)
print(c2.lay_egg())
print(c2.lay_egg())
print(Chicken.total_eggs)

