# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import random
import numpy as np
import plotly.graph_objects as go

def predictMonthlyInputGrowth(initAmount, monthlySalaryInput, monthlygrowthrate, lastMonths):
    # Use a breakpoint in the code line below to debug your script.
    totalValue = initAmount
    for i in range(1, lastMonths + 1):
        totalValue = (totalValue +  monthlySalaryInput) * (1 + monthlygrowthrate)
        print("keep doing monthly investment after " +  str(i) + " month " + "you will get " + str(totalValue) + " cad !!! \n")

    totalValue1 = initAmount
    for i in range(1, lastMonths + 1):
        totalValue1 = totalValue1 + monthlySalaryInput
    
    print("but if you dont do any invest, you will get :", str(totalValue1))    


# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.show()

xTradeLabel = []
yTradeLabel = []
yTradeRealGainLabel = []

xSavingLabel = []
ySavingLabel = []

def predictDailyIncrementalGrowth(initAmount, biweeklySalary, tradingGrowthRate, tradingLossRate, gainingPossibility, lastdays, dayTradeTimes = 0):

    '''

    :param initAmount:   the amount of money initially put inside the account
    :param biweeklySalary:  how much month put into the account every two weeks
    :param tradingGrowthRate:  the total portfolio growth after each trade
    :param tradingLossRate:    the total portfolio loss after each trade
    :param gainingPossibility:   the possibility each time the bot check the market price the price is (1 + tradingGrowthRate) times higher than  before
    :param lastdays:   how many days the bot has been doing trading
    :param dayTradeTimes: how many days the bot doing trade in a 24hour day
    :return:
    '''

    totalValue = initAmount
    for i in range(1, lastdays + 1):
        if i % 15 == 0: # pay day, add salary
            totalValue = totalValue + biweeklySalary

        for j in range(1, dayTradeTimes + 1):
            # todo: add chances, percentage xxx gain money, xxx chance to lost money

            if random.random() < gainingPossibility:   # the possibility we will gain from trading
                totalValue = totalValue * (1 + tradingGrowthRate)
                xTradeLabel.append("day" + str(i) + " trade " + str(j))
                yTradeLabel.append(totalValue)
                # yTradeRealGainLabel.append(totalValue)
                print("this is day " + str(i) + "day win trade " + str(j) + " we have " + str(
                    totalValue) + " increment \n")
            else:
                # totalValue = totalValueue * (1 - dailyLossRate)
                xTradeLabel.append("day" + str(i) + " trade " + str(j))
                yTradeLabel.append(totalValue)

                # print("this is day " + str(i) + "day loss trade " + str(j) + " we have " + str(
                #     totalValue) + " increment \n")

    totalValue1 = initAmount
    for i in range(1, lastdays + 1):

        totalValue1 = totalValue1 * np.power(1.01, (1/365))

        if i % 15 == 0:
            totalValue1 = totalValue1 + biweeklySalary
        for j in range(1, dayTradeTimes + 1):
            xSavingLabel.append("day" + str(i) + " trade " + str(j))
            ySavingLabel.append(totalValue1)
    
    print("but if you dont do any invest only put it into saving account , you will get :", str(totalValue1))


def printGraph(xTradeLabel, yTradeLabel, xSavingLabel, ySavingLabel):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=xTradeLabel, y=yTradeLabel,
                             mode='lines+markers',
                             name='doing day trade'))

    fig.add_trace(go.Scatter(x=xSavingLabel, y=ySavingLabel,
                             mode='lines+markers',
                             name='pure saving'))

    fig.show()

def chanceToGainMoney():
    return 0.8


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # predictMonthlyInputGrowth(initAmount = 9100, monthlySalaryInput = 2400 , monthlygrowthrate = 0.03, lastMonths = 53)
    predictDailyIncrementalGrowth(initAmount = 1000, biweeklySalary = 800, tradingGrowthRate= 0.001, tradingLossRate= 0.01, gainingPossibility = 0.001, lastdays =30 * 12 * 15, dayTradeTimes = 24 * 30)

    printGraph(xTradeLabel, yTradeLabel, xSavingLabel, ySavingLabel)
