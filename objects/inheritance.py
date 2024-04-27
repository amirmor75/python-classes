class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):

    def __init__(self, fname, lname):
        course_list = ['python','JAVA']
        Person.__init__(self, fname, lname)
  
if __name__ == '__main__':
    p1 = Person('Amir','Mor')
    p1.printname()
    s1 = Student('Ilay','Iluz')
    s1.printname()
      