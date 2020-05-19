#PROBLEM 17 – Number letter counts
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
ie 456 = four hundred and fifty six = 4 + 7 + 3 + 5 + 3 = 22
"""

def count_letters(number):
    mapping = {0: '', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
    10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
    20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}
    result = 0
    
    if number == 1000:
        return 11
    
    if number > 99:
        # 10^2
        result += len(mapping[number // 100]) + 7
        if (number % 100 == 0):
            return result
        #to further processing
        result += 3
        number = number % 100
    
    if (number > 20):
        # 10^1
        result += (len(mapping[number - (number % 10)]))
        # 10^0
        result += (len(mapping[number % 10]))
    else:
        result += len(mapping[number])
    
    return result
    
x = int(input('enter integer (1 - 1000): '))

counter = 0
for num in range(1, x+1):
    counter += count_letters(num)

print(counter)
