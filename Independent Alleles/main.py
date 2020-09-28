# coding=utf-8

def alleles():
    import math
    g = 7  # Number of generations
    k = 33  # Number of successes
    n = 2 ** g  # Population of given generation k^2
    probability = 0
    for i in range(k, n + 1):  # This is to work out the sum of all the probabilities
        # criteria (See bottom of code for explanation)
        prob = (math.factorial(n) /
                (math.factorial(i) * math.factorial(n - i))) * (0.25 ** i) * (0.75 ** (n - i))
        probability += prob
    print(probability)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    alleles()
