import random

print("UP / DOWN 게임을 시작합니다.")

rm = random.randrange(1,100)
answer = 0
while (answer != rm) :
    answer = int(input("1~100중에서 숫자를 입력해주세요 : "))
    if(answer > rm) :
        print("Down")
        
    elif(answer < rm) :
        print("Up")
        
    else :
        print("정답")
        break