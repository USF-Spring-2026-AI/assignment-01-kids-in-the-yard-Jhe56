# Partnered with Ryan from 362 to follow along an outline of the project recommended by chatgpt
from person import person
from pandas import read_csv

df = read_csv('first_names.csv')

print(df['name'])