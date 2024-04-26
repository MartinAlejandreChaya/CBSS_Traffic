from graphics import *
import time


def main():

    # Create window
    win = GraphWin("My Circle", 400, 200)

    # Create gray circle
    c = Circle(Point(50,50), 10)
    c.setFill(color_rgb(51, 51, 51))
    c.draw(win)

    # Move circle every 0.01 seconds
        # x -> x + 2
        # y -> y + 0.5
    for i in range(150):
        c.move(2, 0.5)
        time.sleep(0.01)

    win.getMouse() # Wait for mouse click
    win.close()    # Close window when done


main()