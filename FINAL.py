#Annie Zhang and Anne Wang
#Fireboy and Watergirl
#Due: June 15, 2018

from pygame import*
screen=display.set_mode((895,598))

#Character starting positions
X,Y=40,537
GX, GY= 40, 455
X2,Y2= 60, 537
GX2,GY2= 35, 537
X3,Y3= 110, 530
GX3,GY3= 820, 70

myClock= time.Clock()
import time as t
levelonetime=0
leveltwotime=0
levelthreetime=0

jumpstate= "standing"
jumpstateg="standing"
currentscreen="titlescreen"
levelcomplete= False
pausescreen=False
levelone= False
leveltwo= False
levelthree= False

#music and sound effects:
#ping= mixer.Sound("audio/gemcollect.mp3")
init()
font.init()
font= font.SysFont("Castellar", 30)
mixer.music.load("audio/FireboyWatergirlRemix.mp3")
mixer.music.play()

#CHARACTERS__________________________________________________________________________________
#choosing character screen
ponchorect=Rect(60, 100, 160, 250)
dressrect=Rect(285, 328, 135, 265)
satchelrect=Rect(492, 100, 128, 258)
suitrect=Rect(683, 330, 140, 248)
ponchoglow= image.load("character/ponchoglow.png")
dressglow= image.load("character/dressglow.png")
satchelglow= image.load("character/satchelglow.png")
suitglow= image.load("character/suitglow.png")

ponchogirl=True
satchelboy=True

#for walking sprites
frame= 0
framewait= 0
frameg= 0
framegwait= 0

#Fireboy:
boystate= "standing"
satchelright= [] #this list will contain the walking sprites and will be looped through to print each one
satchelleft= [] #same as above
for i in range (4):
    satchelright.append(transform.scale(image.load("character/satchelright"+str(i)+".png"), (25, 33)))
for i in range (4):
    satchelleft.append(transform.scale(image.load("character/satchelleft"+str(i)+".png"), (25, 33)))
satchelupright= transform.scale(image.load("character/satchelupright.png"), (25, 33))
satchelupleft= transform.scale(image.load("character/satchelupleft.png"), (25, 35))
satchelup= transform.scale(image.load("character/satchelup.png"), (25, 33))
dyingb= transform.scale(image.load("character/deadboy.png"), (25,33))
satchelstand= transform.scale(image.load("character/satchelstand.png"), (25, 33))

suitright=[] #same as walking fireboy sprites
suitleft=[]
for i in range (4):
    suitright.append(transform.scale(image.load("character/suitright"+str(i)+".png"), (25, 33)))
for i in range (4):
    suitleft.append(transform.scale(image.load("character/suitleft"+str(i)+".png"), (25, 33)))
suitupright= transform.scale(image.load("character/suitupright.png"), (25, 33))
suitupleft= transform.scale(image.load("character/suitupleft.png"), (25, 35))
suitup= transform.scale(image.load("character/suitup.png"), (25, 33))
suitstand= transform.scale(image.load("character/suitstand.png"), (25, 33))

#Watergirl
girlstate= "standing"
ponchoright= []
poncholeft= []
for i in range (4):
    ponchoright.append(transform.scale(image.load("character/ponchoright"+str(i)+".png"), (25, 33)))
for i in range (4):
    poncholeft.append(transform.scale(image.load("character/poncholeft"+str(i)+".png"), (23, 33)))
ponchoupright= transform.scale(image.load("character/ponchoupright.png"), (25, 38))
ponchoupleft= transform.scale(image.load("character/ponchoupleft.png"), (25, 38))
ponchoup= transform.scale(image.load("character/ponchoup.png"), (25, 33))
dyingg= transform.scale(image.load("character/deadgirl.png"), (25, 33))
ponchostand= transform.scale(image.load("character/ponchostand.png"), (25, 33))

dressright= []
dressleft= []
for i in range (4):
    dressright.append(transform.scale(image.load("character/dressright"+str(i)+".png"), (25, 33)))
for i in range (4):
    dressleft.append(transform.scale(image.load("character/dressleft"+str(i)+".png"), (23, 33)))
dressupright= transform.scale(image.load("character/dressupright.png"), (25, 38))
dressupleft= transform.scale(image.load("character/dressupleft.png"), (25, 38))
dressup= transform.scale(image.load("character/dressup.png"), (25, 33))
dressstand= transform.scale(image.load("character/dressstand.png"), (25, 33))

#____________________________________________________________________________________________________
#LOADING IMAGES
    #titlescreen:
title= image.load("misc/title.jpg")
title=transform.scale(title, (895, 600))
start= image.load("level1/start.png")
startbutton= transform.scale(start, (142, 65))
startb= Rect(426, 443, 135, 58)
    #instructionscreen:
instructionrect=Rect(345, 522, 135, 65)
instructionb= image.load("misc/howtoplay.png")
instructions= image.load("misc/instructions.jpg")
    #characterscreen:
characterrect= Rect(513, 522, 135, 65)
characters= image.load("character/selectchara.jpg")
charactersb= image.load("misc/select.png")

gobackrect= Rect(20, 499, 133, 90)
gobackb= image.load("misc/back.png")           
    #levelscreen:
levelselect= image.load("levelselect/levelselect.jpg")
one= image.load("levelselect/one.png")
two= image.load("levelselect/two.png")
three= image.load("levelselect/three.png")
rectone= Rect(387, 109, 98, 98)
recttwo= Rect(256, 319, 103, 100)
rectthree= Rect(519, 319, 103, 100)
    #pausescreen:
pauserect= Rect(835, 542, 35, 46)
pause= image.load("misc/pausescreen.png")
pauseb= image.load("misc/pause.png")
pauseb2= image.load("misc/pause2.png")
resumerect= Rect(366, 216, 154, 35)
resume= image.load("misc/resume.png")
    #gameover screen:
gameoverim= image.load("misc/gameover.png")
retrymenu= image.load("misc/retrymenu.png")
backmenu= image.load("misc/backmenu.png")
    #levelcomplete screen:
lvlcomp= image.load("misc/complete.png")
continuepic= image.load("misc/continue.png")
continuepic= transform.scale(continuepic,(160, 35))

retryrect= Rect(303, 265, 271, 37)
retryrect2= Rect(305, 270, 270, 35)
backrect= Rect(351, 338, 177, 70)
backrect2= Rect(348, 338, 175, 65)
#_________________________________________________________________________________

#LEVEL ONE INFO
lvl1back = transform.scale(image.load("level1/level1back.jpg"), (895,600)).convert()

