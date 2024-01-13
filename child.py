# This is another udemy mini project.
# In this project it demonstrate the
# use of multiple inheritance. In this
# app the child inherit some of the traits
# of the parents. Some of these trait are:
# eye color, hair color, and hair type.
# the child inherit most of the traits from
# the mother.

class Mother:
    def __init__(self,eye,hcolor,htype):
        self.eye = eye
        self.hcolor = hcolor
        self.htype = htype
        
    def eye_color(self):
        return f"eye color is {self.eye}"
    
    def hair_color(self):
        return f"hair color is {self.hcolor}"
    
    def hair_type(self):
        return f"hair type is {self.htype}"

class Father:
    def __init__(self,eye,hcolor,htype):
        self.eye = eye
        self.hcolor = hcolor
        self.htype = htype
    
    def eye_color(self):
        return f"f eye color is {self.eye}"
    
    def hair_color(self):
        return f"f hair color is {self.hcolor}"
    
    def hair_type(self):
        return f"f hair type is {self.htype}"

class Child(Mother,Father):
    def __init__(self,eye,hcolor,htype):
        super().__init__(eye,hcolor,htype)

eye_color =  Child("brown","dark brown","curly")
print(eye_color.eye_color())
    

