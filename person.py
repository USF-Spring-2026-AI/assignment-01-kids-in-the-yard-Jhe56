class person:
    birth_year = 0000
    year_died = 0000
    first_name = "jane"
    last_name = "doe"
    gender = "f"

    #other persons
    spouse = None
    children = []

    #probably could've reduced some of this to a single init func
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
    
    def add_child(self, smallPerson):
        self.children.append(smallPerson)
    def get_children(self):
        return self.children