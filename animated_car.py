from graphics import*
import time
import random

class Car(Rectangle):
    def __init__(self,win,x,y,unit):
        colorlist = ["green","yellow","red","purple","orange","blue"]
        self.color = random.choice(colorlist)


        
        p1 = Point(x-unit*4,y)
        p2 = Point(x+unit*4,y+unit*3)
        p3 = Point(x,y+unit*4)

        self.score = int(unit*10)
        self.drawCar(p1,p2,p3,win)

        super().__init__(p1,p2)

        
    def getColor(self):
        return self.color
    def getScore(self):
        return self.score

    def drawCar(self,p1,p2,p3,win):
        self.car_list = []

        width = abs(p2.x-p1.x)
        self.leftTire = Circle(Point(p1.x+width/4,p1.y),width/8)
        self.leftTire.setFill("black")
        self.leftTire.draw(win)
        self.rightTire = Circle(Point(p2.x-width/4,p1.y),width/8)
        self.rightTire.setFill("black")
        self.rightTire.draw(win)
        self.carBody = Rectangle(Point(p1.x,p1.y),Point(p2.x,p2.y))
        self.carBody.setFill(self.color)
        self.carBody.draw(win)
        self.carRoof = Polygon(Point(p1.x+width/4,p2.y),Point(p1.x+(3/4)*(width),p2.y),Point(p2.x-3*(width/8),p3.y),Point(p1.x+3*(width/8),p3.y))
        self.carRoof.setFill("black")
        self.carRoof.draw(win)
        
        self.car_list.append(self.leftTire)
        self.car_list.append(self.rightTire)
        self.car_list.append(self.carBody)
        self.car_list.append(self.carRoof)

    def move(self, Xdistance):
        for blah in self.car_list:
            blah.move(Xdistance,0)
        super().move(Xdistance,0)

    def undraw(self):
        for bloop in self.car_list:
            bloop.undraw()
    
def draw_buildings(win, p1_x,p1_y,p2_x,p2_y,color):
    shape=Rectangle(Point(p1_x,p1_y),Point(p2_x,p2_y))
    shape.setFill(color)
    shape.draw(win)

def isClicked(pClick,rec):

    if rec.getP1().getX() < pClick.getX() < rec.getP2().getX() and rec.getP1().getY() < pClick.getY() < rec.getP2().getY():
        return True
    else:
        return False



