while(1):
    r = int(input())
    if r != 0:
        c = int(input())
        l1 = []
        for i in range(0,r):
            l1.append(input())
    else:
        exit()
    print('Across')   
    for i in l1:
        i = i.split('*')
        while '' in i:
            i.remove('')
        for j in i:
            print(  j)
    print('Down')
    s = "".join(map(str,[i[j] for j in range(0,c) for i in l1]))
    for i in range(len(s)):
        l1 = s[r*i:r*(i+1)]
        l1 = l1.split('*')
        while '' in l1:
            l1.remove('')
        for j in l1:
            print(  j)

