total = int(input("게시물이 몇개인지 입력하세요... "))
see = int(input("한페이지당 몇개의 게시물을 올릴건지 입력하세요... "))

if total%see==0 :
    print(int(total/see))
else :
    print(int(total/see+1))