# Partnered with Ryan from 362 to follow along an outline of the project recommended by chatgpt
from person import Person
from pandas import read_csv

#gpt recommends person factory
class Person_factory:

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