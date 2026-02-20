# Partnered with Ryan from 362 to follow along an outline of the project recommended by chatgpt
from person import Person
from pandas import read_csv

#gpt recommends person factory
class Person_factory:
    #init is basically read files
    def __init__(self):
        #print(fn['name'][0]) -- for legal reference
        self.fn = read_csv('first_names.csv')
        self.ln = read_csv('last_names.csv')

        #we get le (life expectancy) from: birth year through life expectancy + birth year
        self.le = read_csv('life_expectancy.csv')

        self.bmr = read_csv('birth_and_marriage_rates.csv')
        self.gnp = read_csv('gender_name_probability.csv')
        self.rtp = read_csv('rank_to_probability.csv')
        
        return self
    
    #Ryan's method: str(year_born/10) + "0s"
    #child, generate married or not, generate spouse
    #took a few rereads to understand this is generating a spouse for our first two people's children
    def get_person(year_born, ln_arg):
        #np for new person
        np = Person()
        np.set_birth_year(year_born)

        decade_index = str(year_born/10) + "0s"
        


        #also child-rearing rate is determined by decade not by marrital status
        #define the number of children by the successor (adult child's statistic)
        #the spouse can be accessory
        
        #joint realization: empty ln_arg -- takes a random last name
        #rather than inherited last name
        pass