#Creating walls:
grid= open("level1/txtbackground.txt").read().strip().split("\n")
walls=[]
buttons= {}
for n in range(len(grid)):
    for i in range (len(grid[n])):
        if grid[n][i] == "w" :
            walls.append(Rect(i*27, n*26, 27, 26)) #each character in textfile reps a 27*26 rectangle of wall or open space
        if grid[n][i].isdigit() and grid[n][i]!="0":
            walls.append(Rect(i*27, n*26, 27, 26))
            if grid[n][i] not in buttons:
                buttons[grid[n][i]] = []
            buttons[grid[n][i]].append(Rect(i*27, n*26, 27, 26)) 

#where each character cannot go
reddead=[]
for n in range(len(grid)):
    for i in range (len(grid[n])):
        if grid [n][i] == "B" or grid[n][i]=="G":
            reddead.append(Rect(i*27, n*26+5, 26, 26))
bluedead=[]
for n in range(len(grid)):
    for i in range (len(grid[n])):
        if grid [n][i] == "R" or grid[n][i]=="G":
            bluedead.append(Rect(i*27, n*26+5, 26, 26))

waterdoor= Rect(717, 65, 60, 45)
firedoor= Rect(785, 65, 60, 45)

#gems and their positions
gems= [[450,535], [630,535], [163,269], [530,288],
       [231,43], [47, 105], [417, 80], [507, 80]]
gemcolour=["red", "blue", "red", "blue", "red", "blue", "red", "blue"] 
gemim= {"red":transform.scale(image.load("misc/firegem.png"), (25, 25)), "blue":transform.scale(image.load("misc/watergem.png"), (25, 25))}

#MOVING PLATFORMS
slideim= image.load("level1/slidey.png")
slide= transform.scale(slideim, (70, 20))
button= image.load("level1/button.png")
button= transform.scale(button, (30, 15))
buttonpressed= image.load("level1/buttond.png")
buttonpressed= transform.scale(buttonpressed, (30, 15))
#needed help: 
movingplat= {"1":[Rect(793, 234, 65, 17), False]} #false means not stepping on button
maxmin= [[26*9, 26*13]] #this gives the maxmimum and minimum hieght the moving platforms can go
direction= ["down"]
#___________________________________________________________________________________________________
#LEVEL TWO INFO
lvl2back = transform.scale(image.load("level2/level2.jpg"), (895,600)).convert()

grid2= open("level2/txtbackground2.txt").read().strip().split("\n")
walls2=[]
buttons2= {}
for n in range(len(grid2)):
    for i in range (len(grid2[n])):
        if grid2[n][i] == "w" :
            walls2.append(Rect(i*27, n*26, 27, 26))
    #BUTTONS 2 AND 3 CONTROL SAME TWO PLATFORMS
        elif grid2[n][i]=="2":
            walls2.append(Rect(i*27, n*26, 27, 26))
            if grid2[n][i] not in buttons2:
                buttons2[grid2[n][i]]=[]
                buttons2["3"]=[]
            buttons2[grid2[n][i]].append(Rect(i*27, n*26, 27, 26))
            buttons2["3"].append(Rect(i*27, n*26, 27, 26))
            
        if grid2[n][i].isdigit() and grid2[n][i]!="0":
            walls2.append(Rect(i*27, n*26, 27, 26))
            if grid2[n][i] not in buttons2:
                buttons2[grid2[n][i]] = []
            buttons2[grid2[n][i]].append(Rect(i*27, n*26, 27, 26))

reddead2=[]
for n in range(len(grid2)):
    for i in range (len(grid2[n])):
        if grid2[n][i] == "B" or grid2[n][i]=="G":
            reddead2.append(Rect(i*27, n*26+3, 27, 26))
bluedead2=[]
for n in range(len(grid2)):
    for i in range (len(grid2[n])):
        if grid2[n][i] == "F" or grid2[n][i]=="G":
            bluedead2.append(Rect(i*27, n*26+3, 27, 26))

waterdoor2= Rect(27*2, 26*2, 27, 26*2)
firedoor2= Rect(27*5, 26*2, 27, 26*2)

gems2= [[182,545], [250,545], [182,480], [250,480],
        [555,545], [618,545], [555,480], [618,480],
        [645,388], [530,388], [343,388], [230,388],
        [284,150], [413,265], [462,265], [586,150],
        [380,59], [337,59]]
gemcolour2=["red", "red", "blue", "blue",
            "blue", "blue", "red", "red",
            "red", "blue", "red", "blue",
            "red", "red", "blue", "blue",
            "blue", "red"] 
gemim2= {"red":transform.scale(image.load("misc/firegem.png"), (25, 25)), "blue":transform.scale(image.load("misc/watergem.png"), (25, 25))}

#MOVING PLATFORMS
slide21= transform.scale(image.load("level2/slidey21.png"), (18,81))
slide22= transform.scale(image.load("level2/slidey22.png"), (80,17))

movingplat2= {"1":[Rect(440, 362, 22, 77), False], "2":[Rect(255, 270, 63, 21),False],
               "3":[Rect(562, 270, 63, 21),False], "4":[Rect(390, 118, 63, 21),False]}
maxmin2= [[295, 362],[200, 270], [200,270], [390, 500]]
direction2= ["up", "down", "down", "right"]

#_______________________________________________________________________________
#LEVEL THREE INFO
lvl3back = transform.scale(image.load("level3/level3.jpg"), (895,600)).convert()

#Creating walls
grid3= open("level3/txtbackground3.txt").read().strip().split("\n")
walls3=[]
buttons3= {}
for n in range(len(grid3)):
    for i in range (len(grid3[n])):
        if grid3[n][i] == "w" :
            walls3.append(Rect(i*27, n*26, 27, 26))
        if grid3[n][i].isdigit() and grid3[n][i]!="0":
            walls3.append(Rect(i*27, n*26, 27, 26))
            if grid3[n][i] not in buttons3:
                buttons3[grid3[n][i]] = []
            buttons3[grid3[n][i]].append(Rect(i*27, n*26, 27, 26))

reddead3=[]
for n in range(len(grid3)):
    for i in range (len(grid3[n])):
        if grid3[n][i] == "B" or grid3[n][i]=="G":
            reddead3.append(Rect(i*27, n*26+5, 26, 26))
bluedead3=[]
for n in range(len(grid3)):
    for i in range (len(grid3[n])):
        if grid3[n][i] == "F" or grid3[n][i]=="G":
            bluedead3.append(Rect(i*27, n*26+5, 27, 26))

waterdoor3= Rect(27*4, 26*15, 27, 26*2)
firedoor3= Rect(27*7, 26*15, 27, 26*2)

gems3= [[642, 162], [642, 265], [45, 395], [45, 285], [45, 45],
        [828, 305], [560, 450], [515, 450], [122,140],
        [345, 305], [440, 405], [363, 485],
        [820, 130]]
