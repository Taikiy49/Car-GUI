#importing graphics library
from graphics import *
#importing time module 
from time import *
#importing random module
import random

#defining car
def draw_car(win,p1,p2):

    #drawing the left and right tire of the car
    carlist1=[]
    width = abs(p2.x-p1.x)
    tire_left = Circle(Point(p1.x+width/4,p1.y),width/8)
    tire_left.setFill("black")
    tire_left.draw(win)

    tire_right = Circle(Point(p2.x-width/4,p1.y),width/8)
    tire_right.setFill("black")
    tire_right.draw(win)

    #drawing the car body
    body = Rectangle(Point(p1.x,p1.y),Point(p2.x,p2.y))
    body.setFill("blue")
    body.draw(win)

    #combining the car tires and car body as carlist1 and returning it
    carlist1.append(tire_left)
    carlist1.append(tire_right)
    carlist1.append(body)
    return carlist1

#defining  car roof
def draw_car_roof(win,p1,p2,p3):

    #drawing the car roof 
    carlist = []
    width = abs(p2.x-p1.x)
    car_roof = Polygon(Point(p1.x+width/4,p2.y),Point(p1.x+(3/4)*(width),p2.y),Point(p2.x-3*(width/8),p3.y),Point(p1.x+3*(width/8),p3.y))
    car_roof.setFill("red")
    car_roof.draw(win)

    #returning carlist after appending the car roof
    carlist.append(car_roof)
    return carlist

#defining truck roof
def draw_truck_roof(win,p4,p5,p6):

    #drawing the truck roof
    trucklist = []
    width = abs(p5.x-p4.x)
    truck_roof = Rectangle(Point((p5.x-width/2),p5.y),Point(p5.x,p6.y))
    truck_roof.setFill("orange")
    truck_roof.draw(win)

    #returning trucklist after appending the truck roof
    trucklist.append(truck_roof)
    return trucklist

#defining truck
def draw_truck(win,p1,p2):

    #drawing the right and left tires of the truck
    buslist=[]
    width = abs(p2.x-p1.x)
    tire_left_truck = Circle(Point(p1.x+width/4,p1.y),width/8)
    tire_left_truck.setFill("black")
    tire_left_truck.draw(win)

    tire_right_truck = Circle(Point(p2.x-width/4,p1.y),width/8)
    tire_right_truck.setFill("black")
    tire_right_truck.draw(win)

    #drawing the truck body
    body_truck = Rectangle(Point(p1.x,p1.y),Point(p2.x,p2.y))
    body_truck.setFill("yellow")
    body_truck.draw(win)

    #combining the tires of the truck and the body of the truck as buslist and returning buslist
    buslist.append(tire_left_truck)
    buslist.append(tire_right_truck)
    buslist.append(body_truck)
    return buslist  

#defining buttons
def createButtons(win, anchor, width, height):
    button_list = [ ]
    #naming the button names
    label = ["Day", "Night", "Speed-Up", "Exit"]
    #for loop to draw all 4 buttons
    for i in range(4):
        anchor1 = anchor.clone()
        anchor2 = anchor.clone()
        anchor2.move(width, height)
        newbutton = Rectangle(anchor1, anchor2)
        newbutton.setFill("gray")
        newbutton.draw(win)
        anchor1.move(width/2, height/2)
        newlabel = Text(anchor1, label[i])
        newlabel.setStyle("bold")
        newlabel.setTextColor("white")
        newlabel.draw(win)
        if i==2:
            newlabel_special=newlabel
        button_list.append(newbutton)
        anchor.move(width+1, 0)
    #returning button_list and newlabel_special
    return button_list, newlabel_special

