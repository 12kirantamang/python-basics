class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks     # changed mark → marks

    def get_avg(self):
        total = 0
        for val in self.marks:
            total += val
        avg = total / len(self.marks)
        print("Hi", self.name, "your avg score is:", avg)

s1 = Student("kiran tamang", [99, 100, 80])
s1.get_avg()
