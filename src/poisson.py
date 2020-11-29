# Poisson Probability Distribution

'''

Probability Distribution of a Poisson random variable x, representing the number of successes occuring in a 
given time interval or a specified region of space is given by the formula:

                                                                    P(x) = ((e ** µ) * (µ ** x)) / x!

                                                Where:

                                                    x = 0,1,2,3,......
                                                    e = 2.71828 (But use your calculators e button)
                                                    µ = mean number of successes in the given time interval or region of space

                                                    E(x) = µ

                                                    V(x) = o ** 2 = µ

'''

# Synthesizing Poisson

from math import e


def factorial(k):

    fact = 1
    for i in range(1, k + 1):
        fact *= i
    return fact


def poisson(lamb, k):
    return e ** (-lamb) * lamb ** k / factorial(k)

print(poisson(10, 11))


# Analyze:

def poisson_dict(lamb, low_k, high_k):
    
    d = {}
    for k in range(low_k, high_k + 1):
        d[k] = poisson(lamb, k)
    return d

for k, v in poisson_dict(4, low_k = 0, high_k = 30).items():
    print(f'{k}: {v}')