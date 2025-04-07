"""
Program Name:Challenge4
Author: Jaime Torres
Last Date Modified: 8/6/2024

Purpose: The purpose of this program is to allow the user to create a stickman scene
one to four time while still being allowed to change the colors every time the image
is created. 
"""

import turtle  #This Imports the turtle module.

t = turtle.Turtle()#This defines the turtle module for use.

screen = turtle.Screen() #This defines the turtle window that will be used for the output.
screen.setup(width=1500, height=700) #This sets the turtle window to a set size specific for the drawing function.
t.up() #This ensures no drawing is done until it is intended.

print("***************************************************************")#This is aesthetic and will appear again in between certain sequences.
print("Hello! This program will use Turtle to create a Stickman scene.") #This explains to the user what the program does.
print("He will be on grass standing next to a tree waving at you.") #This explains the output.
print("He'll be waving at you once you decide the colors you want to use!") #This lets the user know what needs to done next.
input("Press enter to get started!")#After the user has read everything for the introdusction message, they will hit enter to proceed.
print("***************************************************************")


#Below is the stickman scene function. This will draw the image the user is using this program for.
def stickmanscene():
    
    colorprompt()#The color prompt is seperated for debugging purposes. This is to allow a seperate function to stop invalid color inputs by the user.
    
    print("^^^^^^Colors for previous image set^^^^^^")#After the color prompt has been set by the user, This line will print help the user understand where they are in the
                                                      #program if they manage to get lose their place by the amount of wrong inputs they're entering.
    print("Switch over to the Turtle Graphics Window")#The turtle window will be behind the program terminal.
    
    t.up() #This is a safeguard to prevent any unintended drawing between drawing sets.
    
    t.pencolor(usercolor) #obtained in the color prompt, this is the first color selected.
    
    t.width(5) #Pen pixel width is set to 5 pixels.

    #This will draw the head of the stickman.
    t.down() #This will put the turtle's tail/pen down on the canvas.
    t.circle(25) #With a diameter of 25, the circle(head) is created.
    t.up #The tail/pen is lifted.
    
    #Everything below here is the stickman body. The limbs are identified.
    t.setheading(270)#Heading faces south/down toward the body.
    t.down()#The pen/tail is down on the canvas.
    t.forward(25)#This is the Neck.
    t.setheading(45)#The heading faces northeast.
    t.forward(38)#This is the right arm(waving arm).
    t.setheading(225)#Heading faces southwest.
    t.forward(38)#Returns to body.
    t.setheading(180)#Heading faces west.
    t.forward(38)#This is the left arm.
    t.setheading(0)#Heading faces east.
    t.forward(38)#Returns to body.
    t.setheading(270)#Heading faces south.
    t.forward(45)#This is the torso/body.
    t.setheading(240)#Heading faces south west.
    t.forward(38)#This is the left leg.
    t.setheading(60)#Heading faces northwest.
    t.forward(38)#Returns to body.
    t.setheading(300)#Heading faces southeast.
    t.forward(38)#This is the right leg.
    t.up() #The pen is lifted off the canvas.

    #Below is a reposition for the tree.
    
    t.setheading(180) #The heading is facing west.
    t.forward(160) #The turtle moves 160 pixels left.

    #Below is the tree drawing
    t.pencolor(usercolor3) #This is the color chosen by the color prompt function.
    t.down() #This begins drawing the trunk.
    t.setheading(90)#The direction is north/up.
    t.forward(150) #From the bottom of trunk to the top of the tree is 150 pixels.

    #Below is the tree top. These angles are 60 degrees for each corner and even sides.
    t.setheading(180) #Faces west/left.
    t.forward(75) #Half of side one is complete
    t.setheading(60) #Heading set to 60 degrees northeast.
    t.forward(150) #Side 2 is complete
    t.setheading(300) #Heading set to 300 degrees southeast.
    t.forward(150) #Side 3 is complete.
    t.setheading(180) #Heading is set back to 180 degrees west/left.
    t.forward(75) #Second half of side 1 is done.
    t.setheading(270)#The turtle faces back to the grass start point.
    t.forward(150) #The turtle returns to the grass start point.

    #Below is the grass section.
    t.setheading(180)#The turtle faces west/left.
    t.pencolor(usercolor2)#The pen color changes to the input for the grass color.
    t.down()#The pen is on the canvas.
    t.forward(150)#The left side of the grass is done.
    t.setheading(0)#The turtle faces east/right.
    t.forward(350)#The right side of the grass is done.
    t.up()#The pen is lifted from the canvas.
    #DO NOT DELETE. Below line of code is critical to the 'for' loops.
    t.sety(0)# This will reset only the 'y' coordinate to 0.

