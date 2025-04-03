class Father:
    def protoctor(self):
        print("i can protect... and i will protect")
    
    def skill(self):
        print("Body Building,Boxing,Nechaku,Cycling")

class Mother:
    def care(self):
        print("I will take care of whole family")
    
    def skill(self):
        print("Cooking,Siging,Guitar,Love,Dance")


class Child(Father,Mother):
    def skill(self):
        Father.skill(self)
        Mother.skill(self)
        print("Multitalented")


c =Child()
c.skill()