gemcolour3=["blue", "blue", "red", "red", "red",
            "blue", "blue", "red", "red",
            "red", "blue", "red",
            "red"]
gemim3= {"red":transform.scale(image.load("misc/firegem.png"), (25, 25)), "blue":transform.scale(image.load("misc/watergem.png"), (25, 25))}

#MOVING PLATFORMS
slide31= transform.scale(image.load("level2/slidey22.png"), (58,18))
slide32= transform.scale(image.load("level2/slidey21.png"), (17, 83))
movingplat3= {"1":[Rect(28, 575, 58, 18), False], "2":[Rect(165,23,17,83), False]}
maxmin3= [[78, 575], [23, 82]]
direction3= ["up", "down"]
#___________________________________________________________________________________________________
#FUNCTIONS

def collide(oldpos, newpos, walls, buttons, movingwalls1):
    newrect= Rect(newpos[0], newpos[1], 25, 33)#finds new position of character
    charrect= Rect(newpos[0], newpos[1]+1, 25, 33) #charrect checks if colliding with button (button is in ground)
    for keyy,rectlist in buttons.items(): #key is num in grid before the colon, rectlist is rect + true/false
        for rect in rectlist:
            if rect.colliderect(charrect):
                movingwalls1[keyy][-1]=True #if standing on button, then True
    for i in walls: 
        if i.colliderect(newrect):
            return oldpos #if hitting a wall, don't go to new position
    for rect in list(movingwalls1.values()): #if hitting a moving platform
        if rect[0].colliderect(newrect):
            return oldpos
    return newpos #if hitting nothing, able to go to new position


#NEEDED HELP:
def movingplatform(movinglist, maxmin, direction):
    for key,rectlist in movinglist.items():
        index=int(key)-1 #index starts at zero, our key starts at 1
        if direction[index] == "down": #checks which direction platform is moving when button is pressed
            if rectlist[-1] and rectlist[0].top < maxmin[int(key)-1][1]: #if the character is standing on the button and
                                                                          #if the moving platform is not past the max,
                                                                          #continue adding 1 to move it down
                xrect, yrect, wrect, hrect = rectlist[0]
                movinglist[key] = [Rect(xrect, yrect+2, wrect, hrect), True]
            elif rectlist[-1]==False and rectlist[0].top > maxmin[int(key)-1][0]:  #if character is not on button,
                                                                                   #platform should move back to the default min
                                                                                   #minimum height
                xrect, yrect, wrect, hrect = rectlist[0]
                movinglist[key] = [Rect(xrect, yrect-2, wrect, hrect), False]
                                                                                    
        if direction[index]=="up":      #if platform moves down when button is pressed
            if rectlist[-1] and rectlist[0].top > maxmin[int(key)-1][0]: 
                xrect, yrect, wrect, hrect = rectlist[0]
                movinglist[key] = [Rect(xrect, yrect-2, wrect, hrect), True]
            elif rectlist[-1]==False and rectlist[0].top < maxmin[int(key)-1][1]:
                xrect, yrect, wrect, hrect = rectlist[0]
                movinglist[key] = [Rect(xrect, yrect+2, wrect, hrect), False]
                
        if direction[index]=="right":   #if platform moves right when button is pressed
            if rectlist[-1] and rectlist[0].right < maxmin[int(key)-1][1]:
                xrect, yrect, wrect, hrect = rectlist[0]
                movinglist[key] = [Rect(xrect+2, yrect, wrect, hrect), True]
            elif rectlist[-1]==False and rectlist[0].right > maxmin[int(key)-1][0]:
                xrect, yrect, wrect, hrect = rectlist[0]
                movinglist[key] = [Rect(xrect-2, yrect, wrect, hrect), False]

        if direction[index]=="left":    #if platform moves left when button is pressed
            if rectlist[-1] and rectlist[0].left >maxmin[int(key)-1][1]:
                xrect, yrect, wrect, hrect = rectlist[0]
                movinglist[key] = [Rect(xrect-2, yrect, wrect, hrect), True]
            elif rectlist[-1]==False and rectlist[0].left > maxmin[int(key)-1][0]:
                xrect, yrect, wrect, hrect = rectlist[0]
                movinglist[key] = [Rect(xrect+2, yrect, wrect, hrect), False]

def checkboydead(X,Y,reddead):
    global boystate #checks if the boy has died
    boypos= [(X, Y), (X+25, Y), (X, Y+33),(X+25, Y+33)] #all four corners of boy rect
    for i in range (len(reddead)):
        for n in range (len(boypos)):
            if (reddead[i]).collidepoint(boypos[n]): #if any boy corners are colliding with
                boystate="dead"                     #blue or green, state changes

def checkgirldead(GX, GY, bluedead):
    global girlstate #checks if girl has died
    girlpos= [(GX, GY+33), (GX, GY+10), (GX+25, GY+33), (GX+25, GY+10)]
    for i in range (len(bluedead)):
        for n in range (len(girlpos)):
            if (bluedead[i]).collidepoint(girlpos[n]):
                girlstate="dead"
                
def moveboy(movingwalls1):
    global X,Y, vY
    global jumpstate, boystate
    oldpos= (X,Y)
    keys = key.get_pressed() #MOVING LEFT
    if keys[K_LEFT]:
        X-=4.75
        boystate= "moveleft" 
    elif keys[K_RIGHT]:   #MOVING RIGHT
        X+=4.75
        boystate= "moveright"
    else:
        boystate= "standing"
    newpos= (X, Y) #every time X,Y moves, must check if you are able to move there
    postomove= collide(oldpos, newpos, walls, buttons, movingwalls1) #this checks colliding
    X, Y = postomove #uses checked position as new X,Y
    #jumping: (needed some help)
    if collide(oldpos, [oldpos[0],oldpos[1]+1], walls, buttons, movingwalls1) == [oldpos[0],oldpos[1]+1] and jumpstate!="jump": #if character is falling down
        jumpstate="jump" #change state to change sprite
        vY=0
    if keys[K_UP] and jumpstate!="jump": #if user jumps up
        jumpstate="jump"
        vY= -5.9 #moves up
    if jumpstate =="jump":
        Y+=vY
        vY+=0.2 #gradually makes vY closer to 0 to stop the jump
        newpos= (X,Y)
        (X,Y) = collide(oldpos, newpos, walls, buttons, movingwalls1) #uses most recently checked X,Y 
        if (X,Y)==oldpos and oldpos[1]<newpos[1]:
          jumpstate="standing"  #if chaacter moved up to new platform
        if (X,Y) ==oldpos and oldpos[1]>newpos[1]:
            vY =0  #if character cannot move up, don't allow it to jump
    charrect= Rect(X,Y,25,33)
    for keyy,rectlist in movingwalls1.items():  #if colliding with a moving platform that moves up and down, 
        if (charrect).colliderect(rectlist[0]): #character should be moving with the platform
            Y-=2                                #speed of platform is same as what is being subtracted to the Y vallue

