lines = int(input("줄 수를 입력해주세요 : "))

for i in range(1, lines+1):
    for j in range(1,lines+1):
        if j>lines-i and j!=lines:
            print('*',end='')
        elif j==lines:
            print('*')
        else:
            print(' ',end='')



