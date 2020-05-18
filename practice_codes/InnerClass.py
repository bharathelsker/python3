class student:
    school = 'kingston'

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.laptop = self.laptop()

    def show(self):
        print(self.school, self.name, self.rollno)
        self.laptop.show()

    class laptop:
        def __init__(self):
            self.brand = 'amma'
            self.cpu = 'i3'
            self.ram = '4gb'

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = student('bharath', 13)
print(s1.show())
