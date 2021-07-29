from collections import Counter
for i in range(int(input())):
    o = input()
    c = []
    d = dict(Counter(o))
    for e in d.values():
        c.append(e)
    c.sort()
    if len(c)<3:
        print("Dynamic")
    else:
        if c[-1] != c[-2]+c[-3]:
            print("Not")
        else:
            print("Dynamic")