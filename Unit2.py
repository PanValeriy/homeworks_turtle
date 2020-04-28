import turtle

pen = turtle.Pen()

def sq(d, color):
   pen.fillcolor(color)
   pen.begin_fill()
   for x in range(4):
       pen.fd(d)
       pen.left(90)

   pen.end_fill()

color = ['blue','red','black']
for y in range (3):
    sq(100,color[y])
    pen.left(90)

pen.up()
pen.fd(200)
pen.down()
pen.left(90)
pen.circle(200)

input()