weight = float(input("현제체중 입력해주세요 : "))
standardweight = float(input("표준체중을 입력해주세요(표준체중을 모르면 0을 입력하세요.) : "))

if (standardweight == 0):
    height = float(input("키를 입력하세요 : "))
    standardweight = (height - 100) * 0.9
    print("당신의 표준체중은 {:.1f}".format(standardweight))

obesity = (weight/standardweight)*100
print("당신의 비만도는 {:.2f}입니다.".format(obesity))