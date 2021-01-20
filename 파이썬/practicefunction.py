def test(a,b,c):
    return a*b*c
print(test(1,2,3))

def test1():
    return "안녕"
print(test1())

def test3(a,b=3,c=4):
    return a+b+c
print("1번 정답: ", test3(1))
print("2번 정답: ", test3(1,2))
print("3번 정답: ", test3(1,2,3))
