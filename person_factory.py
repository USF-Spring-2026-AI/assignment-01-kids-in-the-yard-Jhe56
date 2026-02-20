# Partnered with Ryan from 362 to follow along an outline of the project recommended by chatgpt
from person import Person
from pandas import read_csv
import random

#gpt recommends person factory
class Person_Factory:
    #init is basically read files
    def __init__(self):
        self.fn = read_csv('first_names.csv')
        self.ln = read_csv('last_names.csv')
        self.le = read_csv('life_expectancy.csv')
        self.bmr = read_csv('birth_and_marriage_rates.csv')
        self.gnp = read_csv('gender_name_probability.csv')
        #fix for find last name: recommended by gpt
        self.rtp = read_csv('rank_to_probability.csv', header=None)

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
            
    def find_last_name(self,decade):
        r = random()
        ln_arr = self.ln[self.ln["Decade"] == decade]

        #two lines offered by gpt
        arr = self.rtp.iloc[0].to_numpy()
        total_prob = arr.sum()

        cumulative_sum = 0;
        for i in range (len(arr)):
            cumulative_sum += (arr[i]/total_prob)
            if r < cumulative_sum:
                #gpt helped with iloc
                return ln_arr.iloc[i]["LastName"]

    def has_children(self, decade):
        r = random.randint(0,1)
        base_children = self.bmr[self.bmr["decade"] == decade]["birth_rate"].values[0]
        if r == 1:
            return round(base_children+1.5)
        return round(base_children-1.5)
    
    def is_married(self, decade):
        r = random()
        marriage_rate = self.bmr[self.bmr["decade"] == decade]["marriage_rate"].values[0]
        if r >= marriage_rate:
            #we can redefine the successor's spouse later.
            return Person()
        return None

    #chatgpt gave me a version I based this off of, that used randint instead of random.randint
    #at the same time it's method of getting expected life span was kind of meh
    def life_expectancy(self, birth_year):
        expected = self.le[self.le["Year"] == birth_year]["Period life expectancy at birth"].values[0]
        r = random.randint(0,1)

        if r == 1:
            return int(birth_year + (expected + 10))
        
        return int(birth_year + (expected - 10))

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
            np.set_last_name(self.find_last_name(decade_index))
            #get life expectancy
            np.set_year_died(self.life_expectancy(year_born))
            #we can later assert that the spouse person is married to the successor
            np.set_birth_year(year_born)
            return np

        np.set_first_name(self.find_name(decade_index, np.get_gender()))
        np.set_last_name(ln_arg)
        np.set_year_died(self.life_expectancy(year_born))
        np.set_birth_year(year_born)
        np.set_children(decade_index)
        np.set_spouse(decade_index)
        return np

test_factory = Person_Factory()

print(test_factory.has_children("1950s"))