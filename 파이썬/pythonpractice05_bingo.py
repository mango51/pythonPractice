lyrics = input('가사 입력 : ')
word = input('찾고 싶은 단어 : ')
numbers = lyrics.count(word)

while(1):
    guess = int(input('찾는 단어가 몇 번 나왔을까요? : '))

    if guess > numbers:
        for i in range(1,guess):
            print(i,end='')
        print('중에 있습니다.')
    elif guess < numbers:
        print(guess,'보다 큽니다')
    elif guess == numbers:
        print('빙고')
        break
