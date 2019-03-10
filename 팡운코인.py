from random import * #랜덤

year=0  #날짜
month=0
week=0
day=1
coin=1000   #돈
apple = randint(10,100)     #아이템 시세변경
desk = randint(10,10000)
ball = randint(10,10000)
book = randint(10,10000)
ruler = randint(10,10000)
balloon = randint(10,10000)
gloves = randint(10,10000)
items = list()              #보유중인 아이템을 출력할때 사용할 배열

while(1):
    if day==8:      #날짜지날수 있게
        day = 1
        week+=1
    if week==5:
        week=1
        month+=1
    if month==13:
        month=1
        year+=1    

    print()
    print()
    print("현재", year,"년, ",month,"월, ", week,"주, ", day,"일 입니다.")
    print("현재 팡운코인은 ",coin,"코인입니다.")

    sel = input("\"팡운코인확인\", \"시세확인\", \"보유중인아이템\", \"다음날\", \"아이템구매\", \"아이템판매\" 그만 하실려면 \"0\"을 입력해주세요... ")
    if sel=="도움말":
        print("도움말")
    elif (sel=="0"):
        break
    elif (sel=="팡운코인확인"):
        print("현재 팡운코인은 ",coin,"코인입니다.")
        continue
    elif (sel=="시세확인"):
        print("사과 : ",apple,"코인입니다.")
        print("책상 : ",desk,"코인입니다.")
        print("공 : ",ball,"코인입니다.")
        print("책 : ",book,"코인입니다.")
        print("자 : ",ruler,"코인입니다.")
        print("풍선 : ",balloon,"코인입니다.")
        print("장갑 : ",gloves,"코인입니다.")
        continue
    elif (sel=="보유중인아이템"):
        sitems = sorted(items)

        if len(items)==0:
            print("보유중인 아이템이 없습니다. 아이템을 구매해주세요.")
            continue

        print("현재 가지고 있는 아이템수는 ",len(items),"개 입니다.")
        print("보유중인 아이템은 ",end='')
        for i in range(0,len(items)):
            print("\"",sitems[i],end='\" ')
        print("입니다.")
    elif (sel=="다음날"):   #하루 지남
        day+=1
        apple = randint(10,coin*100)
        desk = randint(10,coin*100)
        ball = randint(10,coin*100)
        book = randint(10,coin*100)
        ruler = randint(10,coin*100)
        balloon = randint(10,coin*100)
        gloves = randint(10,coin*100)
        print("하루가 지납니다.")
    elif (sel=="아이템구매"):
        if len(items)==6:   #아이템 6개까지 구매가능
            print("아이템은 최대 6개까지 구매가능합니다. 아이템을 판매하시고 구매하세요.")
            continue

        buy = input("구매를 원하는 아이템을 입력해주세요... ") 

        count=0 #몇개 중복됐는지 계산
        for i in range(0,len(items)):  
            sitem = sorted(items)   #정렬
            if buy==sitem[i]:       #같은아이템이 발견되면 카운트
                count+=1
            else:                   #아니면 0으로 초기화
                count=0
        if count==3:                #같은 아이템이 3개가 되면 더이상 구매 불가능
            print("같은 아이템을 3개까지 구매가능합니다.")
            continue
      
        if buy=="사과":
            if coin>apple:  #가격보다 가지고 있는 돈이 많으면 구매
                print(buy,"를(을) 구매 완료했습니다.")
                coin-=apple     #돈지불
                items.append("사과")  #배열에 집어넣기
            else:           #아니면 구매 불가능
                print("돈이 부족합니다. 다른 아이템을 구매하시거나 시세가 변경되길 기다리세요.")
                continue
        elif buy=="책상":
            if coin>desk:
                if count==2:
                    print("같은 아이템을 3개까지 구매가능합니다.")
                    continue

                print(buy,"를(을) 구매 완료했습니다.")
                coin-=desk
                items.append("책상")
            else:
                print("돈이 부족합니다. 다른 아이템을 구매하시거나 시세가 변경되길 기다리세요.")
                continue
        elif buy=="공":
            if coin>ball:
                print(buy,"를(을) 구매 완료했습니다.")
                coin-=ball
                items.append("공")
            else:
                print("돈이 부족합니다. 다른 아이템을 구매하시거나 시세가 변경되길 기다리세요.")
                continue
        elif buy=="책":
            if coin>book:
                print(buy,"를(을) 구매 완료했습니다.")
                coin-=book
                items.append("책")
            else:
                print("돈이 부족합니다. 다른 아이템을 구매하시거나 시세가 변경되길 기다리세요.")
                continue
        elif buy=="자":
            if coin>ruler:
                print(buy,"를(을) 구매 완료했습니다.")
                coin-=ruler
                items.append("자")
            else:
                print("돈이 부족합니다. 다른 아이템을 구매하시거나 시세가 변경되길 기다리세요.")
                continue
        elif buy=="풍선":
            if coin>balloon:
                print(buy,"를(을) 구매 완료했습니다.")
                coin-=balloon
                items.append("풍선")
            else:
                print("돈이 부족합니다. 다른 아이템을 구매하시거나 시세가 변경되길 기다리세요.")
                continue
        elif buy=="장갑":
            if coin>gloves:
                print(buy,"를(을) 구매 완료했습니다.")
                coin-=gloves
                items.append("장갑")
            else:
                print("돈이 부족합니다. 다른 아이템을 구매하시거나 시세가 변경되길 기다리세요.")
                continue
        else:
            print("존재하지않는 아이템입니다.")
            continue

        day+=1
        apple = randint(10,coin*100)   #구매만 하면 하루가 안지나가서 이렇게 해야함. 하루 지나게
        desk = randint(10,coin*100)
        ball = randint(10,coin*100)
        book = randint(10,coin*100)
        ruler = randint(10,coin*100)
        balloon = randint(10,coin*100)
        gloves = randint(10,coin*100)
    elif (sel=="아이템판매"):
        sell = input("판매할 아이템을 입력해주세요... ")

        if sell == "사과":
            try:    #해당 아이템이 있는지 제거 시도
                items.remove("사과")
            except: #해당아이템이없으면
                print("해당 아이템이 없습니다")
                continue
            coin+=apple
            print("판매를 완료하였습니다.")
        elif sell == "책상":
            try:
                items.remove("책상")
            except:
                print("해당 아이템이 없습니다")
                continue
            coin+=desk
            print("판매를 완료하였습니다.")
        elif sell == "공":
            try:
                items.remove("공")
            except:
                print("해당 아이템이 없습니다")
                continue
            coin+=ball
            print("판매를 완료하였습니다.")
        elif sell == "책":
            try:
                items.remove("책")
            except:
                print("해당 아이템이 없습니다")
                continue
            coin+=book
            print("판매를 완료하였습니다.")
        elif sell == "자":
            try:
                items.remove("자")
            except:
                print("해당 아이템이 없습니다")
                continue
            coin+=ruler
            print("판매를 완료하였습니다.")
        elif sell == "풍선":
            try:
                items.remove("풍선")
            except:
                print("해당 아이템이 없습니다")
                continue
            coin+=balloon
            print("판매를 완료하였습니다.")
        elif sell == "장갑":
            try:
                items.remove("장갑")
            except:
                print("해당 아이템이 없습니다")
                continue
            coin+=gloves
            print("판매를 완료하였습니다.")
        else:
            print("존재하지않는 아이템입니다.")

        day+=1                          #판매만하면 하루가 안지나서 이렇게 해야함
        apple = randint(10,coin*100)
        desk = randint(10,coin*100)
        ball = randint(10,coin*100)
        book = randint(10,coin*100)
        ruler = randint(10,coin*100)
        balloon = randint(10,coin*100)
        gloves = randint(10,coin*100)

    else:   #오타이면 출력
        print()
        print()
        print()
        print("오타입니다. 다시 입력해주세요.")
        print()
        print()
        print()
        continue