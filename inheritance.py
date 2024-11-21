# inheritance(kalıtım) = miras alma
class Person():
    def __init__(self, fname, lname) :
        self.firstName = fname
        self.lastName = lname
        print("Person created.")
    def who_am_i(self):
        print("I am a person")
    def eat(self):
        print("I am eating")

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print("Student created.")
    def who_am_i(self):   # aynı isimdeki metot temel sınıftaki medtodu ezer
        print("I am a student")  # buna override denir

p1 = Person("Ali", "Yilmaz")
s1 = Student("Cinar", "Turan", 2210)
print(p1.firstName + " " + p1.lastName)
print(s1.firstName + " " + s1.lastName + " " + str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
