import turtle

pen = turtle.Pen()

def speral(d):
   pen.fd(d)
   pen.rt(90)

dlina = 200
otrezkov = 30
pen.left(90)
while otrezkov>0:
	dlina=dlina*0.9
	speral(dlina)
	otrezkov-=1

input()
