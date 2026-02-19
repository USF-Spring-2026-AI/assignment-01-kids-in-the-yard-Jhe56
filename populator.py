# Partnered with Ryan from 362 to follow along an outline of the project recommended by chatgpt
from person import person
from pandas import read_csv

first_names = read_csv('first_names.csv')
last_names = read_csv('last_names.csv')

#we get lifespan from: birth year through life expectancy + birth year
life_span = read_csv('life_expectancy.csv')