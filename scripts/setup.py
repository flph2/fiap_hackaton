import pandas as pd
dataset1 = pd.read_csv('data/Dataset-1.csv')
dataset2 = pd.read_csv('data/Dataset-2.csv')
dataset3 = pd.read_csv('data/Dataset-3.csv')

print(dataset1.columns)
print(dataset2.columns)
print(dataset3.columns)