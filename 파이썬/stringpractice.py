a = 'ABCDEFG'
print('1번 : ',a[1:4])

b="AbcCDeEFggG"
print('2번 : ',b.upper())
print('2번 : ',b.lower())

c = "aaaAAbbBBcCCdE"
length = len(c)

total = 0
for i in range(1, length+1):
    total += i
    if (i<length):
        print(i,'+ ', end='')
    else:
        print(i,'= ', end='')

print(total)
