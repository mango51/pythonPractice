number = input('1=가위, 2=바위, 3=보 : ')

number2 = number.split()
#split()으로 공백 기준 나누어 리스트로 반환해주기


rock =0
paper =0
scissor = 0

print('이긴 사람 수 : ', end='')

for i in range(0, len(number2)):
    if number2[i] == '1':
        scissor += 1
    elif number2[i] == '2':
        rock += 1
    elif number2[i] == '3':
        paper += 1

if scissor >= 1 and rock >= 1 and paper >= 1:
    print(0)
elif scissor != 0 and rock != 0:
    print(rock)
elif scissor != 0 and paper != 0:
    print(scissor)
elif rock != 0 and paper != 0:
    print(paper)
elif rock != 0 and paper == 0 and scissor == 0:
    print(rock)
elif rock ==0 and paper != 0 and scissor ==0:
    print(paper)
elif rock==0 and paper ==0 and scissor !=0:
    print(scissor)
