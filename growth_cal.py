# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(monthlySalaryInput, monthlygrowthrate, lastMonths):
    # Use a breakpoint in the code line below to debug your script.
    totalValue = 9100
    for i in range(1, lastMonths + 1):
        totalValue = (totalValue +  monthlySalaryInput) * (1 + monthlygrowthrate)
        print("keep doing monthly investment after " +  str(i) + " month " + "you will get " + str(totalValue) + " cad !!! \n")

    totalValue1 = 9100
    for i in range(1, lastMonths + 1):
        totalValue1 = totalValue1 + monthlySalaryInput
    
    print("but if you dont do any invest, you will get", str(totalValue1))    







# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print_hi(monthlySalaryInput = 2400 , monthlygrowthrate = 0.037, lastMonths = 12 * 6)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
