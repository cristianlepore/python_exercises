from moduleProblem2 import *

# The outstanding balance on the credit card
balance = 5000
# AnnualInterestRate
annualInterestRate = 0.18
# Minimum monthly payment rate as a decimal
monthlyPayment = 10
# Number of months in a year
monthsInAYear = 12

startingBalance = balance
while balance > 0:
    balance = startingBalance
    for i in range(monthsInAYear):
        # Iterate over the months of the year
        monthlyBalance = newMonthlyBalance(balance, annualInterestRate, monthlyPayment)
        balance = monthlyBalance
        i += 1

    if balance > 0:
        monthlyPayment += 10

print("Minimum monthly payment:", end=' ')
print(monthlyPayment)