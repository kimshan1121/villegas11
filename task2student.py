class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, my name is {self.name}. I'm {self.age} years old and my program is {self.course}.")

# Create three student objects
student1 = Student("Kimberly Villegas", 19, "Information Technology")
student2 = Student("Ashly Cajusay", 20, "Information Technology")
student3 = Student("James Andrew", 23, "Information Technology")

# Call the introduce method for each student
student1.introduce()
student2.introduce()
student3.introduce()
