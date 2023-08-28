# clasess

class Person:
    age = dob - datetime.now
    
    def __init__(self, name, dob):
        self.name = name
        self.age = dob 
        
    def speak():
        print("Hello")
        
    def walk():
        print("walking away")
    
    def get_name():
        return name
    
    def get_age():
        return age
    
    
    
class Student(Person):
    courses= []
    
    def get_courses():
        return courses
    
    def speak():
        print("I am tired")
        