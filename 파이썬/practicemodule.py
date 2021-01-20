import modulepractice
import random

print(modulepractice.multi(2,3,4))

lists=[]

for i in range(1,5):
    num = random.randint(1,100)
    lists.append(num)
    
lists.sort()
print(lists)
