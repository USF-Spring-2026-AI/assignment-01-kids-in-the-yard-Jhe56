from person import Person
from person_factory import Person_Factory
from queue import Queue

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
        self.MJ.set_children(self.factory.has_children("1950s"))

        self.DJ.set_spouse(self.MJ)
        self.MJ.set_spouse(self.DJ)

    def run_queue (self, tree_queue):
        while tree_queue.empty() == False:
            #we get a parent from the queue
            p = tree_queue.get()
            p_spouse = p.get_spouse()
            p_25_yo = p.get_birth_year() + 25

            children_num = p.get_number_of_children()
            print("Number of children: ", children_num)
            years_apart = int(20/children_num)
           
            #vsco-pilot generated loop
            for i in range(children_num):
                if p_25_yo + (i*years_apart) > self.end_year:
                    child = self.factory.get_person(self.end_year, p.get_last_name())
                else:
                    child = self.factory.get_person(p_25_yo + (i*years_apart), p.get_last_name())
                    #only enqueue the child for processing if they're born before the end year
                    tree_queue.put(child)

                #add the child to the parents
                p.add_child(child)
                if p_spouse != None:
                    p_spouse.add_child(child)
            
            print(tree_queue.qsize())

    def __init__(self):
        self.factory = Person_Factory()
        self.make_jones()

        self.end_year = 2120
        self.people_queue = Queue()

        self.people_queue.put(self.MJ)

        self.run_queue(self.people_queue)

my_family_tree = Family_Tree()
my_family_tree.run_queue(my_family_tree.people_queue)