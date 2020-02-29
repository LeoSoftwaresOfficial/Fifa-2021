import pygame, math, random, time
from pygame import mixer

#gameinit

pygame.init()
gamestate = 1

#lobby

fontlobby = pygame.font.Font("pixel.ttf", 50)
fontbutton = pygame.font.Font("pixel.ttf", 20)
lmind = 1

def lobby():
    title = fontlobby.render("FIFA 2021", True, (255, 0, 0))
    screen.blit(title, (275, 10))
    title = fontbutton.render("premi esc per uscire", True, (0, 0, 0))
    screen.blit(title, (275, 400))
    pygame.draw.rect(screen, (0, 0, 0), (300, 250, 200, 100))
    btext = fontbutton.render("Gioca", True, (255, 255, 255))
    screen.blit(btext, (375, 290))

def lobbymusic():
    if lmind == 1:
        mixer.music.load('lobby.wav')
        mixer.music.play(-1)
    else:
        pass

#player1

pl1img = pygame.image.load('player1.png')
player1x = 200
player1y = 300

def player1(x, y):
    screen.blit(pl1img, (x, y))

#player2

pl2img = pygame.image.load('player2.png')
player2x = 600
player2y = 300

def player2(x, y):
    screen.blit(pl2img, (x, y))

#palla

pallaimg = pygame.image.load('ball.png')
pallax = 400
pallay = 300
plp = 0
a = 10
launch = 0
ls = 0

def palla(x,y):
    screen.blit(pallaimg, (x, y))

def preso(player1x, player1y, player2x, player2y, pallax, pallay):
    displ1 = math.sqrt((math.pow(player1x - pallax, 2)) + (math.pow(player1y - pallay, 2)))
    displ2 = math.sqrt((math.pow(player2x - pallax, 2)) + (math.pow(player2y - pallay, 2)))
    if displ1 <= 27 and displ2 >= 27:
        return 0
    elif displ2 <= 27 and displ1 >= 27:
        return 1
    elif displ1 <= 27 and displ2 <= 27:
        return 2
    else:
        return 3

#score

puntir = 0
puntib = 0
font = pygame.font.Font('pixel.ttf', 32)
scorex = 10
scorey = 10

def scoretab(x,y):
    scoreb = font.render("Score Blu : " + str(puntib), True, (255, 255, 255))
    screen.blit(scoreb, (x, y))
    scorer = font.render("Score Rosso : " + str(puntir), True, (255, 255, 255))
    screen.blit(scorer, (10, 42))

#winscreen

fontr = pygame.font.Font('pixel.ttf', 32)
fontb = pygame.font.Font('pixel.ttf', 10)

def winr():
    tr = fontr.render("Vince il Rosso", True, (255, 0, 0))
    screen.blit(tr, (300, 200))
    t2 = fontb.render("premi capslock per tornare alla lobby", True, (0, 0, 255))
    screen.blit(t2, (300, 250))

def winb():
    tb = fontr.render("Vince il Blu", True, (0, 0, 255))
    screen.blit(tb, (300, 200))
    t3 = fontb.render("premi capslock per tornare alla lobby", True, (0, 0, 255))
    screen.blit(t3, (300, 250))

#musictheme

mtind = 1

def maintheme():
    if mtind == 1:
        mixer.music.load('backmusic.wav')
        mixer.music.play(-1)
    else:
        pass

