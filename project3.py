e = 0
while(1):
    a,b,c,d,l1,e = 0,0,0,0,[],e + 1
    l1.append(input())
    if l1[0] != 'z':
        for i in range (0,4):l1.append(input())
        mov = list(input())
        for i in range(0,5):l1[i] = [x for x in l1[i]]
        for i in range(0,5):
            if ' ' in l1[i]:
                pos,index = l1[i].index(' '),i
        for i in range(len(mov)):
            if mov[i] == 'A':
                if index == 0:
                    a += 1
                    print('this puzzle has no final configuration')
                    break
                else:l1[index][pos],l1[index-1][pos],index = l1[index-1][pos],l1[index][pos],index - 1
            if mov[i] == 'B':
                if index == 4:
                    b += 1
                    print('this puzzle has no final configuration')
                    break
                else:l1[index][pos],l1[index+1][pos],index = l1[index+1][pos],l1[index][pos],index + 1
            if mov[i] == 'R':
                if pos == 4:
                    c += 1
                    print('this puzzle has no configuration')
                    break
                else:l1[index][pos],l1[index][pos+1],pos = l1[index][pos+1],l1[index][pos],pos + 1
            if mov[i] == 'L':
                if pos == 0:
                    d += 1
                    print('this puzzle has no configuration')
                    break
                else:l1[index][pos],l1[index][pos-1],pos = l1[index][pos-1],l1[index][pos],pos - 1
    else:
        exit()
    if a is 0 and b is 0 and c is 0 and d is 0:
        print('puzzle #',e)
        for i in l1:
            for j in i:
                print(j,end = ' ')
            print('\n')