def movegirl(movingwalls1):
    global GX, GY, vYg
    global girlstate, jumpstateg
    oldpos=(GX,GY)
    keys = key.get_pressed()
    if keys[K_a]:
        GX-= 4.75
        girlstate= "moveleft"
    elif keys[K_d]:
        GX+=4.75
        girlstate= "moveright"
    else:
        girlstate= "standing"
    newpos= (GX, GY)
    gpostomove= collide(oldpos, newpos, walls, buttons, movingwalls1)
    GX, GY= gpostomove
    if collide(oldpos, [oldpos[0],oldpos[1]+1], walls, buttons, movingwalls1) == [oldpos[0],oldpos[1]+1] and jumpstateg!="jump":
        jumpstateg="jump"
        vYg=0
    if keys[K_w] and jumpstateg!="jump":
        jumpstateg = "jump"
        vYg=-5.9
    if jumpstateg =="jump":
        GY += vYg
        vYg+=0.2
        newpos= (GX,GY)
        (GX,GY) = collide(oldpos, newpos, walls, buttons, movingwalls1)
        if (GX,GY)==oldpos and oldpos[1]<newpos[1]:
          jumpstateg="standing"
        if (GX,GY) ==oldpos and oldpos[1]>newpos[1]:
            vYg =0
    charrect= Rect(GX,GY,25,33)
    for keyy,rectlist in movingwalls1.items():
        if (charrect).colliderect(rectlist[0]):
            GY-=2

def moveboy2(movingwalls):
    global X2, Y2, vY
    global jumpstate, boystate
    oldpos= (X2,Y2)
    keys = key.get_pressed()
    if keys[K_LEFT]:
        X2-= 2.65
        boystate= "moveleft"
    elif keys[K_RIGHT]:
        X2+= 2.65
        boystate= "moveright"
    else:
        boystate= "standing"
    newpos= (X2, Y2)
    postomove= collide(oldpos, newpos, walls2, buttons2, movingwalls)
    X2, Y2 = postomove
    #jumping: (needed some help)
    if collide(oldpos, [oldpos[0],oldpos[1]+1], walls2, buttons2, movingwalls) == [oldpos[0],oldpos[1]+1] and jumpstate!="jump":
        jumpstate="jump"
        vY=0
    if keys[K_UP] and jumpstate!="jump":
        jumpstate="jump"
        vY=-5.9
    if jumpstate =="jump":
        Y2+=vY
        vY+=0.2
        newpos= (X2,Y2)
        (X2,Y2) = collide(oldpos, newpos, walls2, buttons2, movingwalls)
        if (X2,Y2)==oldpos and oldpos[1]<newpos[1]:
          jumpstate="standing"
        if (X2,Y2) ==oldpos and oldpos[1]>newpos[1]:
            vY =0
    charrect= Rect(X2,Y2,25,33)
    for keyy,rectlist in movingwalls.items():  #if colliding with a moving platform that moves up and down, 
        if (charrect).colliderect(rectlist[0]): #character should be moving with the platform
            Y2-=2            

def movegirl2(movingwalls):
    global GX2, GY2, vYg
    global girlstate, jumpstateg
    oldpos=(GX2,GY2)
    keys = key.get_pressed()
    if keys[K_a]:
        GX2-= 2.65
        girlstate= "moveleft"
    elif keys[K_d]:
        GX2+= 2.65
        girlstate= "moveright"
    else:
        girlstate= "standing"
    newpos= (GX2, GY2)
    gpostomove= collide(oldpos, newpos, walls2, buttons2, movingwalls)
    GX2, GY2= gpostomove
    if collide(oldpos, [oldpos[0],oldpos[1]+1], walls2, buttons2, movingwalls) == [oldpos[0],oldpos[1]+1] and jumpstateg!="jump":
        jumpstateg="jump"
        vYg=0
    if keys[K_w] and jumpstateg!="jump":
        jumpstateg = "jump"
        vYg=-5.5
    if jumpstateg =="jump":
        GY2 += vYg
        vYg+=0.2
        newpos= (GX2,GY2)
        (GX2,GY2) = collide(oldpos, newpos, walls2, buttons, movingwalls)
        if (GX2,GY2)==oldpos and oldpos[1]<newpos[1]:
          jumpstateg="standing"
        if (GX2,GY2) ==oldpos and oldpos[1]>newpos[1]:
            vYg =0
    charrect= Rect(GX2,GY2,25,33)
    for keyy,rectlist in movingwalls.items():  #if colliding with a moving platform that moves up and down, 
        if (charrect).colliderect(rectlist[0]): #character should be moving with the platform
            GY2-=2

def moveboy3(movingwalls):
    global X3, Y3, vY
    global jumpstate, boystate
    oldpos= (X3,Y3)
    keys = key.get_pressed()
    if keys[K_LEFT]:
        X3-= 4.2
        boystate= "moveleft"
    elif keys[K_RIGHT]:
        X3+= 4.2
        boystate= "moveright"
    else:
        boystate= "standing"
    newpos= (X3, Y3)
    postomove= collide(oldpos, newpos, walls3, buttons3, movingwalls)
    X3, Y3 = postomove
    #jumping: (needed some help)
    if collide(oldpos, [oldpos[0],oldpos[1]+1], walls3, buttons3, movingwalls) == [oldpos[0],oldpos[1]+1] and jumpstate!="jump":
        jumpstate="jump"
        vY=0
    if keys[K_UP] and jumpstate!="jump":
        jumpstate="jump"
        vY=-5.5
    if jumpstate =="jump":
        Y3+=vY
        vY+=0.2
        newpos= (X3,Y3)
        (X3,Y3) = collide(oldpos, newpos, walls3, buttons3, movingwalls)
        if (X3,Y3)==oldpos and oldpos[1]<newpos[1]:
          jumpstate="standing"
        if (X3,Y3) ==oldpos and oldpos[1]>newpos[1]:
            vY =0
    charrect= Rect(X3,Y3,25,33)
    for keyy,rectlist in movingwalls.items():  #if colliding with a moving platform that moves up and down, 
        if (charrect).colliderect(rectlist[0]): #character should be moving with the platform
            Y3-=2

