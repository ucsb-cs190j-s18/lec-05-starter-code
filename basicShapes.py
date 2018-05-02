import turtle
import math

jane = turtle.Turtle()
jane.shape("turtle")
jane.speed(0)
jane.width(8)

      
def drawRectangle(width, height, tilt, penColor, fillColor):
    jane.color(penColor, fillColor)
    jane.begin_fill()
    jane.seth(tilt)
    jane.forward(width)
    jane.left(90)
    jane.forward(height)
    jane.left(90)
    jane.forward(width)
    jane.left(90)
    jane.forward(height)
    jane.end_fill()
    jane.seth(0)

def drawTriangle(base, height, penColor, fillColor):

    jane.begin_fill()
    jane.color(penColor, fillColor)
    jane.forward(base)
    turnAngle = 180 - math.degrees(math.atan2(height,base/2))
    jane.left(turnAngle)
    side = math.sqrt((base/2)**2 +(height**2))
    jane.forward(side)
    jane.left(2*(180-turnAngle))
    jane.forward(side)
    jane.seth(0)
    jane.end_fill()
     
