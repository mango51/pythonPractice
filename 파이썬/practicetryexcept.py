list1 = ['A','B','C','D']

for i in range(0,5):
    try:
        print(list1[i])
    except IndexError:
        print("해당하는 인덱스가 없습니다.")

try:
    f = open('name.txt','r')
    print(f.read())
except FileNotFoundError:
    print("파일이 없습니다.")
