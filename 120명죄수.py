# 감옥에 120명의 죄수가 있다. 간수는 복도를 120번 동안 다음 조건에 지나간다.

# - 처음에 문은 모두 닫혀 있다.
# - N번째 지나갈 때에는 N의 배수인 문들이 열려 있으면 닫고, 닫혀 있으면 연다.
# - 마지막에 문이 열려 있으면 그 방의 죄수는 석방이다.

# 문제 : 과연 몇 명의 죄수가 석방될까?

# c = close, o = open

prison = list()

cheak = 0

for i in range (120) :
    prison.append("c")

for i in range(1,len(prison)) :
    for k  in range(1,len(prison)) :
        if i*k<120 :
            if prison[i*k] == "c" :
                prison[i*k] = "o"
            elif prison[i*k] == "o" :
                prison[i*k] = "c"


for i in range(0,len(prison)) :
    if (prison[i]=="o") :
        cheak+=1

print(cheak,"명의 죄수가 석방되었습니다.")