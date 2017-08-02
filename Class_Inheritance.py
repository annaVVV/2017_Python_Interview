class Person(object):
    def __init__(self, name):
        self.name = name
    def reveal_identity(self):
        print "My name is {}".format(self.name)

class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name

    def reveal_identity(self):
        super(SuperHero,self).reveal_identity()
        print " ... And I am {}".format(self.hero_name)

class Person:

    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age

    def __str__(self):
        return self.firstname + " " + self.lastname + ", " + str(self.age)

class Employee(Person):

    def __init__(self, first, last, age, staffnum):
        Person.__init__(self, first, last, age)
        # super().__init__(first, last, age)
        self.staffnumber = staffnum

    def __str__(self):
        #return super().__str__() + ", " +  self.staffnumber
        return Person.__str__(self) + ", " +  self.staffnumber



def main():
    x = Person("Marge", "Simpson", 36)
    y = Employee("Homer", "Simpson", 28, "1007")
    print x
    print y

if __name__ == "__main__":
    main()

# Output:
# Marge Simpson, 36
# Homer Simpson, 28, 1007

#chel = Person("Mike")
#chel.reveal_identity()

# ss = SuperHero("Mike", "DDDDD")
# ss.reveal_identity()
# Output:
# My name is Mike
#  ... And I am DDDDD
