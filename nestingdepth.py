t = int(input())

for r in range(t):
    s = list(input())
    temp = s

    res = ""
    a = []
    av = 0
    for i in temp:
        x = int(i)
        while av > x:
            a.append(")")
            av -= 1
        if av == 0:
            while x:
                a.append("(")
                x -= 1
                av += 1
        if av < x:
            while x > av:
                a.append("(")
                av += 1
        a.append(i)
    while(av):
        a.append(")")
        av -= 1
    print("Case #" + str(r + 1) + ":", ''.join(a))
