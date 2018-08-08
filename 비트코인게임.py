from random import *

coin = 5000
money = 1000
myCoin=0
day = 0
cheak = 0

print(":: 기본 비트코인은 ",coin,"현제 기본 돈은 ",money,"원 있습니다. 그리고 알바해서 10원씩 벌수 있습니다.")
print(":: 하루에 한번씩 비트코인 시세가 달라지고 돈으로 비트코인 살수 있습니다.")
print(":: 20일이 되기전에 가지고있는 비트코인이 비트코인시세보다 많으면 승 아니면 패배 입니다.")
print()

while(1) :
    day+=1
    print(day,"일차")

    if (day==20) :
        print("패배하였습니다.")
        break
    elif (myCoin>coin) :
        print("승리하였습니다.")
        break
        
    sel = input("비트코인시세 및 현제돈 그리고 내 비트코인을 확인 하려면 \"확인\", \"알바\", 비트코인 \"구매\", 그만 하실려면 \"0\"을 입력해주세요... ")
    
    if sel=="0" :
        break
    elif sel=="확인" :
        print("비트코인 시세는 ",coin,", 현재 잔액은 ",money,", 내 비트코인은 ",myCoin,"입니다.")
        day-=1
        cheak+=1
        continue
    elif sel=="알바" :
        print("계속 1을 입력해주세요. 1를 입력한 만큼 10원이 들어 옵니다. 0을 입력하면 알바 종료합니다.")
        while(1) :
            work = int(input())
            if (work==1) :
                money+=10
            elif (work==0) :
                break
    elif sel=="구매" :
        pay = int(input("얼마를 구매 하시겠습니까? "))
        while (1):
            if (money-pay<0) :
                pay = int(input("돈이 부족합니다. 다시 입력해주세요 "))
            else :
                break
        myCoin+=pay
        money-=pay
        coin-=pay

    if (cheak>0) :
        coin+=0
        cheak-=1
    else :
        rm = randint(100,1000)
        coin+=rm