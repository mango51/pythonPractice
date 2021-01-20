fruits = ['apple','strawberry', 'banana','melon','grape','kiwi']
print(fruits[1:4])
print(fruits[2:])

fruits1 = ['apple','strawberry', 'banana', 'watermelon']
fruits2 = ['melon','grape','kiwi']
if(len(fruits1) > len(fruits2)):
    print(fruits1)
else:
    print(fruits2)

countries = ['Korea', 'America', 'Spain', 'Germany', 'Mexico', 'Vietnam' ]
countries.append('China')
print(countries)

countries2 = ['Korea', 'America', 'Spain', 'Germany', 'Mexico', 'Vietnam' ]
countries2.extend(['China','Japan'])
print(countries2)

countries3 = ['Korea', 'America', 'Spain', 'Germany', 'Mexico', 'Vietnam' ]
del countries3[2]
print(countries3)

num = [1, 3, 5, 7, 9]
print(sum(num))

num2 = [13, 29, 54, 31, 67]
print(max(num2) + min(num2))