def movegirl3(movingwalls):
    global GX3, GY3, vYg
    global girlstate, jumpstateg
    oldpos=(GX3,GY3)
    keys = key.get_pressed()
    if keys[K_a]:
        GX3-= 4.2
        girlstate= "moveleft"
    elif keys[K_d]:
        GX3+= 4.2
        girlstate= "moveright"
    else:
        girlstate= "standing"
    newpos= (GX3, GY3)
    gpostomove= collide(oldpos, newpos, walls3, buttons3, movingwalls)
    GX3, GY3= gpostomove
    if collide(oldpos, [oldpos[0],oldpos[1]+1], walls3, buttons3, movingwalls) == [oldpos[0],oldpos[1]+1] and jumpstateg!="jump":
        jumpstateg="jump"
        vYg=0
    if keys[K_w] and jumpstateg!="jump":
        jumpstateg = "jump"
        vYg=-5.5
    if jumpstateg =="jump":
        GY3 += vYg
        vYg+=0.2
        newpos= (GX3,GY3)
        (GX3,GY3) = collide(oldpos, newpos, walls3, buttons3, movingwalls)
        if (GX3,GY3)==oldpos and oldpos[1]<newpos[1]:
          jumpstateg="standing"
        if (GX3,GY3) ==oldpos and oldpos[1]>newpos[1]:
            vYg =0
    charrect= Rect(GX3,GY3,25,33)
    for keyy,rectlist in movingwalls.items():  #if colliding with a moving platform that moves up and down, 
        if (charrect).colliderect(rectlist[0]): #character should be moving with the platform
            GY3-=2

def checkcomplete(levelcomplete, rdoor, bdoor, gemlist, X, Y, GX, GY): #checks if level is finished
    if rdoor.collidepoint(X,Y) and bdoor.collidepoint(GX,GY) and len(gemlist)==0: #if colliding with proper door 
        levelcomplete=True                                                        #and all gems are collected
    return levelcomplete

def sprites(X,Y,GX,GY, girlstate, boystate, jumpstate, jumpstateg): #draws all character sprites depending on their state
    global frame, framewait, frameg, framegwait
    if boystate=="moveright":
        if jumpstate=="jump":
            if satchelboy==True: #checks which fireboy sprite to use
                screen.blit(satchelupright, (X, Y))
            else:
                screen.blit(suitupright, (X,Y))
        else:
            if satchelboy==True:
                screen.blit(satchelright[frame], (X,Y))
            else:
                screen.blit(suitright[frame], (X,Y))
            if framewait>=6: #if counter reaches/passes 6, sprite frame changes
                frame+=1 #frame declares with stage of walking spite will be used
                framewait=0 #resets frame counter
                if frame>(len(satchelright)-1): #makes sure frame doesn't surpass the number of images there are
                    frame=0
    if girlstate=="moveright":
        if jumpstateg=="jump":
            if ponchogirl==True:    #checks which watergirl to use
                screen.blit(ponchoupright, (GX, GY-3))
            else:
                screen.blit(dressupright, (GX,GY-3))
        else:
            if ponchogirl==True:
                screen.blit(ponchoright[frameg], (GX,GY))
            else:
                screen.blit(dressright[frameg], (GX,GY))
            if framegwait>=6:
                frameg+=1
                framegwait=0
                if frameg>(len(ponchoright)-1):
                    frameg=0
    if boystate=="moveleft":
        if jumpstate=="jump":
            if satchelboy==True:
                screen.blit(satchelupleft, (X,Y))
            else:
                screen.blit(suitupleft, (X,Y))
        else:
            if satchelboy==True:
                screen.blit(satchelleft[frame], (X,Y))
            else:
                screen.blit(suitleft[frame], (X,Y))
            if framewait>=6:
                frame+=1
                framewait=0
                if frame>=(len(satchelleft)-1):
                    frame=0
    if girlstate=="moveleft":
        if jumpstateg=="jump":
            if ponchogirl==True:
                screen.blit(ponchoupleft, (GX, GY-3))
            else:
                screen.blit(dressupleft, (GX,GY-1))
        else:
            if ponchogirl==True:
                screen.blit(poncholeft[frameg], (GX,GY))
            else:
                screen.blit(dressleft[frameg], (GX,GY))
            if framegwait>=6:
                frameg+=1
                framegwait=0
                if frameg>(len(poncholeft)-1):
                    frameg=0
    if boystate=="standing":
        if jumpstate=="jump":
            if satchelboy==True:
                screen.blit(satchelup, (X,Y))
            else:
                screen.blit(suitup, (X,Y))
        else:
            if satchelboy:
                screen.blit(satchelstand, (X,Y))
            else:
                screen.blit(suitstand, (X,Y))
    if boystate=="dead":
        screen.blit(dyingb, (X,Y))
    if girlstate=="standing":
        if jumpstateg=="jump":
            if ponchogirl:
                screen.blit(ponchoup, (GX,GY))
            else:
                screen.blit(dressup, (GX,GY))
        else:
            if ponchogirl:
                screen.blit(ponchostand, (GX,GY))
            else:
                screen.blit(dressstand,(GX,GY))
    if girlstate=="dead":
        screen.blit(dyingg, (GX,GY))    

def currentscreenfunc(mx,my): 
    global levelonetime, leveltwotime, levelthreetime, currentscreen #draws all screen except for levels
    global ponchogirl, satchelboy
    global levelone, leveltwo, levelthree
    if currentscreen=="titlescreen":
        screen.blit(title,(0,0))
        if startb.collidepoint(mx, my):
            screen.blit(startbutton, (421, 438))
            if mb[0]==1:
                currentscreen="levelscreen"
        if instructionrect.collidepoint(mx,my): 
            screen.blit(instructionb,(0,0))
            if mb[0]==1:
                currentscreen="instructionscreen"
        if characterrect.collidepoint(mx,my):
            screen.blit(charactersb, (0,0))
            if mb[0]==1:
                currentscreen="characterscreen"
#INSTRUCTIONS
    if currentscreen=="instructionscreen": 
        screen.blit(instructions,(0,0))
        if gobackrect.collidepoint(mx,my):
            screen.blit(gobackb, (0,0))
            if mb[0]==1:
                currentscreen="titlescreen"
