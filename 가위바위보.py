import random

print("가위바위보 게임입니다.")

game = ["가위", "바위", "보"]
rm = random.choice(game)
answer = input("가위,바위,보중 하나를 입력해주세요 : ")

if (answer != rm) :
    print("당신은 AI상대로 패배하였습니다.")
    print("정답은 \"{}\"였습니다.".format(rm))
else :
    print("당신은 AI상대로 승리하였습니다.")