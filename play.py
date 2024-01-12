# This is an exercise I completed from udemy.
# This project demosntrate the use of inheritance.
# "NPC" (which stands for Non-Player Character) that 
# inherits from Character,and has an additional 
# instance method called speak  which prints the speech 
# that character would say when a player interacts with them. 

class Character:
    def __init__(self,name,hp,level):
        self.name = name
        self.hp = hp
        self.level = level

# NPC is Non Player Character
class NPC(Character):
    def __init__(self,name,hp,level):
        super().__init__(name,hp,level)
       
    def speak(self):
        return f"{self.name} say: I heard there were monsters running around last night!"

villager = NPC("Bob",100,12)
print(villager.name)
print(villager.hp)
print(villager.level)
print(villager.speak())