def main():
    
    win = GraphWin("Moving Cars", 800, 600)
    win.setCoords(0, 0, 40, 40)

    bg = Rectangle(Point(0,25), Point(40, 40))
    bg.setFill("light blue")
    bg.draw(win)

    ground = Rectangle(Point(0,6) , Point(40, 24))
    ground.setFill("light grey")
    ground.draw(win)
    temp=4
    
    while temp<40:
        gnd_lines1= Line(Point(temp,10),Point(temp+4,10))
        gnd_lines1.setWidth(5)
        gnd_lines1.setFill("white")
        gnd_lines2= Line(Point(temp,15),Point(temp+4,15))
        gnd_lines2.setWidth(5)
        gnd_lines2.setFill("white")
        gnd_lines3= Line(Point(temp,20),Point(temp+4,20))
        gnd_lines3.setWidth(5)
        gnd_lines3.setFill("white")
        temp=temp+10
        gnd_lines1.draw(win)
        gnd_lines2.draw(win)
        gnd_lines3.draw(win)

    sun = Circle(Point(37,38), 1.5)
    sun.setFill("yellow")
    sun.setOutline("yellow")
    sun.draw(win)

    with open('hw5_input.txt','r') as file:
     # reading each line
        for line in file:
            coordinates=[]
            # reading each word
            for word in line.split():
             # displaying the words
                coordinates.append(word)
            draw_buildings(win,coordinates[0],coordinates[1],coordinates[2],coordinates[3],coordinates[4])


    button = Rectangle(Point(2,2), Point(6, 4))
    button.setFill("gray")
    button.draw(win)
    label = Text(Point(4, 3), "Start")
    label.setStyle("bold")
    label.setTextColor("white")
    label.draw(win)

    bottom_message = Text(Point(12, 5), "Please click the Start button to begin")
    bottom_message.setStyle("bold")
    bottom_message.setTextColor("green")
    bottom_message.draw(win)
    car_on_screen_message = Text(Point(15, 27), "")
    car_on_screen_message.setStyle("bold")
    car_on_screen_message.setTextColor("purple")
    car_on_screen_message.draw(win)
    score_title = Text(Point(15, 3), "Current Score: ")
    score_title.setStyle("bold")
    score_title.setSize(18)
    score_title.setTextColor("blue")
    score_title.draw(win)
    score_message = Text(Point(21, 3), "0")
    score_message.setStyle("bold")
    score_message.setSize(18)
    score_message.setTextColor("blue")
    score_message.draw(win)
    clicked_colors_message = Text(Point(29, 5), "")
    clicked_colors_message.setStyle("bold")
    clicked_colors_message.setTextColor("black")
    clicked_colors_message.draw(win)

    exit_bg = Rectangle(Point(10,5), Point(30, 20))
    exit_bg.setFill("light gray")
    exit_message = Text(Point(20, 15), "Click Exit to stop \n or Resume to continue")
    exit_message.setSize(18)
    exit_message.setStyle("bold")
    exit_message.setTextColor("red")
    confirm_label = Text(Point(15, 8), "Exit")
    confirm_label.setStyle("bold")
    confirm_label.setTextColor("white")
    go_back_button = Rectangle(Point(23, 7), Point(27, 9))
    go_back_button.setFill("gray")
    go_back_label = Text(Point(25, 8), "Resume")
    go_back_label.setStyle("bold")
    go_back_label.setTextColor("white")

    mylabel=Text(Point(26,3),"Clicked Color:")
    mylabel.setStyle("bold")
    mylabel.draw(win)
    myrectangle=Rectangle(Point(29,2),Point(31,4))
    myrectangle.draw(win)

    ###
    bottom_message2 = Text(Point(12,5), "Click a moving car or Pause to stop")
    bottom_message2.setStyle("bold")
    bottom_message2.setFill("green")
    pause_label = Text(Point(4, 3), "Pause")
    pause_label.setStyle("bold")
    pause_label.setTextColor("white")
    
    pixel_per_second = 10
    refresh_sec = 0.05
    gameState = 0 # 0 for initial mode, 1 for start mode, 2 for pause mode
    total_score = 0
    carlist = []
    clicked_colors = {}
    
    
    start_time1 = 0
    start_time2 = 0
    clickedCounter = 0


    while True:
        pClick = win.checkMouse()
       
        if gameState == 0: #initial
            time.sleep(0.1)
            if pClick != None:
                bottom_message.undraw()
                bottom_message2.draw(win)
                label.undraw()
                pause_label.draw(win)  
                if isClicked(pClick, button):
                    gameState = 1
                            
                                                            
        elif gameState == 1: #start
            if pClick != None:
                if isClicked(pClick,button):
                    exit_bg.draw(win)
                    exit_message.draw(win)
                    confirm_button = Rectangle(Point(13, 7), Point(17, 9))
                    confirm_button.setFill("gray")
                    confirm_button.draw(win)
                    confirm_label.draw(win)
                    go_back_button.draw(win)
                    go_back_label.draw(win)
                    gameState = 2
                else:
                    for remove in carlist:
                        if isClicked(pClick,remove.carBody):
                            remove.undraw()
                            clickedCounter = clickedCounter + remove.getScore()
                            score_message.setText(clickedCounter)
                            myrectangle.setFill(remove.getColor())
                            color_number_text = []

                            clicked_colors[remove.getColor()] = clicked_colors.get(remove.getColor(),0)+1

                            for colors,numbers in enumerate(clicked_colors):
                                color_number_text.append(numbers+" "+str(clicked_colors[numbers]))
                                joined_text = ", ".join(color_number_text)
                                clicked_colors_message.setText(joined_text)
                                
                                

                

                        
                        
    
    
                            
                            
                            
                                  

            current_time = time.time()
            if (current_time - start_time1) >= 0.2:
                x = random.random()
                x = x - 0.5 + 4
                y = random.uniform(7,23)
                unit = random.random()
                unit = unit * 0.6
                unit = 0.4 + unit
                car = Car(win,x,y,unit)
                carlist.append(car)
                start_time1 = current_time+1

            if current_time - start_time2 >= refresh_sec:
                for i in carlist:
                    i.move(pixel_per_second*refresh_sec)
                    if i.carBody.getP1().getX()>40:
                        i.undraw()
                    


        elif gameState == 2:
            time.sleep(0.1)
            if pClick != None:
                if isClicked(pClick,confirm_button):
                    win.close()
                elif isClicked(pClick,go_back_button):
                    exit_bg.undraw()
                    exit_message.undraw()
                    confirm_button.undraw()
                    confirm_label.undraw()
                    go_back_button.undraw()
                    go_back_label.undraw()
                    gameState = 1
                    

if __name__ == '__main__':
    main()

        

        

