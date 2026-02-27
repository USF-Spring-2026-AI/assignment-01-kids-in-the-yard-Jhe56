class Person:
    def __init__(self):
        self.birth_year = 0
        self.year_died = 0
        self.first_name = "jane/john"
        self.last_name = "doe"
        self.gender = "female"

        #other persons
        self.spouse = None
        self.children = []
        self.num_children = 0

    def set_gender(self, g):
        self.gender = g
    def get_gender(self):
        return self.gender

    def set_first_name(self, firstName):
        self.first_name = firstName
    def get_first_name(self):
        return self.first_name

    def set_last_name(self, lastName):
        self.last_name = lastName
    def get_last_name(self):
        return self.last_name
    
    def set_birth_year(self, birthYear):
        self.birth_year = birthYear
    def get_birth_year(self):
        return self.birth_year
    
    def set_year_died(self, yearDied):
        self.year_died = yearDied
    def get_year_died(self):
        return self.year_died
    
    def set_spouse(self, otherPerson):
        self.spouse = otherPerson
    def get_spouse(self):
        return self.spouse
    
    def set_children(self, number):
        self.num_children = number
    def get_number_of_children(self):
        return self.num_children
    def add_child(self, smallPerson):
        self.children.append(smallPerson)
    def get_children(self):
        return self.children