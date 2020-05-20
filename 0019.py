#PROBLEM 19 – Counting Sundays
"""
You are given the following information, but you may prefer to do some research for yourself.

* 1 Jan 1900 was a Monday.
* Thirty days has September, April, June and November.
* All the rest have thirty-one,
* Saving February alone, Which has twenty-eight, rain or shine. And on leap years, twenty-nine.
* A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def isLeap(year):
    if (year % 100 == 0) and (year % 400 == 0):
        return True
    elif (year % 100 == 0):
        return False
    elif (year % 4 == 0):
        return True
    else:
        return False

    
months = [(1, 31),(2, 28),(3, 31),(4, 30),(5, 31),(6, 30),(7, 31),(8, 31),(9, 30),(10, 31),(11, 30),(12, 31)]
monthsL = [(1, 31),(2, 29),(3, 31),(4, 30),(5, 31),(6, 30),(7, 31),(8, 31),(9, 30),(10, 31),(11, 30),(12, 31)]
day = {1:'monday', 2:'tuesday', 3:'wednesday', 4:'thursday', 5:'friday', 6:'saturday', 0:'sunday'}
 
 
counter = 0
year = 1901
start = 2

for i in range(100):
    for i in range(12):
        if day[start % 7] == 'sunday':
            counter += 1
        if isLeap(year):
            start += monthsL[i][1]
        else:
            start += months[i][1]
            
        year += 1
        
print(counter)