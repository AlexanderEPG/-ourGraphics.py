#ourGraphics by APG and Gen
from graphics import*

#variables
winX = 600
winY = 600

#window
oGwin = GraphWin("ourGraphics", winX, winY)
oGwin.setCoords(0, 0, winX, winY)

#Sun
s = Circle(Point(winX-40,winY-40), 100)
s.draw(oGwin)
cornerPoint = s.getP1()
s.setFill("yellow")

