
from graphics import *
import queue
import sys

q = queue.Queue()
scale = 100
win = GraphWin("Square", 900, 900)
wOX = win.getWidth()//2
wOY = win.getHeight()//2

# Draw the square whose 'mental' centre is at (cx,cy) and whose mental size is s
def drawSquare(cx, cy, s):
    wcx = wOX + cx*scale
    wcy = wOY + cy*scale
    ws = s*scale
    square = Rectangle(Point(wcx - ws, wcy - ws), Point(wcx + ws, wcy + ws))
    square.draw(win)
    # square.setFill(color_rgb(r,g,b))
    # square.setOutline(color_rgb(r,g,b))
    return s

#Takes the size of the square and returns corners of said square.
def findCorners(c):
  corners = [c,c,c,-c, -c,-c, -c,c]
  return corners


def main():
    #First layer with its x/y followed by size
    fsquare = [0,0,1]
    list(map(q.put, fsquare))  #Mapping what will be, input from sys.stdin into the Queue.
    corner = drawSquare(q.get(),q.get(),q.get())  #Draw the first square
    newcorner = (findCorners(corner))
    list(map(q.put, newcorner))
    while q.qsize() > 0:
        drawSquare(q.get(),q.get(), .8)
    
        
    win.getMouse()
    win.close()

main()

##If layer == 1 then the origin is 0,0
##Else the layer is the corners of the first square.
# print(findCorners(1.0))
    # square = [0,0,1.0, 255, 0 ,0,1]
    # q = queue.Queue()
    # # for i in range(0, 20):
    # #     q.put(i)
    # list(map(q.put, square))
    # print(q.qsize())

# ---------------

#      Rectangle( p1, p2)  # p1 and p2 are points for upper left lower rt

#      clone()
#      getCenter()  # returns a Point object corresponding to the center
#      getP1()      # returns the upper left corner Point
#      getP2()      # returns the lower right corner Point

#      draw(graphwin)
#      move(dx, dy)    # move the Rectangle dx pixels on x-axis, dy on y-axis
#      setFill(color)
#      setOutline(color)
#      setWidth(width)   # set the width, in pixels of the outline
#      undraw()
