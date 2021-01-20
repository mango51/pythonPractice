age = input("나이를 입력하세요. ")
intage = int(age)

if (intage >= 20):
    print ("성인")
    if (intage % 2 == 0):
        print("나이가 짝수인 성인")
    else:
        print ("나이가 홀수인 성인")
            
else:
    print ("미성년자")
    if(intage % 2==0):
        print("나이가 짝수인 미성년자")
    else:
        print("나이가 홀수인 미성년자")
