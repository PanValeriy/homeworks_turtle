import turtle

pen = turtle.Pen()

def speed(d):
   pen.fd(d)
   pen.rt(5)

d = 0
gradus = 180
while gradus>0:
	d=d+0.1
	speed(d)
	gradus-=1


input()
