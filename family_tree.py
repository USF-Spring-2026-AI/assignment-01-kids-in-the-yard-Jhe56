from person import Person
from person_factory import Person_Factory
from queue import Queue
from collections import defaultdict

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
            years_apart = 20
            if children_num > 0:
                years_apart = int(20/children_num)

            #vsco-pilot generated loop
            for i in range(children_num):
                if p_25_yo + (i*years_apart) > self.end_year:
                    continue
                else:
                    child = self.factory.get_person(p_25_yo + (i*years_apart), p.get_last_name())
                    #only enqueue the child for processing if they're born before the end year
                    tree_queue.put(child)

                #add the child to the parents
                p.add_child(child)
                if p_spouse != None:
                    p_spouse.add_child(child)

    #drafted by vscode, refined with chatgpt to consider the spouse
    def count_people(self):
        count_queue = Queue()
        count_queue.put(self.MJ)
        count_queue.put(self.DJ)
        
        #chatgpt uses visited, a set to keep track of the id() of each person
        visited = set()
        count = 0
        while count_queue.empty() == False:
            p = count_queue.get()
            
            #checks if the id of the person is in visited
            if id(p) in visited:
                continue
            visited.add(id(p))

            if p.get_spouse() != None:
                count_queue.put(p.get_spouse())

            for c in p.get_children():
                count_queue.put(c)
            count += 1
        return count

    #gpt generated
    def decade_count(self):
        count_queue = Queue()
        count_queue.put(self.MJ)
        count_queue.put(self.DJ)

        visited = set()
        decade_counts = defaultdict(int)

        while not count_queue.empty():
            p = count_queue.get()

            # prevent double counting (important if spouses reference each other)
            if id(p) in visited:
                continue
            visited.add(id(p))

            # compute decade
            birth_year = p.get_birth_year()
            decade = (birth_year // 10) * 10
            decade_counts[decade] += 1

            # enqueue children
            for c in p.get_children():
                count_queue.put(c)
            
            #added spouse
            if p.get_spouse() != None:
                count_queue.put(p.get_spouse())

        # print sorted decades
        for decade in sorted(decade_counts.keys()):
            print(f"{decade}: {decade_counts[decade]}")

    #drafted by vscode, refined with chatgpt to consider the spouse
    def duplicate_names(self):
        count_queue = Queue()
        count_queue.put(self.MJ)
        count_queue.put(self.DJ)

        visited = set()
        names = set()
        duplicates = set()

        while count_queue.empty() == False:
            p = count_queue.get()

            #checks if the id of the person is in visited
            if id(p) in visited:
                continue
            visited.add(id(p))

            for c in p.get_children():
                count_queue.put(c)

            if p.get_spouse() != None:
                count_queue.put(p.get_spouse())

            name_tuple = (p.get_first_name(), p.get_last_name())

            if name_tuple in names:
                duplicates.add(name_tuple)
            else:
                names.add(name_tuple)
        
        for t in duplicates:
            print(t[0],t[1])

    def __init__(self):
        self.factory = Person_Factory()
        self.make_jones()

        self.end_year = 2120
        self.people_queue = Queue()

        self.people_queue.put(self.MJ)

        self.run_queue(self.people_queue)
    
Family_Tree_Instance = Family_Tree()
while True:
    cmd = input("Are you interested in: \n (T)otal people in the family tree \n (D)ecade count \n (N)ame duplicates \n (Q)uit \n")
    if cmd == "T":
        print("Total people in the family tree: ", Family_Tree_Instance.count_people())
    elif cmd == "D":
        Family_Tree_Instance.decade_count()
    elif cmd == "N":
        Family_Tree_Instance.duplicate_names()
    elif cmd == "Q":
        break

