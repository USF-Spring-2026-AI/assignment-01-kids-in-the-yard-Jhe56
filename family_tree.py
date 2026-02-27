from person import Person
from person_factory import Person_Factory
import queue

class Family_Tree:

    #create our initial couple
    def make_jones(self):
        #Desmond Jones
        self.DJ = Person()
        self.DJ.set_gender("male")
        self.DJ.set_first_name("Desmond")
        self.DJ.set_last_name("Jones")
        self.DJ.set_birth_year(1950)
        self.DJ.set_year_died(self.factory.life_expectancy)
        self.DJ.set_children(self.factory.has_children)

        #Molly Jones
        self.MJ = Person()
        self.MJ.set_gender("female")
        self.MJ.set_first_name("Molly")
        self.MJ.set_last_name("Jones")
        self.MJ.set_birth_year(1950)
        self.MJ.set_year_died(self.factory.life_expectancy)
        self.MJ.set_children(self.factory.has_children)

        self.DJ.set_spouse(self.MJ)
        self.MJ.set_spouse(self.DJ)

    def process_queue(tree_queue):
        # while tree_queue != 
        pass

    def __init__(self):
        self.factory = Person_Factory()
        self.make_jones()

        self.end_year = 2120
        self.people_queue = queue()


# class test:
# 	def __init__(self):
#             self.name = "molly"
        
# q = queue.Queue()
# new_person = test()

# q.put(new_person)
# q.put(new_person)
# q.put(new_person)

#copilot this makes no sense...
# while q.empty() == False:
#     p_holder = q.get()
#     print(p_holder.name)
