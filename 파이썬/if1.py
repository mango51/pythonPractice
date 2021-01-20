agestring = input('나이를 입력하세요. ')
age = int(agestring)

if (age <= 7 & age >= 1):
    ages = "유아"
elif (age <= 13 & age >= 8):
    ages = "초등학생"
elif (age <=16 & age >= 14):
    ages = "중학생"
elif (age <=19 & age >= 17):
    ages = "고등학생"
elif (age >= 20):
    ages = '성인'

print(ages)
