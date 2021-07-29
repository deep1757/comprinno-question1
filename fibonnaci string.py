from collections import Counter
# for loop to enter input value 
for i in range(int(input())):
    o = input()
#create list to enter values 
    c = []
#create counter to values 
    d = dict(Counter(o))
    for e in d.values():
        c.append(e)
    c.sort()
#if else condition to check values
    if len(c)<3:
        print("Dynamic")
    else:
        if c[-1] != c[-2]+c[-3]:
            print("Not")
        else:
            print("Dynamic")