#CHOOSING CHARACTER
    if currentscreen=="characterscreen":
        screen.blit(characters, (0,0))
        if gobackrect.collidepoint(mx,my):
            screen.blit(gobackb, (0,0))
            if mb[0]==1:
                currentscreen="titlescreen"
        if ponchorect.collidepoint(mx,my) and mb[0]==1:
            ponchogirl=True
        if dressrect.collidepoint(mx,my) and mb[0]==1:
            ponchogirl=False
        if satchelrect.collidepoint(mx,my) and mb[0]==1:
            satchelboy=True
        if suitrect.collidepoint(mx,my) and mb[0]==1:
            satchelboy=False
        if ponchogirl==True:
            screen.blit(ponchoglow, (0,0))
        if ponchogirl==False:
            screen.blit(dressglow,(0,0))
        if satchelboy==True:
            screen.blit(satchelglow,(0,0))
        if satchelboy==False:
            screen.blit(suitglow,(0,0))
    if currentscreen=="levelscreen":
        screen.blit(levelselect, (0,0))

        timetext= font.render("Best Time:", True, (205,190,112))

        #high score
        score1= open("highscore1.txt", "r").read().strip().split("\n") #opens high score txt file and reads all previous times
        score1= str(sorted([int(float(a)) for a in score1])[0]) #this line is not our own. It takes all times and converts them to an integer (cannot change from string with decimals to float)
        score1 = font.render(score1, True, (205,190,112))       #it sorts them from lowest to highest and takes the fastest score
        screen.blit(score1, (385, 248))
        screen.blit(timetext, (385, 213))
        
        score2= open("highscore2.txt", "r").read().strip().split("\n") #repeats high score for level two
        score2= str(sorted([int(float(a)) for a in score2])[0])
        score2 = font.render(score2, True, (205,190,112))
        screen.blit(score2, (255, 457))
        screen.blit(timetext, (255, 424))
        
        score3= open("highscore3.txt", "r").read().strip().split("\n") #repeats high score for level three
        score3= str(sorted([int(float(a)) for a in score3])[0])
        score3 = font.render(score3, True, (205,190,112))
        screen.blit(score3, (520, 457))
        screen.blit(timetext, (520, 424))
            #Choosing level
        if rectone.collidepoint(mx,my):
           screen.blit(one, (0,0))
           if mb[0]==1:
               #highscore:
               levelonetime= t.time()
               levelone=True
        if recttwo.collidepoint(mx,my):
            screen.blit(two, (0,0))
            if mb[0]==1:
                leveltwotime= t.time()
                leveltwo=True
        if rectthree.collidepoint(mx,my):
           screen.blit(three, (0,0))
           if mb[0]==1:
               levelthreetime= t.time()
               levelthree=True
        if gobackrect.collidepoint(mx,my):
            screen.blit(gobackb, (0,0))
            if mb[0]==1:
                currentscreen="titlescreen"

#__________________________________________________________________________________________________

def levelonefunc():
    global levelone, currentscreen, pausescreen, boystate, girlstate, jumpstate, jumpstateg, levelcomplete
    global X,Y,GX,GY
    global gems, gemim, gemcolour
    #DEFAULT:
    defaultgems= [[450,535], [630,535], [163,269], [530,288],
                  [231,43], [47, 105], [417, 80], [507, 80]]
    defaultgemcolour=["red", "blue", "red", "blue", "red", "blue", "red", "blue"]
    boypos= [(X, Y), (X+25, Y), (X, Y+33),(X+25, Y+33)]
    girlpos= [(GX, GY), (GX+25, GY), (GX, GY+33), (GX+25, GY+33)]

    def drawscene1():
        screen.blit(lvl1back,(0,0))
        screen.blit(pauseb, (0,0))
        screen.blit(button, (646, 225))
        screen.blit(button, (538, 328))
        for keyy,rectlist in movingplat.items():
            screen.blit(slide, rectlist[0])     
        #GEMS- had a little help
        gemboxes= []
        index=[]                 
        for n in range (len(gems)):
            gemboxes.append(screen.blit(gemim[gemcolour[n]], gems[n]))
        for n in range (len(gemboxes)):
            if gemcolour[n]=="red":
                for i in range(len(boypos)):
                    if gemboxes[n].collidepoint(boypos[i]): #if boy collides with red gem, append gem position to list
                        index.append(n)
                        #ping.play()
            if gemcolour[n]=="blue":
                for i in range(len(girlpos)):
                    if gemboxes[n].collidepoint(girlpos[i]): #if girl collides with blue gem, append gem position to list
                        index.append(n)
                        #ping.play()
        for i in range(len(index)): #remove gems at listed positions 
            del gems[index[i]]
            del gemcolour[index[i]]
        sprites(X,Y,GX,GY, girlstate, boystate, jumpstate, jumpstateg)
        if pauserect.collidepoint(mx,my):
            screen.blit(pauseb2, (0,0))
        if pausescreen:
            screen.blit(pause, (200,100))
            if resumerect.collidepoint(mx,my):
                screen.blit(resume, (351, 203))
            if retryrect2.collidepoint(mx,my):
                screen.blit(retrymenu, (291,258))
            if backrect2.collidepoint(mx,my):
                screen.blit(backmenu, (333, 321))
        if boystate=="dead" or girlstate=="dead":
            screen.blit(gameoverim, (200, 100))
            if retryrect.collidepoint(mx,my):
                screen.blit(retrymenu, (289, 254))
            if backrect.collidepoint(mx,my):
                screen.blit(backmenu, (335, 324))
        if checkcomplete(levelcomplete, firedoor, waterdoor, gems, X, Y, GX, GY)==True:
            continuerect= Rect(379, 402, 150, 22)
            screen.blit(lvlcomp, (308, 156))
            if continuerect.collidepoint(mx,my):
                screen.blit(continuepic, (379, 402))

    if checkcomplete(levelcomplete, firedoor, waterdoor, gems, X, Y, GX, GY) == False: #only move things is level is not complete
        if girlstate!= "dead" and boystate!="dead" and pausescreen==False: #continue moving sprites and platforms if they're not dead and game is not on pause
            for keyy in movingplat:
                movingplat[keyy][-1]=False #reset button back to false and button can go back to true was collide function is called
            movegirl(movingplat)
            moveboy(movingplat)
            movingplatform(movingplat, maxmin, direction)
    checkboydead(X,Y,reddead)
    checkgirldead(GX,GY,bluedead)
