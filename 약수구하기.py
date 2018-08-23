num = int(input("숫자를 입력해주세요 : "))

print(num,"의 약수 : ",end="")
for i in range(1,num+1) :
    if (num%i==0) :
        print(i,end=" ")