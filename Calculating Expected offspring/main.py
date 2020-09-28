# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.
    values = open("rosalind_iev.txt", "r")
    sep_values = values.read().split()

    a = int(sep_values[0])
    b = int(sep_values[1])
    c = int(sep_values[2])
    d = int(sep_values[3])
    e = int(sep_values[4])
    f = int(sep_values[5])

    total_calc = (a * 2 * 1) + (b * 2 * 1) + (c * 2 * 1) + (d * 2 * 0.75) + (e * 2 * 0.5) + (f * 2 * 0)
    print(total_calc)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