#gameloop

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("FIFA 2021")
icon = pygame.image.load('icon.png')
background = pygame.image.load('pitch.png')
pygame.display.set_icon(icon)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if gamestate == 0:
        run = False
    if gamestate == 1:
        mtind = 1
        lobbymusic()
        lmind = 0
        screen.fill((190, 239, 237))
        lobby()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mx >= 300 and mx <= 600 and my >= 250 and my <= 450:
                gamestate = 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gamestate = 0
    if gamestate == 2:
        lmind = 1
        maintheme()
        mtind = 0
        if event.type == pygame.KEYDOWN:
            #player1commands
            if event.key == pygame.K_UP:
                    player2y -= 1
                    dir = 0
            if event.key == pygame.K_LEFT:
                    player2x -= 1
                    dir = 1
            if event.key == pygame.K_RIGHT:
                    player2x += 1
                    dir = 3
            if event.key == pygame.K_DOWN:
                    player2y += 1
                    dir = 2
            if event.key == pygame.K_RSHIFT:
                    launch = 1
            #player2commands
            if event.key == pygame.K_w:
                    player1y -= 1
                    dir = 10
            if event.key == pygame.K_a:
                    player1x -= 1
                    dir = 11
            if event.key == pygame.K_d:
                    player1x += 1
                    dir = 13
            if event.key == pygame.K_s:
                    player1y += 1
                    dir = 12
            if event.key == pygame.K_e:
                    launch = 1
            #tolobby
            if event.key == pygame.K_CAPSLOCK:
                    gamestate = 1

        screen.blit(background, (0, 0))
        player1(player1x, player1y)
        if player1x >= 736:
            player1x = 736
        if player1x <= 0:
            player1x = 0
        if player1y >= 536:
            player1y = 536
        if player1y <= 0:
            player1y = 0
        player2(player2x, player2y)
        if player2x >= 736:
            player2x = 736
        if player2x <= 0:
            player2x = 0
        if player2y >= 536:
            player2y = 536
        if player2y <= 0:
            player2y = 0
        palla(pallax, pallay)
        if pallax >= 736:
            pallax = 736
        if pallax <= 0:
            pallax = 0
        if pallay >= 536:
            pallay = 536
        if pallay <= 0:
            pallay = 0
        pr = preso(player1x, player1y, player2x, player2y, pallax, pallay)
        if pr == 0 and ls == 0:
            pallax = player1x
            pallay = player1y
            plp = 1
        if pr == 1 and ls == 0:
            pallax = player2x
            pallay = player2y
            plp = 2
        if pr == 2 and ls == 0:
            caso = random.randint(1,3)
            if caso == 1:
                pallax = player1x
                pallay = player1y
                plp = 1
            if caso == 2:
                pallax = player2x
                pallay = player2y
                plp = 2
        if pr == 3:
            pass
        if launch == 1:
            if dir == 0 and plp == 2:
                    pallay -= 150
                    lsound = mixer.Sound('launch.wav')
                    lsound.play()
                    launch = 0
                    ls = 1
                    time.sleep(0.3)
                    ls = 0
                    plp = 0
            if dir == 1 and plp == 2:
                    pallax -= 150
                    lsound = mixer.Sound('launch.wav')
                    lsound.play()
                    launch = 0
                    ls = 1
                    time.sleep(0.3)
                    ls = 0
                    plp = 0
            if dir == 2 and plp == 2:
                    pallay += 150
                    lsound = mixer.Sound('launch.wav')
                    lsound.play()
                    launch = 0
                    ls = 1
                    time.sleep(0.3)
                    ls = 0
                    plp = 0
            if dir == 3 and plp == 2:
                    pallax += 150
                    lsound = mixer.Sound('launch.wav')
                    lsound.play()
                    launch = 0
                    ls = 1
                    time.sleep(0.3)
                    ls = 0
                    plp = 0
            if dir == 10 and plp == 1:
                    pallay -= 150
                    lsound = mixer.Sound('launch.wav')
                    lsound.play()
                    launch = 0
                    ls = 1
                    time.sleep(0.3)
                    ls = 0
                    plp = 0
            if dir == 11 and plp == 1:
                    pallax -= 150
                    lsound = mixer.Sound('launch.wav')
                    lsound.play()
                    launch = 0
                    ls = 1
                    time.sleep(0.3)
                    ls = 0
                    plp = 0
            if dir == 12 and plp == 1:
                    pallay += 150
                    lsound = mixer.Sound('launch.wav')
                    lsound.play()
                    launch = 0
                    ls = 1
                    time.sleep(0.3)
                    ls = 0
                    plp = 0
            if dir == 13 and plp == 1:
                    pallax += 150
                    lsound = mixer.Sound('launch.wav')
                    lsound.play()
                    launch = 0
                    ls = 1
                    time.sleep(0.3)
                    ls = 0
                    plp = 0
        scoretab(scorex, scorey)
        if pallay >= 150 and pallay <= 375 and pallax <= 10:
            puntir += 1
            pallax = 400
            pallay = 300
            player1x = 200
            player1y = 300
            player2x = 600
            player2y = 300
        if pallay >= 150 and pallay <= 375 and pallax >= 700:
            puntib += 1
            pallax = 400
            pallay = 300
            player1x = 200
            player1y = 300
            player2x = 600
            player2y = 300
        if puntir == 5:
            gamestate = 3
        if puntib == 5:
            gamestate = 4
    if gamestate == 3:
        mtind = 1
        screen.fill((255, 255, 255))
        winr()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_CAPSLOCK:
            time.sleep(0.5)
            puntib = 0
            puntir = 0
            gamestate = 1
    if gamestate == 4:
        mtind = 1
        screen.fill((255, 255, 255))
        winb()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_CAPSLOCK:
            time.sleep(0.5)
            puntib = 0
            puntir = 0
            gamestate = 1
    pygame.display.update()