#defining the slow button
def createSlowDownButton(win, anchor, width, height):
    slowDownButton = [ ]
    label = ["Slow Down"]
    for i in range(1):
        anchor1 = anchor.clone()
        anchor2 = anchor.clone()
        anchor2.move(width, height)
        newbutton = Rectangle(anchor1, anchor2)
        newbutton.setFill("gray")
        newbutton.draw(win)
        anchor1.move(width/2, height/2)
        newlabel = Text(anchor1, label[i])
        newlabel.setStyle("bold")
        newlabel.setTextColor("white")
        newlabel.draw(win)
    #returning slowbutton
    return slowDownButton

#defining the speed button
def createSpeedUpButton(win, anchor, width, height):
    speedUpButton = [ ]
    label = ["Speed-Up"]
    for i in range(1):
        anchor1 = anchor.clone()
        anchor2 = anchor.clone()
        anchor2.move(width, height)
        newbutton = Rectangle(anchor1, anchor2)
        newbutton.setFill("gray")
        newbutton.draw(win)
        anchor1.move(width/2, height/2)
        newlabel = Text(anchor1, label[i])
        newlabel.setStyle("bold")
        newlabel.setTextColor("white")
        newlabel.draw(win)
    #returning speed button
    return speedUpButton
    
#defining isHitBtn
def isHitBtn(pClick,Btn):

    #setting the lower left and upper right coordinates for all 4 buttons
    dayBtn_ll = Point(2,2)
    dayBtn_ur = Point(6,4)

    nightBtn_ll = Point(7,2)
    nightBtn_ur = Point(11,4)

    speedSlowBtn_ll = Point(12,2)
    speedSlowBtn_ur = Point(16,4)
    
    exitBtn_ll = Point(17,2)
    exitBtn_ur = Point(21,4)

    #if mouse is clicked on a button, each button would return a different Btn value

    if dayBtn_ll.x < pClick.x < dayBtn_ur.x and dayBtn_ll.y < pClick.y < dayBtn_ur.y:
        return Btn == 0
        return True
        
    elif nightBtn_ll.x < pClick.x < nightBtn_ur.x and nightBtn_ll.y < pClick.y < nightBtn_ur.y:
        return Btn == 1
        return True
 
    elif speedSlowBtn_ll.x < pClick.x < speedSlowBtn_ur.x and speedSlowBtn_ll.y < pClick.y < speedSlowBtn_ur.y:
        return Btn == 2
        return True
 
    elif exitBtn_ll.x < pClick.x < exitBtn_ur.x and exitBtn_ll.y < pClick.y < exitBtn_ur.y:
        return Btn == 3
        return True
    else:
        return False

