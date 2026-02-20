# Partnered with Ryan from 362 to follow along an outline of the project recommended by chatgpt
from person import Person
from pandas import read_csv
from random import random

#gpt recommends person factory
class Person_Factory:
    #init is basically read files
    def __init__(self):
        self.fn = read_csv('first_names.csv')
        self.ln = read_csv('last_names.csv')
        self.le = read_csv('life_expectancy.csv')
        self.bmr = read_csv('birth_and_marriage_rates.csv')
        self.gnp = read_csv('gender_name_probability.csv')
        self.rtp = read_csv('rank_to_probability.csv')

    #chatgpt recommended implementing a cumulative sum iterator 
    def find_name(self,decade,gender):
        r = random()

        #this ln below was pulled from gpt suggestion
        subset = self.fn[(self.fn["decade"] == decade) & (self.fn["gender"] == gender)]

        probability = subset["frequency"].cumsum()
        names = subset["name"]
        for i in range (len(probability)):
            if r < probability[i]:
                return names[i]

    #so each of these functions are going to be expected to come from a Person_Factory instance
    def get_person(self,year_born, ln_arg):
        #np for new person
        np = Person()
        np.set_birth_year(year_born)

        #defaults for all people, year born, decade born, randomized gender
        decade_index = str(year_born/10) + "0s"

        #gender rng borrowed from google gemini
        #person class has female defaulted for the gender
        rand = random.randint(0,1)
        if rand == 1:
            np.set_gender("male")

        #if the last name is empty then we're making a spouse
        if len(ln_arg) == 0:
            #set first name
            np.set_first_name(self.find_name(decade_index, np.get_gender()))
            #get last name

            #get life expectancy
            #get rank probability
            return np

        #also child-rearing rate is determined by decade not by marrital status
        #define the number of children by the successor (adult child's statistic)
        #the spouse can be accessory
        pass

test_factory = Person_Factory()
print(test_factory.rtp)