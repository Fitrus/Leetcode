r = dict()
r = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
s = input("Roman Digits: ")   
roman = 0
prev_value = 0

for i in s:
    value = r[i]
    if prev_value < value:
        roman = roman + (value - 2 * prev_value)
    else:
        roman = roman + value
    prev_value = value

print(roman)



              