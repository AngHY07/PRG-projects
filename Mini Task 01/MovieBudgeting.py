# Ang Hao Yi (10273989D)
import math 

movietickets = float(input("Enter the number of movie ticket: "))
snacks= float(input("Enter the number of snacks: "))
drinks = float(input("Enter the number of drinks: "))

costmovie = movietickets*12
costsnacks = snacks* 2.5
costdrinks = drinks*1.8

totalCostBeforeTax = costmovie + costsnacks + costdrinks
totalCostAfterTax = totalCostBeforeTax + (totalCostBeforeTax*0.1)

print("Total cost of the purchase before service fee is ${:.2f}".format(math.ceil(totalCostBeforeTax*10)/10))
print("Total cost of the purchase is ${:.2f}".format(math.ceil(totalCostAfterTax*10)/10))