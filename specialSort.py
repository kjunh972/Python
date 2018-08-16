'''정렬이 되고 난 후, 음의 정수는 앞쪽에 양의정수는 뒷쪽에 있어야 한다.
또한 양의정수와 음의정수의 순서에는 변함이 없어야 한다.'''

import random

ls = list()

for i in range(0,6) :
    ls.append(random.randrange(-10, 11))

print("정렬전 : ",ls)

print("정렬후 : ",end="")
for i in range(0,3) :
    for k in range(0,6) :
        if (i==0) :
            if (ls[k]<0) :
                print(ls[k],end="   ")
        elif (i==1) :
            if (ls[k]==0) :
                print(ls[k],end="   ")
        else :
            if (ls[k]>0) :
                print(ls[k],end="   ")

print()