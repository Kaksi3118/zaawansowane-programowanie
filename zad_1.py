class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if not self.marks:
            return False
        average = sum(self.marks) / len(self.marks)
        return average > 50

student1 = Student("Alice", [60, 70, 80]) 
student2 = Student("Bob", [40, 30, 20])    

print(student1.is_passed())
print(student2.is_passed())