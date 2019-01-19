from pygame import *
from random import *
width=840
height=950


screen=display.set_mode((width,height))
timer=time.Clock()

red=255,0,0
grn=0,255,0
blu=0,0,255          #Basic Setup
ylw=255,255,0
wht=255,255,255
blk=0,0,0
gry=120,120,120

space=image.load("pics/spaaaace.jpg")
bg=transform.scale(space,(840,950))
yak=image.load("pics/yak.png")
topYak=transform.scale(yak,(400,260))    #Images
gay=image.load("pics/for pay.png")
rainbow=transform.scale(gay,(670,350))

safeZone=[0,350,840,100]


def rectCreate(positions, rows):
    blockW = width//rows
    blockH = height//(rows+1)  #creating a list for all of the falling rectangles

    rects = [Rect(blockW*(positions[i]), -blockH*i, blockW, blockH) for i in range(100)]
    return rects

def rectChange(rects, pixel):
    return [Rect(i[0], i[1]+pixel, i[2], i[3]) for i in rects]

def rectDraw(rects, thickness = 0, color = (255, 255, 255)):
    for i in rects:
        draw.rect(screen, color, i, thickness) #actually drawing the rectangles

def rectCreateReverse(positions, rows):
    blockW = width//rows
    blockH = height//(rows+1) 

    rects = [Rect(blockW*(positions[i]), blockH*i+height, blockW, blockH) for i in range(len(positions))]
    return rects

def rectChangeReverse(rects, pixel):
    return [Rect(i[0], i[1]-pixel, i[2], i[3]) for i in rects] #same as earlier, but going upwards instead

def fadeDraw(alpha):
    surf = Surface((width, height), SRCALPHA)
    draw.rect(surf, ((0,0,0, alpha)), (0,0,width,height))  #gradually making the screen darker
    return surf

def runLose():
    running = True
    mainMenuRect = Rect(240, 470, 360, 220) 
    
    while running:
        for e in event.get():
            if e.type==QUIT:
                running=False
    
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        screen.fill(0)
        rectDraw([mainMenuRect], 5)         #losing screen
        
        init()
        scoreFont1=font.SysFont("Impact",55)
        scoreFont2=font.SysFont("Impact",90)
        yourScore1=scoreFont1.render("You got a score of:",True,wht)
        yourScore2=scoreFont2.render(str(score),True,wht)
        screen.blit(yourScore1,(220,120))
        screen.blit(yourScore2,(395,220))

        backToMenu1=scoreFont1.render("Back To",True,wht)
        backToMenu2=scoreFont1.render("Main Menu",True,wht)
        screen.blit(backToMenu1,(280,510))
        screen.blit(backToMenu2,(280,580))
        
        if mainMenuRect.collidepoint(mx,my):
            
            rectDraw([mainMenuRect], 0, ylw)
            backToMenu3=scoreFont1.render("Back To",True,blk)
            backToMenu4=scoreFont1.render("Main Menu",True,blk)
            screen.blit(backToMenu3,(280,510))
            screen.blit(backToMenu4,(280,580))
            
            if mb[0] == 1:
                
                return "menu"
            
    
        display.flip()
    quit() 
    
def checkLose(rects, screenRect):
    return (False if screenRect.contains(rects[0]) else True)  #conditions for losing

def checkLoseReverse(rects, screenRect):
    #print(rects[0][1], rects[0][1]<0)
    return ((rects[0][1])<0)

