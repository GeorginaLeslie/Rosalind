# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def run():
    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.
    nth_term = input("Please enter the Nth term you want the answer for : ")
    pair_number = input("Please enter the number of pairs per litter: ")
    count = 0
    total = 1
    next_offspring = 1*pair_number

    while count != nth_term-2:
        repro = total
        current_offspring = next_offspring
        next_offspring = repro * pair_number
        total = current_offspring + repro
        count = count+1
        print(total)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
