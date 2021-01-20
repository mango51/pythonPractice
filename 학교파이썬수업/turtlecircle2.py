import turtle as t

t.shape('turtle')

t.fillcolor('yellow')
#내부 색상을 yellow로 칠해주기
t.begin_fill()
#칠해주기 시
t.circle(40)
t.forward(100)
t.circle(40)
t.end_fill()
#여기까지 그려진 circle 2개는 yellow 색상으로 도형 내부 채우기
t.forward(100)
t.circle(40)
#여기 원은 색상 없음
t.done()
