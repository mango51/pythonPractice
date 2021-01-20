number = input('1=가위, 2=바위, 3=보 : ')
number2 = number.split()

scissor = number2.count('1')
rock = number2.count('2')
paper = number2.count('3')

if scissor==0 and rock!=0 and paper!=0:
    print(paper) #가위 낸 사람 없으니 주먹 보에서 보 낸 사람 승리
    elif scissor!=0 and rock==0 and paper!=0:
        print(scissor) #바위 낸 사람 없으니 보 가위 낸 사람 중에 가위 승리
    elif scissor!=0 and rock!=0 and paper==0:
        print(rock) #보 낸 사람 없으니 바위 가위 낸 사람 중에 바위 승리
    elif scissor!=0 and rock!=0 and paper!=0:
        print(0) #무승부
    elif scissor==0 or rock==0 or paper==0:
        print(0) #가위 혹은 바위 혹은 보가 없을 때, 같이 전부 같은 것을 냈을 때
