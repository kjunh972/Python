ls = list()

for i in range(0,10) :
    num = int(input("0~9까지의 숫자를 입력해주세요 : "))
    ls.append(num)

compare = set(ls)

if (len(ls)==len(compare)) :
    print("false")
else :
    print("true")