#PAUSE
    if pauserect.collidepoint(mx,my) and mb[0]==1:
        pausescreen=True
    if pausescreen:
        if resumerect.collidepoint(mx,my) and mb[0]==1:
            pausescreen=False        
        if retryrect2.collidepoint(mx,my) and mb[0]==1:#reset everythiing back to default
            pausescreen=False
            boystate="standing"
            girlstate="standing"
            X,Y= 40, 537
            GX,GY= 40, 460
            gems= defaultgems
            gemcolour=defaultgemcolour
        if backrect2.collidepoint(mx,my) and mb[0]==1:#reset everythiing back to default
            pausescreen=False
            boystate="standing"
            girlstate="standing"
            X,Y= 40, 537
            GX,GY= 40, 460
            gems= defaultgems
            gemcolour=defaultgemcolour
            pausescreen=False
            currentscreen="levelscreen"
            levelone=False              
    #DYING        
    if boystate=="dead" or girlstate=="dead":
        if retryrect.collidepoint(mx,my):
            if mb[0]==1:
                #reset all gems and states to default
                boystate="standing"
                girlstate="standing"
                X,Y= 40, 537
                GX,GY= 40, 460
                gems= defaultgems
                gemcolour=defaultgemcolour
        if backrect.collidepoint(mx,my):
            if mb[0]==1:#reset everythiing back to default
                X,Y= 40, 537
                GX,GY= 40, 460
                gems= gems= defaultgems
                gemcolour=defaultgemcolour
                currentscreen="levelscreen"
                levelone=False
                boystate="standing"
                girlstate="standing"

    if checkcomplete(levelcomplete, firedoor, waterdoor, gems, X, Y, GX, GY)==True:
        continuerect= Rect(379, 402, 150, 22)
        if continuerect.collidepoint(mx,my):
            if mb[0]==1:
                #HIGHSCORE
                highscore1= open("highscore1.txt", "a+")
                highscore1.write(str(t.time()-levelonetime)+"\n")#adds new time to textfile
                highscore1.close()
                #reset everythiing back to default
                X,Y= 40, 537
                GX,GY= 40, 460
                gems= defaultgems
                gemcolour=defaultgemcolour
                levelcomplete= False
                levelone=False
                currentscreen="levelscreen"
    drawscene1()
#_______________________________________________________________________________________________

def leveltwofunc():
    global leveltwo,  pausescreen, currentscreen, boystate, girlstate, jumpstate, jumpstateg, levelcomplete
    global X2,Y2,GX2,GY2
    global gems2, gemim2, gemcolour2
    boypos= [(X2, Y2), (X2+25, Y2), (X2, Y2+33),(X2+25, Y2+33)]
    girlpos= [(GX2, GY2), (GX2+25, GY2), (GX2, GY2+33), (GX2+25, GY2+33)]
    defaultgems= [[182,545], [250,545], [182,480], [250,480],
            [555,545], [618,545], [555,480], [618,480],
            [645,388], [530,388], [343,388], [230,388],
            [284,150], [413,265], [462,265], [586,150],
            [380,59], [337,59]]
    defaultgemcolour=["red", "red", "blue", "blue",
                      "blue", "blue", "red", "red",
                      "red", "blue", "red", "blue",
                      "red", "red", "blue", "blue",
                      "blue", "red"]

    def drawscreen2():  
        screen.blit(lvl2back,(0,0))
        screen.blit(pauseb, (0,0))
        for keyy,rectlist in movingplat2.items():
            if keyy=="1":
                screen.blit(slide21, (rectlist[0]))
            if keyy=="2" or keyy=="3" or keyy=="4":
                screen.blit(slide22, (rectlist[0]))
        #GEMS
        gemboxes2= []
        index2=[]                 
        for n in range (len(gems2)):
            gemboxes2.append(screen.blit(gemim2[gemcolour2[n]], gems2[n]))
        for n in range (len(gemboxes2)):
            if gemcolour2[n]=="red":
                for i in range(len(boypos)):
                    if gemboxes2[n].collidepoint(boypos[i]):
                        index2.append(n)
            if gemcolour2[n]=="blue":
                for i in range(len(girlpos)):
                    if gemboxes2[n].collidepoint(girlpos[i]):
                        index2.append(n)
        for i in range(len(index2)):
            del gems2[index2[i]]
            del gemcolour2[index2[i]]
        sprites(X2,Y2,GX2,GY2, girlstate, boystate, jumpstate, jumpstateg)
        if pauserect.collidepoint(mx,my):
            screen.blit(pauseb2, (0,0))
        if pausescreen:
            screen.blit(pause, (200,100))
            if resumerect.collidepoint(mx,my):
                screen.blit(resume, (351, 203))
            if retryrect2.collidepoint(mx,my):
                screen.blit(retrymenu, (291,258))
            if backrect2.collidepoint(mx,my):
                screen.blit(backmenu, (333, 321))
        if boystate=="dead" or girlstate=="dead":
            screen.blit(gameoverim, (200, 100))
            if retryrect.collidepoint(mx,my):
                screen.blit(retrymenu, (289, 254))
            if backrect.collidepoint(mx,my):
                screen.blit(backmenu, (335, 324))
        if checkcomplete(levelcomplete, firedoor2, waterdoor2, gems2, X2, Y2, GX2, GY2)==True:
            continuerect= Rect(379, 402, 150, 22)
            screen.blit(lvlcomp, (308, 156))
            if continuerect.collidepoint(mx,my):
                screen.blit(continuepic, (379, 402))

    if checkcomplete(levelcomplete, firedoor2, waterdoor2, gems2, X2, Y2, GX2, GY2) == False:
        if girlstate!= "dead" and boystate!="dead" and pausescreen==False:
            for keyy in movingplat2:
                movingplat2[keyy][-1]=False
            movegirl2(movingplat2)
            moveboy2(movingplat2)
            movingplatform(movingplat2, maxmin2, direction2) 
    checkboydead(X2,Y2,reddead2)
    checkgirldead(GX2,GY2,bluedead2) 

    if pauserect.collidepoint(mx,my) and mb[0]==1:
        pausescreen=True
    if pausescreen:
        screen.blit(pause, (200,100))
        if resumerect.collidepoint(mx,my) and mb[0]==1:
            pausescreen=False        
        if retryrect2.collidepoint(mx,my) and mb[0]==1:
            boystate="standing"
            girlstate="standing"
            X2,Y2= 60, 537
            GX2,GY2= 35, 537
            gems2= defaultgems
            gemcolour2=defaultgemcolour
            pausescreen=False
        if backrect2.collidepoint(mx,my) and mb[0]==1:
            boystate="standing"
            girlstate="standing"
            X2,Y2= 60, 537
            GX2,GY2= 35, 537
            gems2= defaultgems
            gemcolour2=defaultgemcolour
            pausescreen=False
            currentscreen="levelscreen"
            leveltwo=False
    #DYING        
    if boystate=="dead" or girlstate=="dead":
        if retryrect.collidepoint(mx,my) and mb[0]==1:
            boystate="standing"
            girlstate="standing"
            X2,Y2= 60, 537
            GX2,GY2= 35, 537
            gems2= defaultgems
            gemcolour2=defaultgemcolour
        if backrect.collidepoint(mx,my) and mb[0]==1:
            boystate="standing"
            girlstate="standing"
            X2,Y2= 60, 537
            GX2,GY2= 35, 537
            gems2= defaultgems
            gemcolour2=defaultgemcolour
            currentscreen="levelscreen"
            leveltwo=False

    if checkcomplete(levelcomplete, firedoor2, waterdoor2, gems2, X2, Y2, GX2, GY2)==True:
        continuerect= Rect(379, 402, 150, 22)
        if continuerect.collidepoint(mx,my) and mb[0]==1:
            highscore2= open("highscore2.txt", "a+")
            highscore2.write(str(t.time()-leveltwotime)+"\n")
            highscore2.close()
            X2,Y2= 60, 537
            GX2,GY2= 35, 537
            gems2= defaultgems
            gemcolour2=defaultgemcolour
            levelcomplete= False
            currentscreen="levelscreen"
            leveltwo=False
    drawscreen2()