#defining main function
def main():
    #opening the win
    win = GraphWin("City View!", 800, 600)
    win.setCoords(0, 0, 40, 30)

    #setting the light blue background
    bg = Rectangle(Point(0,15), Point(40, 30))
    bg.setFill("light blue")
    bg.draw(win)

    #setting the light grey ground
    ground = Rectangle(Point(0,6) , Point(40, 14))
    ground.setFill("light grey")
    ground.draw(win)  

    #drawing dashed lines on the tracks
    dashedLine = Line(Point(4,10), Point(8,10))
    dashedLine.setFill("white")
    dashedLine.setWidth(5)
    dashedLine.draw(win)
    dashedLineCopy = dashedLine.clone()
    dashedLineCopy.move(10,0)
    dashedLineCopy.draw(win)
    dashedLineCopy = dashedLine.clone()
    dashedLineCopy.move(20,0)
    dashedLineCopy.draw(win)
    dashedLineCopy = dashedLine.clone()
    dashedLineCopy.move(30,0)
    dashedLineCopy.draw(win)

    #drawing the sun
    sun = Circle(Point(37,27), 2)
    sun.setFill("yellow")
    sun.setOutline("yellow")
    sun.draw(win)

    #initial sunny day text
    txtMsg1 = Text(Point(20,29),"Sunny Day")
    txtMsg1.setTextColor("orange")
    txtMsg1.setStyle("bold")
    txtMsg1.draw(win)

    #initial red instruction text
    pntMsg = Point(20,5)
    txtMsg = Text(pntMsg, "Please click the left bottom point of the car body.")
    txtMsg.setTextColor("red")
    txtMsg.setStyle("bold")
    txtMsg.draw(win)

    #opening input file to draw the buildings in the background
    file = open("hw4_input.txt","r")
    with open("hw4_input.txt","r") as file:
        numberofLines = sum(1 for line in file)
    with open("hw4_input.txt","r") as file:
        for i in range(0,numberofLines):
            l = file.readline()
            l = l.split("\t")
            l[4] = l[4].replace("\n","")
            buildings = Rectangle(Point(l[0],l[1]),Point(l[2],l[3]))
            buildings.setFill(str(l[4]))
            buildings.draw(win)

    #getting mouse to set the bottom left point of the car body and instructing the user to click on the upper right point of the car body
    p1 = win.getMouse()
    p1text = Text(Point(20,5),"Now click the upper right point of the car body.")
    p1text.setTextColor("red")
    p1text.setStyle("bold")
    p1text.draw(win)
    txtMsg.undraw()

    #getting mouse to set the upper right point of the car body and instructing the user to click on the roof top point of the car
    p2 = win.getMouse()
    p2text = Text(Point(20,5),"Now click the roof top point of the car.")
    p2text.setTextColor("red")
    p2text.setStyle("bold")
    p2text.draw(win)
    p1text.undraw()

    #setting e1 as draw_car
    e1 = draw_car(win,p1,p2)

    #getting mouse to set the roof top point of the car and instructing the user to click on the lower left point of the truck body
    p3 = win.getMouse()
    p3text = Text(Point(20,5),"Now click the lower left point of the truck body.")
    p3text.setTextColor("red")
    p3text.setStyle("bold")
    p3text.draw(win)
    p2text.undraw()

    #setting e2 as draw_car_roof
    e2 = draw_car_roof(win,p1,p2,p3)

    #getting mouse to set the lower left point of the truck body and instructing the user to click on the upper right point of the truck body
    p4 = win.getMouse()
    p4text = Text(Point(20,5),"Now click the upper right point of the truck body.")
    p4text.setTextColor("red")
    p4text.setStyle("bold")
    p4text.draw(win)
    p3text.undraw()
    
    #getting mouse to set the upper right point of the truck body and instructing the user to click on the roof top point of the truck
    p5 = win.getMouse()
    p5text = Text(Point(20,5),"Now click the roof top point of the truck.")
    p5text.setTextColor("red")
    p5text.setStyle("bold")
    p5text.draw(win)
    p4text.undraw()
    
    #setting e3 as draw_truck
    e3 = draw_truck(win,p4,p5)

    #getting mouse to set the roof top point of the truck
    p6 = win.getMouse()
    p5text.undraw()

    #setting e4 as draw_truck_roof
    e4 = draw_truck_roof(win,p4,p5,p6)

    #placing down all 4 buttons on the window
    buttons,special_label = createButtons(win, Point(2,2), 4, 2)

    #initializing gameState and speed values
    gameState = 0
    speed = 0.05

    #while loop to make the truck move
    while True:
        sleep(0.0001)
        for part in e3:
            part.move(speed,0)
            if part.getP1().getX()>40:
                part.move(-42,0)
            
        for part in e4:
            part.move(speed,0)
            if part.getP1().getX()>40:
                part.move(-42,0)

        #if pClick is not on the buttons, nothing happens
        pClick = win.checkMouse()
        if pClick is not None:
            #if pClick is on the exit button, window closes
            if isHitBtn(pClick,3): 
                win.close()
                break
            #if pClick is on the day button, background turns to day
            elif isHitBtn(pClick, 0):
                #what happens when gameState is already at 0
                if gameState == 0:
                    speed = 0.05

                #what happens when gameState is already at 1
                elif gameState == 1:
                    moon1.undraw()
                    moon2.undraw()
                    speed = 0.05
                    sun = Circle(Point(37,27), 2)
                    sun.setFill("yellow")
                    sun.setOutline("yellow")
                    sun.draw(win)
                    gameState = 0
                    bg.setFill("lightblue")

                #what happens when gameState is already at 2
                elif gameState == 2:
                    speed = 0.3          
                        
                #what happens when gameState is already at 3
                elif gameState == 3:
                    moon1.undraw()
                    moon2.undraw()
                    bg.setFill("lightblue")
                    sun = Circle(Point(37,27), 2)
                    sun.setFill("yellow")
                    sun.setOutline("yellow")
                    sun.draw(win)
                    speed = 0.3
                    gameState = 2
                    
            #if pClick is on the night button, background turns to night
            elif isHitBtn(pClick, 1):

                #what happens when gameState is already at 0
                if gameState == 0:
                    sun.undraw()
             
                    bg.setFill("navy")
                 
                    moon1 = Circle(Point(37,27),2)
                    moon1.setFill("white")
                    moon1.setOutline("white")
                    moon1.draw(win)

                    moon2 = Circle(Point(37.75,28),1.5)
                    moon2.setFill("navy")
                    moon2.setOutline("navy")
                    moon2.draw(win)
                  
                    gameState = 1

                #what happens when gameState is already at 1
                elif gameState == 1:
                    gameState = 1

                #what happens when gameState is already at 2
                elif gameState == 2:
                    sun.undraw()

        
                    bg.setFill("navy")

   
                    moon1 = Circle(Point(37,27),2)
                    moon1.setFill("white")
                    moon1.setOutline("white")
                    moon1.draw(win)
                    moon2 = Circle(Point(37.75,28),1.5)
                    moon2.setFill("navy")
                    moon2.setOutline("navy")
                    moon2.draw(win)
                    gameState = 3
                    speed = 0.15

                #what happens when gameState is already at 3
                elif gameState == 3:
                    speed = 0.15
                    
                    
            #when pClick hits the speed up and slow down button
            elif isHitBtn(pClick, 2):
                #what happens if gameState is already 0
                if gameState == 0:
                    createSlowDownButton(win, Point(12,2), 4, 2)
                    gameState = 2
                    speed = 0.3

                #what happens if gameState is already 1
                elif gameState == 1:
                    createSlowDownButton(win, Point(12,2), 4, 2)
                    gameState = 3
                    speed = 0.15

                #what happens if gameState is already 2
                elif gameState == 2:
                    createSpeedUpButton(win, Point(12,2), 4, 2)
                    gameState = 0
                    speed = 0.05

                #what happens if gameState is already 3
                elif gameState == 3:
                    createSpeedUpButton(win, Point(12,2), 4, 2)
                    gameState = 1
                    speed = 0.05

            #orange sunny day text when gameState is 0
            if gameState == 0:
                txtMsg1.undraw()
                txtMsg1 = Text(Point(20,29),"Sunny Day")
                txtMsg1.setTextColor("orange")
                txtMsg1.setStyle("bold")
                txtMsg1.draw(win)

            #orange moon night text when gameState is 1
            elif gameState == 1:
                txtMsg1.undraw()
                txtMsg1 = Text(Point(20,29),"Moon Night")
                txtMsg1.setTextColor("orange")
                txtMsg1.setStyle("bold")
                txtMsg1.draw(win)
 
            #orange sunny day high speed text when gameState is 2
            elif gameState == 2:
                txtMsg1.undraw()
                txtMsg1 = Text(Point(20,29),"Sunny Day, High Speed")
                txtMsg1.setTextColor("orange")
                txtMsg1.setStyle("bold")
                txtMsg1.draw(win)

            #orange moon night medium speed text when gameState is 3
            elif gameState == 3:
                txtMsg1.undraw()
                txtMsg1 = Text(Point(20,29),"Moon Night, Medium Speed")
                txtMsg1.setTextColor("orange")
                txtMsg1.setStyle("bold")
                txtMsg1.draw(win)

#running the main function
main()
