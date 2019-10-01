from moduleProblem1 import *

# The outstanding balance on the credit card
balance = 3329
# AnnualInterestRate
annualInterestRate = 0.2
# Minimum monthly payment rate as a decimal
monthlyPaymentRate = 0.00
# Number of months in a year
monthsInAYear = 12

# Print the information on screen
print("Balance:", end=' ')
print(balance)
print("Annual interest rate:", end=' ')
print(annualInterestRate)
print("Monthly payment rate:", end=' ')
print(monthlyPaymentRate)

for i in range(monthsInAYear):
    monthlyBalance = newMonthlyBalance(balance, annualInterestRate, monthlyPaymentRate)
    balance = monthlyBalance
    i += 1
    print("Month", i, "Remaining balance:", end = ' ')
    print(monthlyBalance)

print("Remaining balance after 1 year:", end=' ')
print(balance)