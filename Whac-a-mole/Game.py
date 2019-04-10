import pygame
import os
import random
import Mole
import Cursor
import Button
import InputBox

#initialize pygame
pygame.init()
#initialize randomizing
random.seed()
#SETTINGS
holes = [(140,150),(410,150),(680,150),(140,277),(410,277),(680,277),(140,394),(410,394),(680,394)]

#Sprite directories
background =  pygame.image.load(os.path.join("data","background.png"))
mole = Mole.Mole(os.path.join("data","mole.png"))
moleHit = Mole.Mole(os.path.join("data","mole_hit.png"))
cursors = pygame.sprite.Group()
hammer = Cursor.Cursor(os.path.join("data", "hammer.png"))
hammer_hit = Cursor.Cursor(os.path.join("data", "hammer_hit.png"))
menuCursor = Cursor.Cursor(os.path.join("data", "cursor.png"))
cursors.add(hammer,hammer_hit,menuCursor)
startButton = Button.Button(os.path.join("data","start.png"))
quitButton = Button.Button(os.path.join("data","quit.png"))
highscoresButton = Button.Button(os.path.join("data","highscores_box.png"))
livesButton = Button.Button(os.path.join("data","lives_box.png"))
ScoreBoxButton = Button.Button(os.path.join("data","your_score_box.png"))
#Background
gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.blit(background,(0,0))
#Booleans
moleDrawn = False
isGame = True
isStart = False
isMoleHitted = False
isHammerPressed = False
timeForBreak= False
isMenu = True
isMusicPlaying = False
#Event Times
maxMoleTime = 2000
breakTime = 200
#Events
moleDisappearEvent = pygame.USEREVENT+1
hammerPressed = pygame.USEREVENT+2
timeForBreakEvent = pygame.USEREVENT+3

#Player values
score = 0
lifes = 3
level = 1
name = ""
highscores =[]
#Loadig Highscores from file
with open(os.path.join("data","highscore.txt")) as file:
    for i in file.readlines():
        tmp = i.split(",")
        try:
            highscores.append((str(tmp[0]), str(tmp[1]).rstrip()))
        except: pass

#System setup
font = pygame.font.SysFont(None, 40)
pygame.mouse.set_visible(False)
mousePosition = (400,300)
ScoreBoxButton.update((180,50))
livesButton.update((680,50))
pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)
pygame.mixer.set_num_channels(2)


#END OF SETTINGS

#Rendering messages on screen
def screenMessage(msg, color,mWidtg, mHeight):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [mWidtg, mHeight])

#Game Loop
while isGame:
    #Background Music setup
    if  not isMusicPlaying:
        pygame.mixer.music.load(os.path.join("data", "bg_music.mp3"))
        pygame.mixer.music.play(-1)
        isMusicPlaying == True

    #Menu Loop
    while isMenu:
        #Player Reset
        score = 0
        lifes = 3
        level = 1
        name = ""
        timeForBreak = False

        gameDisplay.blit(background, (0, 0))
        highscoresButton.update((400,210))
        highscoresButton.draw(gameDisplay)
        screenMessage("Top 5 scores :",(255,255,255),310,100)
        for i in range(len(highscores)):
            screenMessage("{} {}".format(highscores[i][0],highscores[i][1]),(255,255,255),270,140+40*i)


        startButton.update((650,540))
        startButton.draw(gameDisplay)
        quitButton.update((150,540))
        quitButton.draw(gameDisplay)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mousePosition = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                isMenu = False
                isGame = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.sprite.spritecollide(startButton,cursors,False):
                    isMenu = False
                    isStart= True
                elif pygame.sprite.spritecollide(quitButton,cursors,False):
                    isMenu = False
                    isGame = False
        menuCursor.update(mousePosition)
        menuCursor.draw(gameDisplay)
        pygame.display.update()

    while isStart:
        #Event Handle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isGame = False
                isStart = False
            if event.type == pygame.MOUSEMOTION:
                mousePosition = pygame.mouse.get_pos()
            if event.type == moleDisappearEvent:
                    if not isMoleHitted:
                        gameDisplay.blit(background, (0, 0))
                        lifes -= 1
                    else:
                        isMoleHitted = False
                    moleDrawn= False
                    timeForBreak = True
                    pygame.time.set_timer(timeForBreakEvent, breakTime)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.sprite.spritecollide(mole,cursors,False) and not isMoleHitted:
                    moleHit.update(holes[holeNumber])
                    score += 10
                    pygame.time.set_timer(moleDisappearEvent, maxMoleTime)
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound(os.path.join("data","hit.wav")))
                    isMoleHitted = True
                else:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound(os.path.join("data", "miss.wav")))
                isHammerPressed= True
                pygame.time.set_timer(hammerPressed, 200)

            if event.type == hammerPressed:
                isHammerPressed = False

            if event.type == timeForBreakEvent:
                timeForBreak = False


        hammer.update(mousePosition)
        hammer_hit.update(mousePosition)

        gameDisplay.blit(background, (0,0))

        ScoreBoxButton.draw(gameDisplay)
        livesButton.draw(gameDisplay)
        screenMessage("{}".format(str(score)), (255, 255, 255), 250, 40)
        screenMessage("{}".format(str(lifes)),(255,255,255), 710, 40)
        if not moleDrawn and not timeForBreak:
            holeNumber = random.randrange(len(holes))
            mole.update(holes[holeNumber])
            pygame.time.set_timer(moleDisappearEvent, maxMoleTime)

        if maxMoleTime >500 and score >level*100:
            maxMoleTime -= 500
            level += 1

        if not isMoleHitted and not timeForBreak:
            mole.draw(gameDisplay)
            moleDrawn = True
        elif not timeForBreak:
            moleHit.draw(gameDisplay)
            moleDrawn = True

        if not isHammerPressed:
            hammer.draw(gameDisplay)
        else:
            hammer_hit.draw(gameDisplay)

        if(lifes == 0):
            for i in range(len(highscores)):
                if(score> int(highscores[i][1])):
                    name = InputBox.ask(gameDisplay, "Enter your name")
                    highscores[i] = (name,str(score))
                    break
            isMenu = True
            isStart = False
        pygame.display.update()

file = open(os.path.join("data","highscore.txt"),"w")
for i in highscores:
    file.write(i[0]+","+i[1]+"\n")
file.close()

pygame.quit()