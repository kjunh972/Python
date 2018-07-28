menu = []

while (1):
    sel = input("(매뉴판 관리 프로그램을 종료하실려면 0을 입력하세요...)매뉴판 확인,추가,수정,삭제중 하나를 골라주세요... ")

    if (sel == "0"):
        break;

    if (sel == "확인"):
        print("=== 매뉴판 목록 ===")
        for i in range (0,len(menu)):
            print(menu[i])

    if (sel == "추가"):
        while (1):
            add = input("(매뉴를 그만 입력하시려면 0을 입력하세요...)추가 하실 매뉴를 입력해주세요... ")
            if (add == "0"):
                break;
            else:
                menu.append(add)

    if (sel == "수정"):
        modOri = input("수정하고 싶은 메뉴를 입력해주새요... ")
        mod = input("수정할 메뉴를 입력해주세요... ")
        menu.insert(menu.index(modOri),mod)
        del(menu[menu.index(modOri)])

    if (sel == "삭제"):
        Del = input("삭제할 매뉴를 입력해주세요...")
        del(menu[menu.index(Del)])