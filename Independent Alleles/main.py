# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    import math
    k = 2  # Number of generations
    N = 1  # Number of successes
    P = 2 ** k  # Population of given generation k^2
    probability = 0
    for i in range(N, P + 1):
        prob = (math.factorial(P) /
                (math.factorial(i) * math.factorial(P - i))) * (0.25 ** i) * (0.75 ** (P - i))
        probability += prob
    print(probability)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
