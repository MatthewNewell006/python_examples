import pandas as pd
import numpy as np

from collections import Counter
from itertools import repeat, chain
from random import randint, choice


powerball_df = pd.read_csv('/Users/matthewnewell/Desktop/github/python_examples/csv/NCELPowerball.csv')

print(powerball_df.head(5))
print('\n')


reversed_df = powerball_df.sort_index(ascending = False)

print(reversed_df.head(5))
print('\n')

print(reversed_df.iloc[0])
print('\n')

reversed_df.drop(reversed_df.index[:1], inplace = True)
print(reversed_df.head(5))
print('\n')

print(reversed_df.columns)
print('\n')

n1 = Counter(reversed_df['Number 1']).most_common(20)
n2 = Counter(reversed_df['Number 2']).most_common(20)
n3 = Counter(reversed_df['Number 3']).most_common(20)
n4 = Counter(reversed_df['Number 4']).most_common(20)
n5 = Counter(reversed_df['Number 5']).most_common(20)

pball = Counter(reversed_df['Powerball']).most_common(20)

top_numbers = n1 + n2 + n3 + n4 + n5
most = [i[0] for i in top_numbers]

print(Counter(most).most_common(20))
print('\n')

nums_chosen = sorted([int(choice(most)) for i in range(5)])
pball = (choice(pball))

print(nums_chosen, int(pball[0]))