#________________________________________________________________________________________________

def levelthreefunc():
    global levelthree, currentscreen, pausescreen, boystate, girlstate, jumpstate, jumpstateg, levelcomplete
    global X3,Y3,GX3,GY3
    global gems3, gemim3, gemcolour3
    defaultgems= [[642, 162], [642, 265], [45, 395], [45, 285], [45, 45],
                  [828, 305], [560, 450], [515, 450], [122,140],
                  [345, 305], [440, 405], [363, 485],
                  [820, 130]]
    defaultgemcolour=["blue", "blue", "red", "red", "red",
                     "blue", "blue", "red", "red",
                     "red", "blue", "red",
                     "red"]
    boypos= [(X3, Y3), (X3+25, Y3), (X3, Y3+33),(X3+25, Y3+33)]
    girlpos= [(GX3, GY3), (GX3+25, GY3), (GX3, GY3+33), (GX3+25, GY3+33)]

    def drawscreen3():
        screen.blit(lvl3back,(0,0))
        screen.blit(pauseb, (0,0))
        for keyy,rectlist in movingplat3.items():
            if keyy=="1":
                screen.blit(slide31, rectlist[0])
            elif keyy=="2":
                screen.blit(slide32, rectlist[0])
        #GEMS
        gemboxes3= []
        index3=[]                 
        for n in range (len(gems3)):
            gemboxes3.append(screen.blit(gemim3[gemcolour3[n]], gems3[n]))
        for n in range (len(gemboxes3)):
            if gemcolour3[n]=="red":
                for i in range(len(boypos)):
                    if gemboxes3[n].collidepoint(boypos[i]):
                        index3.append(n)
            if gemcolour3[n]=="blue":
                for i in range(len(girlpos)):
                    if gemboxes3[n].collidepoint(girlpos[i]):
                        index3.append(n)
        for i in range(len(index3)):
            del gems3[index3[i]]
            del gemcolour3[index3[i]]
        sprites(X3,Y3,GX3,GY3, girlstate, boystate, jumpstate, jumpstateg)
        if pauserect.collidepoint(mx,my):
            screen.blit(pauseb2, (0,0))
        if pausescreen:
            screen.blit(pause, (200,100))
            if resumerect.collidepoint(mx,my):
                screen.blit(resume, (351, 203))       
            if retryrect2.collidepoint(mx,my):
                screen.blit(retrymenu, (291,258))
            if backrect2.collidepoint(mx,my):
                screen.blit(backmenu, (333, 321))
        if checkcomplete(levelcomplete, firedoor3, waterdoor3, gems3, X3, Y3, GX3, GY3)==True:
            continuerect= Rect(379, 402, 150, 22)
            screen.blit(lvlcomp, (308, 156))
            if continuerect.collidepoint(mx,my):
                screen.blit(continuepic, (379, 402))
        if boystate=="dead" or girlstate=="dead":
            screen.blit(gameoverim, (200, 100))
            if retryrect.collidepoint(mx,my):
                screen.blit(retrymenu, (289, 254))
            if backrect.collidepoint(mx,my):
                screen.blit(backmenu, (335, 324))

    if checkcomplete(levelcomplete, firedoor3, waterdoor3, gems3, X3, Y3, GX3, GY3) == False:
        if girlstate!= "dead" and boystate!="dead" and pausescreen==False:
            for keyy in movingplat3:
                movingplat3[keyy][-1]=False
            movegirl3(movingplat3)
            moveboy3(movingplat3)
            movingplatform(movingplat3, maxmin3, direction3)
    checkboydead(X3,Y3,reddead3)
    checkgirldead(GX3,GY3,bluedead3)

    if pauserect.collidepoint(mx,my) and mb[0]==1:
        pausescreen=True
    if pausescreen:
        if resumerect.collidepoint(mx,my) and mb[0]==1:
            pausescreen=False        
        if retryrect2.collidepoint(mx,my) and mb[0]==1:
            boystate="standing"
            girlstate="standing"
            X3,Y3= 110, 530
            GX3,GY3= 820, 70
            gems3= defaultgems
            gemcolour3=defaultgemcolour
            pausescreen=False
        if backrect2.collidepoint(mx,my):
            screen.blit(backmenu, (333, 321))
            if mb[0]==1:
                boystate="standing"
                girlstate="standing"
                X3,Y3= 110, 530
                GX3,GY3= 820, 70
                gems3= defaultgems
                gemcolour3=defaultgemcolour
                pausescreen=False
                currentscreen="levelscreen"
                levelthree=False            
    #DYING        
    if boystate=="dead" or girlstate=="dead":
        if retryrect.collidepoint(mx,my):
            if mb[0]==1:
                boystate="standing"
                girlstate="standing"
                X3,Y3= 110, 530
                GX3,GY3= 820, 70
                gems3= defaultgems
                gemcolour3=defaultgemcolour
        if backrect.collidepoint(mx,my) and mb[0]==1:
            boystate="standing"
            girlstate="standing"
            X3,Y3= 110, 530
            GX3,GY3= 820, 70
            gems3= defaultgems
            gemcolour3=defaultgemcolour
            currentscreen="levelscreen"
            levelthree=False
                
    if checkcomplete(levelcomplete, firedoor3, waterdoor3, gems3, X3, Y3, GX3, GY3)==True:
        continuerect= Rect(379, 402, 150, 22)
        if continuerect.collidepoint(mx,my) and mb[0]==1:
            highscore3= open("highscore3.txt", "a+")
            highscore3.write(str(t.time()-levelthreetime)+"\n")
            highscore3.close()
            X3,Y3= 110, 530
            GX3,GY3= 820, 70
            gems3= defaultgems
            gemcolour3=defaultgemcolour
            levelcomplete= False
            currentscreen="levelscreen"
            levelthree=False
    drawscreen3()
#________________________________________________________________________________________________
#RUNNING        
running=True
mx,my=0,0
mb=(0,0,0)
import time as t
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False      
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    
    currentscreenfunc(mx,my)

    if levelone:
        levelonefunc()              
    if leveltwo:
        leveltwofunc()   
    if levelthree:
        levelthreefunc()
    myClock.tick(60)
    framewait+=1
    framegwait+=1
    display.flip()
quit()
