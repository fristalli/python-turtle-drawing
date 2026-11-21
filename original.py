import turtle as t

k=9
t.color('purple')
t.seth(90)

for i in range (4):
    t.forward(7*k)
    t.right(90)
    t.forward(7*k)
    t.left(90)
    t.forward(7*k)
    t.right(90)
t.up()
for x in range (0,30):
    for y in range (-10,15):
        t.goto(x*k,y*k)
        t.dot(3)