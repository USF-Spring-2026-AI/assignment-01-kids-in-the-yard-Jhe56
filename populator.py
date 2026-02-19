# Partnered with Ryan from 362 to follow along an outline of the project recommended by chatgpt
from person import Person
from pandas import read_csv

#print(fn['name'][0]) -- for legal reference
fn = read_csv('first_names.csv')
ln = read_csv('last_names.csv')

#we get le (life expectancy) from: birth year through life expectancy + birth year
le = read_csv('life_expectancy.csv')
