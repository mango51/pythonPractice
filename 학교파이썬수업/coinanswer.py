money, c500, c100, c50, c10 = 0,0,0,0,0 #교환할 돈과 각 동전 개수를 저장할 전역변수 설정

money = int(input('돈: '))
c500 = money//500
money %= 500

c100 =money//100
money %= 100

c50 = money//50
money%= 50

c10 = money//10
money%= 10

print('%d %d %d %d %d' %(c500, c100, c50, c10, money))


money2, c50000, c10000, c5000, c1000 = 0, 0, 0,0 ,0

money2 = int(input('돈 :'))
c50000 = money2//50000
money2 %= 50000

c10000 = money2//10000
money2 %= 10000

c5000 = money2//5000
money2 %= 5000

c1000 = money2//1000
money2 %= 1000

print('%d %d %d %d %d'% (c50000, c10000, c5000, c1000, money2))