#Below is the color prompt of all the colors that will be used.
def colorprompt():
    #This 'global' line is needed to allow these color input values to be used in the stickman scene.
    global usercolor, usercolor2, usercolor3
    #The user is advised on the colors that may be used in this program.
    print("Type from one of these color choices:\n 'red', 'blue', 'green', 'black', 'purple', 'brown', 'yellow', 'orange'.")
    #For reasons related to printing a reasonable length list of colors, only these colors may be chosen.
    validcolors = {'red', 'blue', 'green', 'black', 'purple', 'brown', 'yellow', 'orange'}
    #below is the prompt that is to be defined when choosing the colors.
    def getvalidcolor(prompt):
        while True:#While true is necessary to prevent an invalid input causing an error.
            color = input(prompt).strip().lower()#The input is stripped and set to lowercase to match the color options.
            if color in validcolors:#If the color is in the valid colors the following will happen.
                return color #color is chosen and value is returned to a 'True' value.
            else:#All other inputs are invalid and may cause an error if allowed.
                print("Invalid input. Try again.")#The user is made aware of the invalid input.

    #Stickman, grass and tree colors are below. Using 'get' they will utilize the validcolors variable.
    usercolor = getvalidcolor("Please type a color for the stickman.\nYour Choice: ")
    usercolor2 = getvalidcolor("Please type a color for the grass.\nYour Choice: ")
    usercolor3 = getvalidcolor("Please type a color for the tree.\nYour Choice: ")

    return  usercolor, usercolor2, usercolor3 #All 3 colors are returned here and the 'global' line of code allows these to not get stuck in this function.

#The below function conatins loops for the user input. To avoid repitition, the major components are explained in the first two 'if' statements. The subesequent statements will
#annotate any changes that differ with their above 'if' variations.
#Below, the user is asked for how many stickman scenes they would like.
def main():
    global userinputdrawings #This allows the user input to be used outside of this function, to be used in other functions.
    
    userinputdrawings = input("Please enter between 1-4 how many scenes you want to have in this image.\nYour Choice:")
    print("***************************************************************")

    if userinputdrawings == "1":#The user selects '1' scene.
        t.goto(0,0)#The scene starts at the center of the canvas.
        stickmanscene() #The scene is pulled once.
        print("The Scene is done!")#The output lets the user know that the sequence is done.
        print("Lookover the image and have a look at what you made!")#The user is reminded to look at the scene if they never switched windows.
        print("**************************************************")#This is aesthetic.
        print("You may now close the program.")#The program is finished and the user may close it.
        
    elif userinputdrawings == "2":#This is for '2' scenes to be made.
        t.goto(-500,0)#The scene is moved farther left to center it more.
        for i in range(2):#A for loop is created for repeated actions using a range. All scene counts >1 will have a 'for' loop.
            t.up()#The pen/tail is off the canvas to avoid any mistakes in the code before drawing.
            t.forward(225)#Before every scene, the drawing is moved 225 pixels right to avoid any 'bad' overlap in scenes.
            stickmanscene()#The stickman scene is called and depending the range provided, will be repeated.
        print("The Scene is done!")
        print("Lookover the image and have a look at what you made!")
        print("**************************************************")
        print("You may now close the program.")
    elif userinputdrawings == "3":#The user selects 3 stickman scenes.
        t.goto(-500,0)
        for i in range(3):#range reflects input by user.
            t.up()
            t.forward(225)
            stickmanscene()
        print("The Scene is done!")
        print("Lookover the image and have a look at what you made!")
        print("**************************************************")
        print("You may now close the program.")
    elif userinputdrawings == "4":#The user selects 4 stickman scenes, the largest one allowed.
        t.goto(-550,0)#This will move the scene over farthest left of the others to fit all 4 sequences.
        for i in range(4):#Range reflects input by user.
            t.up()
            t.forward(225)
            stickmanscene()
        print("The Scene is done!")
        print("Lookover the image and have a look at what you made!")
        print("**************************************************")
        print("You may now close the program.")
    else:
        print("Try again, please input an integer between 1 and 4.")#If the user mistyped or tried putting a larger number, this is stopped and they are let known.


if __name__ == '__main__':#DO NOT DELETE.
    main()
#END OF PROGRAM.
