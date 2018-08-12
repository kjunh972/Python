ls = list()

while(1) :
    add = input("(그만입력하려면 0을 입력해주세요)입력하세요 : ")
    if (add=="0") :
        break
    else :
        ls.append(add)

for i in range(0,len(ls)) :
        if(ls[i-1]=="_") :
            change = ord(ls[i+1])
        else :
            change = ord(ls[i])
        if (change>=65 and change<=90) :
            if(ls[i-1]=="_") :
                ls.insert(i+1, "_")
            else :
                ls.insert(i, "_")

for i in range(0,len(ls)) :
    print(ls[i]," ",end='')