def scoreBlit(txt):
    init()
    titleFont = font.SysFont("Impact", 30)
    #titleFont.set_bold(True)
    subtitleText = titleFont.render(txt,True,red)
    screen.blit(subtitleText,(420-subtitleText.get_width()//2,100))  #shows your current score on-screen
    
def runMenu():
    global width, height
    gameOptionsRect = Rect(270, 570, 300, 160)  #main menu/intro screen
    running = True
    ayy = 0
    lmao = 1
    while running:
        for e in event.get():
            if e.type==QUIT:
                running=False
            if e.type==MOUSEBUTTONUP and gameOptionsRect.collidepoint(mx, my):
                ayy=1
    
        mb=mouse.get_pressed()
        mx,my=mouse.get_pos()
        screen.blit(bg,(0,0))
        screen.blit(rainbow,(95,50))
        screen.blit(topYak,(240,200))
        
        rectDraw([gameOptionsRect],5)
        
        init()
        startFont=font.SysFont("Impact",90)
        #startFont.set_bold(True)
        playButton1=startFont.render("PLAY",True,wht)
        playButton2=startFont.render("PLAY",True,blk)
        screen.blit(playButton1,(335,595))
        
        yakFont1=font.SysFont("Impact",48)
        yak1=yakFont1.render("PIANO TILES",True,wht)
        yakFont2=font.SysFont("Edwardian Script ITC",38)
        yak2=yakFont2.render("Yak Edition",True,wht)
        screen.blit(yak1,(300,270))
        screen.blit(yak2,(340,322))
        
        
        if gameOptionsRect.collidepoint(mx, my):
            rectDraw([gameOptionsRect], 0, ylw)
            screen.blit(playButton2,(335,595))
            if ayy==lmao:
                time.wait(10)
                
                return "gameOptions"
                
            
            
    
        display.flip()
    quit()



def runGameOptions():
    classicRect = Rect(200, 100, 440, 100)
    amazingRect = Rect(200, 260, 440, 100)
    reverseRect = Rect(200, 420, 440, 100)  #game mode selections
    fadeRect = Rect(200, 580, 440, 100)
    sandyRect = Rect(200, 740, 440, 100)


    optionRects = [classicRect, amazingRect, reverseRect, fadeRect, sandyRect]
    screen.fill(0)
    running = True
    while running:
        mouseHold = False
        for e in event.get():
            if e.type==QUIT:
                running=False
            if e.type==MOUSEBUTTONUP:
                mouseHold= False
            if e.type == MOUSEBUTTONDOWN:
                mouseHold = True
    
        mb=mouse.get_pressed()
        mx,my=mouse.get_pos()
        

        rectDraw(optionRects, 1)
        init()
        genericFont=font.SysFont("Impact",48)
        classicTxt=genericFont.render("Classic Mode",True,wht)
        amazingTxt=genericFont.render("Amazing Mode",True,wht)
        reverseTxt=genericFont.render("Reverse Mode",True,wht)
        fadeTxt=genericFont.render("Fade Mode",True,wht)
        darudeTxt=genericFont.render("Sandstorm Mode",True,wht)
        screen.blit(classicTxt,(290,115))
        screen.blit(amazingTxt,(285,280))
        screen.blit(reverseTxt,(290,(280+165)-6))
        screen.blit(fadeTxt,(320,(280+165*2)-12))
        screen.blit(darudeTxt,(265,(280+165*3)-16))

        if classicRect.collidepoint(mx,my):
            if mouseHold:
                rectDraw([classicRect], 0, ylw)
                time.wait(10)
                return "classic"
            
        elif amazingRect.collidepoint(mx,my):
            if mouseHold:
                time.wait(10)
                
                return "amazing"
        elif reverseRect.collidepoint(mx,my):
            if mouseHold:
                time.wait(10)
                return "reverse"

        elif fadeRect.collidepoint(mx,my):
            if mouseHold:
                time.wait(10)
                return "fade"
            
        elif sandyRect.collidepoint(mx,my):
            if mouseHold:
                time.wait(10)
                return "sandy"
        
    
        display.flip()
    quit() 



def runClassic():
    screenRect = Rect(0,0,width,height)
    columns = 4
    positions=[randint(0, columns-1) for i in range(2000)]
    
    rects = rectCreate(positions, columns)

    letters = ["a", "s", "d", "f", "g", "h", "k", "l"]
    letterNums = [ord(letters[i]) for i in range(columns)]
    buttons = [i for i in range(columns)]

    keys = key.get_pressed()
    running = True
    lose = False
    pixel=5
    while running:
        keyHold = False
        for e in event.get():
            time.delay(10)
            if e.type==QUIT:
                running=False
            if KEYDOWN and not keyHold:
                time.delay(20)
                keys = key.get_pressed()
                for i, j in zip(buttons, letterNums):
                    if keys[j]:
                        if positions[0] == i:
                            del positions[0]
                            del rects[0]
                            time.delay(10)
                        else:
                            lose = True
                keyHold = True
            if KEYUP:
                keyHold = False


                    
    
        mb=mouse.get_pressed()
        mx,my=mouse.get_pos()
        screen.fill(0)
        #screen.blit(bg,(0,0))
        draw.rect(screen,gry,safeZone)
        
        
        
        
            

        #keys = key.get_pressed()
        #print(keys)
        

        rects = rectChange(rects, int(pixel))
        rectDraw(rects)
        if lose:
            return "lose"
            
        lose = checkLose(rects, screenRect)
        
        global score
        score = 2000-len(positions)
        scoreBlit(str(score))

        pixel+=0.02
        

        time.wait(1)
    
        timer.tick(60)
        display.flip()


def runReverse():
    screenRect = Rect(0, 0, width, height)
    columns = 4
    positions=[randint(0, columns-1) for i in range(2000)]
    rects = rectCreateReverse(positions, columns)

    letters = ["a", "s", "d", "f", "g", "h", "k", "l"]
    letterNums = [ord(letters[i]) for i in range(columns)]
    buttons = [i for i in range(columns)]

    keys = key.get_pressed()
    running = True
    lose = False
    pixel = 5
    while running:
        keyHold = False
        for e in event.get():
            time.delay(10)
            if e.type==QUIT:
                running=False
            if KEYDOWN and not keyHold:
                time.delay(20)
                keys = key.get_pressed()
                for i, j in zip(buttons, letterNums):
                    if keys[j]:
                        if positions[0] == i:
                            del positions[0]
                            del rects[0]
                            time.delay(10)
                        else:
                            lose = True
                keyHold = True
            if KEYUP:
                keyHold = False

        mb=mouse.get_pressed()
        mx,my=mouse.get_pos()

        


            

        #keys = key.get_pressed()
        #print(keys)
        screen.fill(0)
        draw.rect(screen,gry,safeZone)

        rects = rectChangeReverse(rects, int(pixel))
        rectDraw(rects)

        if lose:
            return "lose"
            
        lose = checkLoseReverse(rects, screenRect)
        
        global score
        score = 2000-len(positions)
        scoreBlit(str(score))

        pixel+=0.02

        time.delay(10)
    
        timer.tick(60)
        display.flip()
    quit() 

def runAmazingChoose():
    rects = [Rect((100*i)-20, 480, 80, 200) for i in range(1, 8)]
    running = True
    time.wait(10)
    while running:
        mouseHold = False
        for e in event.get():
            if e.type==QUIT:
                running=False
            if e.type==MOUSEBUTTONUP:
                mouseHold= False
            if e.type == MOUSEBUTTONDOWN:
                mouseHold = True
    
        mb=mouse.get_pressed()
        mx,my=mouse.get_pos()

        screen.fill(0)

        rectDraw(rects, 1)

        init()
        iFont=font.SysFont("Impact",45)
        instructions=iFont.render("Pick the number of keys",True,wht)
        screen.blit(instructions,(195,200))
        uno=iFont.render("1",True,wht)
        dos=iFont.render("2",True,wht)
        tres=iFont.render("3",True,wht)
        cuatro=iFont.render("4",True,wht)
        cinco=iFont.render("5",True,wht)
        seis=iFont.render("6",True,wht)
        siete=iFont.render("7",True,wht)

        screen.blit(uno,(100*1,500))
        screen.blit(dos,(100*2,500))
        screen.blit(tres,(100*3,500))
        screen.blit(cuatro,(100*4,500))
        screen.blit(cinco,(100*5,500))
        screen.blit(seis,(100*6,500))
        screen.blit(siete,(100*7,500))

        for i in rects:
            if i.collidepoint(mx,my):
                rectDraw([i], 1, (255,255,0))
                if mb[0] == 1:
                    return rects.index(i) + 2
        
    
        display.flip()
    quit()

def runAmazing():
    screenRect = Rect(0,0,width,height)


    columns = runAmazingChoose()
    positions=[randint(0, columns-1) for i in range(2000)]
    rects = rectCreate(positions, columns)

    letters = ["a", "s", "d", "f", "g", "h", "k", "l"]
    letterNums = [ord(letters[i]) for i in range(columns)]
    buttons = [i for i in range(columns)]

    keys = key.get_pressed()
    running = True
    lose = False
    pixel = 5
    while running:
        keyHold = False
        for e in event.get():
            time.delay(10)
            if e.type==QUIT:
                running=False
            if KEYDOWN and not keyHold:
                time.delay(20)
                keys = key.get_pressed()
                for i, j in zip(buttons, letterNums):
                    if keys[j]:
                        if positions[0] == i:
                            del positions[0]
                            del rects[0]
                            time.delay(10)
                        else:
                            lose = True
                keyHold = True
            if KEYUP:
                keyHold = False

                   
    
        mb=mouse.get_pressed()
        mx,my=mouse.get_pos()
        screen.fill(0)
        draw.rect(screen,gry,safeZone)
        


        rects = rectChange(rects, int(pixel))
        rectDraw(rects)

        if lose:
            return "lose"
            
        lose = checkLose(rects, screenRect)

        global score
        score = 2000-len(positions)
        scoreBlit(str(score))

        pixel+=0.02

        time.wait(1)
    
        timer.tick(60)
        display.flip()
        
def runFade():
    screenRect = Rect(0, 0, width, height)
    columns = 4
    positions=[randint(0, columns-1) for i in range(2000)]
    rects = rectCreate(positions, columns)

    letters = ["a", "s", "d", "f", "g", "h", "k", "l"]
    letterNums = [ord(letters[i]) for i in range(columns)]
    buttons = [i for i in range(columns)]

    keys = key.get_pressed()
    running = True
    lose = False
    alpha = 0
    reset = False
    pixel = 5
    while running:
        keyHold = False
        for e in event.get():
            time.delay(10)
            if e.type==QUIT:
                running=False
            if KEYDOWN and not keyHold:
                time.delay(20)
                keys = key.get_pressed()
                for i, j in zip(buttons, letterNums):
                    if keys[j]:
                        if positions[0] == i:
                            del positions[0]
                            del rects[0]
                            time.delay(10)
                        else:
                            lose = True
                keyHold = True
            if KEYUP:
                keyHold = False

    
        mb=mouse.get_pressed()
        mx,my=mouse.get_pos()

        

        if lose:
            return "lose"
        lose = checkLose(rects, screenRect)
            

        #keys = key.get_pressed()
        #print(keys)
        screen.fill(0)
        draw.rect(screen,gry,safeZone)

        rects = rectChange(rects, int(pixel))
        rectDraw(rects)

        screen.blit(fadeDraw(alpha), (0,0))
        if not reset:
            alpha+=2
        if reset:
            alpha-=2
        if alpha==0:
            reset = False
        if alpha==254:
            reset = True

        global score
        score = 2000-len(positions)
        scoreBlit(str(score))

        pixel+=0.02
        


        

        time.delay(10)
    
        timer.tick(60)
        display.flip()

def runSandy():
    sandy = transform.smoothscale(image.load("pics/YakTiles.jpg").convert(32,SRCALPHA), (width, int(height*1.5//7)))
    screenRect = Rect(0,0,width,height)
    columns = 4
    positions=[randint(0, columns-1) for i in range(2000)]
    rects = rectCreate(positions, columns)

    letters = ["a", "s", "d", "f", "g", "h", "k", "l"]
    letterNums = [ord(letters[i]) for i in range(columns)]
    buttons = [i for i in range(columns)]

    keys = key.get_pressed()
    running = True
    lose = False
    y=-int(height*2//7)
    pixel = 5
    while running:
        keyHold = False
        for e in event.get():
            time.delay(10)
            if e.type==QUIT:
                running=False
            if KEYDOWN and not keyHold:
                time.delay(20)
                keys = key.get_pressed()
                for i, j in zip(buttons, letterNums):
                    if keys[j]:
                        if positions[0] == i:
                            del positions[0]
                            del rects[0]
                            time.delay(10)
                        else:
                            lose = True
                keyHold = True
            if KEYUP:
                keyHold = False


                    
    
        mb=mouse.get_pressed()
        mx,my=mouse.get_pos()
        screen.fill(0)
        draw.rect(screen,gry,safeZone)

        rects = rectChange(rects, 5)
        rectDraw(rects)
        
        if lose:
            return "lose"
            
        lose = checkLose(rects, screenRect)
        screen.blit(sandy, (0,y))
        y+=1
        
        if y==height+int(height*2/7):
            y = -int(height*2/7)

        global score
        score = 2000-len(positions)
        scoreBlit(str(score))

        pixel +=0.02
        

        time.wait(1)
    
        timer.tick(60)
        display.flip()


page = "menu"
while page != "exit":
    if page == "menu":
        page = runMenu()
    if page == "gameOptions":
        page = runGameOptions()
    if page == "classic":
        page = runClassic()
    if page == "amazing":
        page = runAmazing()
    if page == "reverse":
        page = runReverse()
    if page == "fade":
        page = runFade()
    if page == "sandy":
        page = runSandy()
    if page == "lose":
        page = runLose()
 
    
