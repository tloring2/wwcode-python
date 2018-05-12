""" The Challenge
Author:
Description: Aling Nena’s Sari-sari store wants a robot that will ask the
customer their total bill and payment amount and tell them their change
(for now, we can allow negative change).
"""

Bill = input('Total Bill:')
Pay = input('Enter your cash amount:')
Change = float(Pay) - float(Bill)
print("Hi! Your change is Php" + str(Change))