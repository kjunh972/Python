from random import *

year=0
month=0
week=0
day=0

money=2000
coin=0

while(1):
    day+=1

    if day==8:
        day = 1
        week+=1
    if week==5:
        week=1
        month+=1
    if month==13:
        month=1
        year+=1

    print("현재", year,"년, ",month,"월, ", week,"주, ", day,"일 입니다.")
    print("현재 잔액은 ",money,"입니다.")

    sel = input("\"잔액확인\", \"시세확인\", \"알바\", \"팡운코인 구매\", 그만 하실려면 \"0\"을 입력해주세요... ")

    if (sel=="0"):
        break
    elif (sel=="잔액확인")
        print("현재 잔액은 ",money,"입니다.")
    elif (sel=="시세확인")
        print("현재 잔액은 ",money,"입니다.")
    elif (sel=="알바")
       
        print("현재 알바자리가 없습니다.")
        elif (sel=="잔액확인")
        print("현재 잔액은 ",money,"입니다.")