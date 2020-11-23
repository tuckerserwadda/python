# object oriented programming
# classes, methods, objects 
class family:
    def __init__(self, name, male, female ):
        self.name = name
        self.male = male
        self.female = female

    
    def shout(self):
        print(f'my family is {self.name} has {self.male} male and {self.female} female')
        return ""
# family subclass

class member(family):
    def __init__(self, name, male, female, fname, lname, weight,height, gender):
        super().__init__(name, male, female)
        self.fname = fname
        self.lname = lname
        self.weight = weight
        self.height = height
        self.gender = gender 
    def fullname(self):
        return self.fname + " " + self.lname


person1 = member("kateregga", 6, 7, "tucker", "serwadda", 200, 5.7, "male")
print(person1.shout() + "and am " + person1.fullname())

class farm:
    def __init__(self, list= []):
        self.list = []
    def add(self, value):
        return self.list.append(value)

farm1 = farm(list)
farm1.add(3)
print(farm1.list)
