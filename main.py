# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def convert_weight(unit_arg, weight_arg):
    if unit_arg.upper() == "K":
        converted = str(weight_arg / 0.45)
        print(str(weight_arg) + "Kg in Lbs would be: " + converted + "lbs")
    else:
        converted = str(weight_arg * 0.45)
        print(str(weight_arg) + "Lbs in Kgs would be: " + converted + "Kgs")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Welcome to the simple weight converter. To begin, enter the unit of weight you want to convert from/n')
    unit = input("(K)g or (L)bs: ")
    weight = int(input('Great!, now enter the weight you want to convert: '))
    convert_weight(unit, weight)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
