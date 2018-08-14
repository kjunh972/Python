mult = 0
plus = 0

print("100 미만으로 적어주세요.")
start = int(input("시작점을 정해주세요 : "))
end = int(input("끝점을 정해주세요 : "))

while(1) :
    if (start>=100) :
        start = int(input("시작점을 100미만으로 정해주세요 : "))
    else :
        break;

while(1) :
    if (end>=100) :
        end = int(input("끝점을 100미만으로 정해주세요 : "))
    else :
        break;

for i in range(start,end+1) :
    num1 = (i%10);
    num10 = (i-num1)/10;
    mult = num1*num10
    plus += mult

print("결과 : ",int(plus))