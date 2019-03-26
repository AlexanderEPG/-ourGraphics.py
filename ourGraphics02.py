#ourGraphics by APG and Gen
from graphics import*

#variables
winX = 600
winY = 600
diaSize = 50
#window
oGwin = GraphWin("ourGraphics", winX, winY)
oGwin.setCoords(0, 0, winX, winY)
oGwin.setBackground("lightBlue")

#Sun
s = Circle(Point(winX-40,winY-40), 100)
s.draw(oGwin)
cornerPoint = s.getP1()
s.setFill("yellow")
s.setOutline("yellow")

#grass
g = Rectangle(Point(winX/-winX,winY/-winY), Point(winX+1,winY/1.5)) 
g.draw(oGwin)
cornerPoint = g.getP1()
g.setFill("green")

#clouds
c1 = Oval(Point(winX/15,winY/1.07142857), Point(winX/3.75,winY/1.2))
c1.draw(oGwin)
cornerPoint = c1.getP1()
c1.setFill("white")
