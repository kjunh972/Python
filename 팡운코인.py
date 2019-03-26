from random import * #랜덤

year=0  #날짜
month=0
week=0
day=1
tax=0   #세금
coin=100   #돈
apple = randint(10,coin*10)    #아이템 시세변경
desk = randint(10,coin*10)
ball = randint(10,coin*10)
book = randint(10,coin*10)
ruler = randint(10,coin*10)
balloon = randint(10,coin*10)
gloves = randint(10,coin*10)
items = list()  #보유중인 아이템을 출력할때 사용할 배열
House = ['일반아파트','고급아파트','삼호상가','고급상가','고급빌딩','쌍둥이빌딩','고급쌍둥이빌딩'] #부동산이름
BuyHouse = list()
invList = ['광은','심송','으튜브','내이버','더음','규글',]  #투자할수 있는 회사이름
invCompList = list()    #투자한 회사이름
invBuyList = list()     #투자한 금액
invBuy = 0  #투자 할 가격
#밑에 있는것은 부동산건물 가격시세
HouseMarket = [randint(100000,1000000), randint(1000000,10000000), randint(10000000,100000000), randint(100000000,1000000000), randint(1000000000,10000000000), randint(10000000000,100000000000), randint(100000000000,1000000000000)]
HouseCount = 0  #부동산 구매 제한. 부동산은 3개까지 구매가능하다.

