#ourGraphics by APG and Gen
from graphics import*

#variables
winX = 600
winY = 600
diaSize = 50
#window
oGwin = GraphWin("ourGraphics", winX, winY)
oGwin.setCoords(0, 0, winX, winY)
oGwin.setBackground("Midnight Blue")

#Moom
m = Circle(Point(winX/2,winY-40), 100)
m.draw(oGwin)
cornerPoint = m.getP1()
m.setFill("Antique White")
m.setOutline("Antique White")

#grass
g = Rectangle(Point(winX/-winX,winY/-winY), Point(winX+1,winY/2)) 
g.draw(oGwin)
cornerPoint = g.getP1()
g.setFill("dark green")
g.setOutline("dark green")

#star(s)
s = Circle(Point(500,400), 5)
s.draw(oGwin)
cornerPoint = s.getP1()
s.setFill("Khaki")
s.setOutline("Khaki")

#pT
p = Rectangle(Point(winX/12, winY/12), Point(winX/6, winY/6))
p.draw(oGwin)
cornerPoint = p.getP1()
p.setFill("Brown")
p.setOutline("Saddle Brown")
p.setWidth(20)
                    
l = Polygon(Point(winX/20,winY/6),
            Point(winX/4,win/6),
            Poiny(winX/5,winY))
l.setOutline()
            
