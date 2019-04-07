#ourGraphics by APG and Gen
from graphics import* #importing graphics module
import random #importing random module

winX = 600 #window x value
winY = 600 #window y value

oGwin = GraphWin("ourGraphics", winX, winY) #creates window
oGwin.setCoords(0, 0, winX, winY) #sets window size
oGwin.setBackground("Midnight Blue") #sets the background of the window


def draw_s(sX, sY, size, color, oGWin): #defines the function for drawing star
    s = Circle(Point(sX,sY), size) #circle for star x,y coords and size
    s.setFill(color) #sets the fill color for the star
    s.setOutline(color) #sets the outline color for the star
    s.draw(oGwin) #draws the star (circle) in the window

for i in range(60): #for loop for the star (circle)
    draw_s((random.randrange(0, 600, 1)), (random.randrange(300, 600, 1)), 5, "khaki", oGwin)
    #calls the draw_s, draws the star 40 times in the range set (x 0-600 and y 300-600)
    #using the random module. size, color (fill/outline) and window is set.


m = Circle(Point(winX/2,winY-40), 100) #moon size and x,y coords
m.setFill("Antique White") #sets the fill color for moon
m.setOutline("Antique White") #sets the outline color for moon
m.draw(oGwin) #draws moon in window


g = Rectangle(Point(winX/-winX,winY/-winY), Point(winX+1,winY/2)) #rectangle lower right and upper left corners (grass)
g.setFill("dark green") #sets the fill color for the grass
g.setOutline("dark green") #sets the outline color for the grass
g.draw(oGwin) #draws the grass in window