while(1):
    if len(invBuyList) > 0: #투자한게 있다면
        if day==8:  #일주일이 지났다면
            for i in range(0,len(invBuyList)):
                invran = randint(0,3)   #성공또는 실패
                if invran == 0:
                    print(invCompList[i],"회사의 ",invBuyList[i],"코인의 투자를 실패하였습니다.")
                elif invran == 1:
                    print(invCompList[i],"회사의 ",invBuyList[i],"코인의 투자를 실패하였습니다.")
                elif invran == 2:
                    print(invCompList[i],"회사의 ",invBuyList[i],"코인의 투자를 실패하였습니다.")
                else:
                    print(invCompList[i],"회사의 ",invBuyList[i],"코인의 투자를 성공하였습니다. 2배로 지불해드립니다.")
                    invSuss = invBuyList[i] #배열에 가격을 받고
                    invSuss*=2  #투자한금액 2배해서
                    tax = invSuss//5    #세금
                    invSuss-=tax
                    coin+=invSuss   #추가

            while(1):
                if len(invBuyList)<=0:  #투자한게 없으면
                    break
                else:   #투자한게있으면 지움
                    del(invBuyList[len(invBuyList)-1])
                    del(invCompList[len(invCompList)-1])
                


    if day==8:      #날짜지날수있게
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

    sel = input("\"도움말\", \"시세확인\", \"보유중인아이템\", \"다음날\", \"아이템구매\", \"아이템판매\", \"부동산\", \"투자\" 그만 하실려면 \"0\"을 입력해주세요... ")
    if sel=="도움말":
        print("도움말 : 도움말을 확인합니다.")
        print("세금 : 아이템이나 건물을 판매할때나 투자에 성공했을때 받을 코인에서 세금20%를 떼어갑니다.")
        print("시세확인 : 아이템시세를 확인합니다.")
        print("보유중인아이템 : 보유중인 아이템을 확인합니다.")
        print("다음날 : 하루가 지납니다.")
        print("아이템구매 : 아이템을 구매합니다. 3개까지 구매가능.")
        print("아이템판매 : 아이템을 판매합니다.")
        print("부동산 : 집을 구매하실수 있습니다. 일주일마다 시세에서 10%씩 코인을 얻습니다.")
        print("투자 : 회사에 투자를 하실수 있습니다.일주일마다 투자에 성공했는지 실패 했는지 알수 있습니다.")
        print("부동산구매 : 건물을 구매합니다. 단 중복 구매는 불가능")
        print("부동산판매 : 건물을 판매합니다.")
        print("부동산시세 : 시세를 확인합니다.")
        print("소유건물목록 : 가지고 있는 건물을 확인합니다.")

    elif (sel=="0"):
        break
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
        HouseMarket = [randint(100000,1000000), randint(1000000,10000000), randint(10000000,100000000), randint(100000000,1000000000), randint(1000000000,10000000000), randint(10000000000,100000000000), randint(100000000000,1000000000000)]
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
        HouseMarket = [randint(100000,1000000), randint(1000000,10000000), randint(10000000,100000000), randint(100000000,1000000000), randint(1000000000,10000000000), randint(10000000000,100000000000), randint(100000000000,1000000000000)]

    elif (sel=="아이템판매"):
        sell = input("판매할 아이템을 입력해주세요... ")

        if sell == "사과":
            try:    #해당 아이템이 있는지 제거 시도
                items.remove("사과")
            except: #해당아이템이없으면
                print("해당 아이템이 없습니다")
                continue
            tax = apple//5  #세금 계산 #세금은 20%
            apple-=tax
            coin+=apple
            print("판매를 완료하였습니다.")
        elif sell == "책상":
            try:
                items.remove("책상")
            except:
                print("해당 아이템이 없습니다")
                continue
            tax = desk//5  #세금 계산
            desk-=tax
            coin+=desk
            print("판매를 완료하였습니다.")
        elif sell == "공":
            try:
                items.remove("공")
            except:
                print("해당 아이템이 없습니다")
                continue
            tax = ball//5  #세금 계산
            ball-=tax
            coin+=ball
            print("판매를 완료하였습니다.")
        elif sell == "책":
            try:
                items.remove("책")
            except:
                print("해당 아이템이 없습니다")
                continue
            tax = book//5  #세금 계산
            book-=tax
            coin+=book
            print("판매를 완료하였습니다.")
        elif sell == "자":
            try:
                items.remove("자")
            except:
                print("해당 아이템이 없습니다")
                continue
            tax = ruler//5  #세금 계산
            ruler-=tax
            coin+=ruler
            print("판매를 완료하였습니다.")
        elif sell == "풍선":
            try:
                items.remove("풍선")
            except:
                print("해당 아이템이 없습니다")
                continue
            tax = balloon//5  #세금 계산
            balloon-=tax
            coin+=balloon
            print("판매를 완료하였습니다.")
        elif sell == "장갑":
            try:
                items.remove("장갑")
            except:
                print("해당 아이템이 없습니다")
                continue
            tax = gloves//5  #세금 계산
            gloves-=tax
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
        HouseMarket = [randint(100000,1000000), randint(1000000,10000000), randint(10000000,100000000), randint(100000000,1000000000), randint(1000000000,10000000000), randint(10000000000,100000000000), randint(100000000000,1000000000000)]
    elif sel=="부동산":
        print()
        print()
        house = input("\"부동산시세\", \"부동산구매\", \"부동산판매\", \"소유건물목록\", \"뒤로가기\"중 하나를 입력해주세요... ")
        if house=="부동산시세":
            for i in range(0,len(House)):
                print(House[i]," : ",HouseMarket[i],"코인입니다.")
        elif house=="부동산구매":
            if HouseCount==3:
                print("건물은 3개만 구매가능합니다.")
                continue

            houseBuy = input("구매하고싶은 건물을 입력해주세요... ")

            houseCount=0 #몇개 중복됐는지 계산
            for i in range(0,len(BuyHouse)):  
                if houseBuy==BuyHouse[i]:       #같은건물이 발견되면 경고문장 count
                    houseCount+=1
            
            if houseCount>0:       #count가 0보다 크면 에러문장 출력
                print("같은 건물을 소유하고 계십니다. 같은 건물은 구매 불가능합니다.")
                continue
                    
            countHouse = 0  #건물이 존재하는지 안하는지 확인하는 변수
            for k in range (0,len(House)):
                if houseBuy==House[k]: #입력한 건물이랑 존재하는 건물이름이랑 같으면
                    countHouse+=1   #countHouse +1
            if countHouse==0:   #입력한 건물이랑 존재하는 건물이랑 같으면 countHouse가 +1되는데 0인것은 존재하는 아파트가 아니니
                print("존재하지않는 건물입니다.")
                continue

            for i in range (0,len(House)):
                if houseBuy==House[i]: #입력한 건물이름이랑 현재 존재하는 이름이 같다면
                    if (coin>HouseMarket[i]):   #건물코인보다 보유한 코인이 더 많다면
                        HouseCount+=1   #HouseCount가 3까지만 구매 가능. 건물 구매제한을 위해 구매할때마다 1씩 늘어남
                        coin-=HouseMarket[i] #가지고 있는 코인에서 건물코인을 뺀다
                        BuyHouse.append(houseBuy)
                        print(House[i],"가 구매 완료되었습니다.")
                    else:
                        print("돈이 부족합니다.")
                        continue
            day+=1                          #구매만하면 하루가 안지나서 이렇게 해야함
            apple = randint(10,coin*100)
            desk = randint(10,coin*100)
            ball = randint(10,coin*100)
            book = randint(10,coin*100)
            ruler = randint(10,coin*100)
            balloon = randint(10,coin*100)
            gloves = randint(10,coin*100)
            HouseMarket = [randint(100000,1000000), randint(1000000,10000000), randint(10000000,100000000), randint(100000000,1000000000), randint(1000000000,10000000000), randint(10000000000,100000000000), randint(100000000000,1000000000000)]

        elif house=="부동산판매":
            if len(BuyHouse)==0:
                print("건물을 소유하고 있지 않습니다.")
                continue
            houseSell = input("판매하고싶은 건물을 입력해주세요... ")

            countHouse = 0  #건물이 존재하는지 안하는지 확인하는 변수
            for k in range (0,len(House)):
                if houseSell==House[k]: #입력한 건물이랑 존재하는 건물이름이랑 같으면
                    countHouse+=1   #countHouse +1
            if countHouse==0:   #입력한 건물이랑 존재하는 건물이랑 같으면 countHouse가 +1되는데 0인것은 존재하는 아파트가 아니니
                print("존재하지않는 건물입니다.")
                continue

            for k in range (0, len(BuyHouse)):
                for i in range (0,len(House)):
                    if BuyHouse[k]==House[i]:
                        if houseSell==BuyHouse[k]: #입력한 건물이름이랑 현재 존재하는 이름이 같다면
                            tax = HouseMarket[i]//5
                            HouseMarket[i]-=tax
                            coin+=HouseMarket[i]
                            HouseCount-=1
                            print(BuyHouse[k],"가 판매 완료되었습니다.")
                            BuyHouse.remove(houseSell)
                            break
                        else:
                            print("해당아파트를 소유하고 있지 않습니다.")
                            continue
            
            day+=1                          #판매만하면 하루가 안지나서 이렇게 해야함
            apple = randint(10,coin*100)
            desk = randint(10,coin*100)
            ball = randint(10,coin*100)
            book = randint(10,coin*100)
            ruler = randint(10,coin*100)
            balloon = randint(10,coin*100)
            gloves = randint(10,coin*100)
            HouseMarket = [randint(100000,1000000), randint(1000000,10000000), randint(10000000,100000000), randint(100000000,1000000000), randint(1000000000,10000000000), randint(10000000000,100000000000), randint(100000000000,1000000000000)]

        elif house=="소유건물목록":
            if len(BuyHouse)==0:
                    print("가지고 있는 건물이 없습니다.")
            for i in range (0,len(BuyHouse)):
                print(BuyHouse[i])
        
        elif house=="뒤로가기":
            print("뒤로갔습니다.")
            continue
        
        else:
            print("오타입니다.")
            continue

    elif sel=="투자":
        inv = input("\"투자가능한회사\", \"투자하기\", \"투자목록\", \"악마의유혹\", \"뒤로가기\"중 하나를 입력해주세요... ")
        
        if inv=="투자가능한회사":
            for i in range(0,len(invList)):
                print(invList[i],end='   ')
        elif inv=="투자하기":
            invComp = input("투자하고 싶은 회사이름을 입력해주세요... ")

            invSame = 0
            for i in range(0,len(invCompList)): 
                if invComp==invCompList[i]:       #중복이 발견되면 invSame+1
                    invSame+=1            
            if invSame>0:       #invSame가 0보다 크면 에러문장 출력
                print("같은 회사를 중복으로 투자하실수 없습니다. 다른회사에 투자해주세요.")
                continue

            invCompCount=0  #입력한회사가 존재하는지 카운트
            for i in range(0,len(invList)): #카운트계산
                if invComp==invList[i]:
                    invCompCount+=1
            if invCompCount<1:  #카운트가 0이면 존재하지않는 회사
                print("존재하지않는 회사입니다.")
                continue
            
            try:    #투자할 금액 받기
                invBuy = int(input("얼마를 투자하시겠습니까?... "))
            except: #정수가 아닌 문자로 입력하면 경고문장 출력하기
                print("정수로 입력해주세요.")
                continue
            
            coin-=invBuy
            print("투자를 완료하였습니다.")
            invBuyList.append(invBuy)   #투자한 금액 배열추가
            invCompList.append(invComp) #투자한 회사 배열제거
            
            day+=1                          #투자만하면 하루가 안지나서 이렇게 해야함
            apple = randint(10,coin*100)
            desk = randint(10,coin*100)
            ball = randint(10,coin*100)
            book = randint(10,coin*100)
            ruler = randint(10,coin*100)
            balloon = randint(10,coin*100)
            gloves = randint(10,coin*100)
            HouseMarket = [randint(100000,1000000), randint(1000000,10000000), randint(10000000,100000000), randint(100000000,1000000000), randint(1000000000,10000000000), randint(10000000000,100000000000), randint(100000000000,1000000000000)]

        elif inv=="투자목록":
            if len(invBuyList)>0:
                for i in range(0,len(invBuyList)):
                    print(invCompList[i],end=' : ') #회사
                    print(invBuyList[i],"코인",end='   ')   #투자한 돈
            else:
                print("현재 투자 목록이 없습니다.")
        
        elif inv=="악마의유혹":
            devil = input("회사이름을 입력해주세요... ")
            devilRan = randint(0,1)
            if devilRan==0:
                print(devil+"는(은) 투자에 실패 할 것 같습니다.")
            else:
                print(devil+"는(은) 투자에 성공 할 것 같습니다.")

        elif inv=="뒤로가기":
            print("뒤로갔습니다.")
            continue

        else:
            print("잘못입력했습니다.")
            continue


    else:   #오타이면 출력
        print()
        print()
        print()
        print("오타입니다. 다시 입력해주세요.")
        continue