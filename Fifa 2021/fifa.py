import pygame, math, random, time
from pygame import mixer

#gameinit

pygame.init()
gamestate = 1

#font

fontr = pygame.font.Font('templates/text/pixel.ttf', 32)
fontb = pygame.font.Font('templates/text/pixel.ttf', 10)
fontlobby = pygame.font.Font("templates/text/pixel.ttf", 50)
fontbutton = pygame.font.Font("templates/text/pixel.ttf", 20)
font = pygame.font.Font('templates/text/pixel.ttf', 32)

#lobby

def lobby():
    title = fontlobby.render("FIFA 2021", True, (255, 0, 0))
    screen.blit(title, (275, 10))
    title = fontbutton.render("premi esc per uscire", True, (0, 0, 0))
    screen.blit(title, (275, 400))
    pygame.draw.rect(screen, (0, 0, 0), (300, 250, 200, 100))
    btext = fontbutton.render("Gioca", True, (255, 255, 255))
    screen.blit(btext, (375, 290))
    pygame.draw.rect(screen, (0, 0, 0), (25, 250, 200, 100))
    btext = fontbutton.render("Skin", True, (255, 255, 255))
    screen.blit(btext, (100, 290))
    pygame.draw.rect(screen, (0, 0, 0), (575, 250, 200, 100))
    btext = fontbutton.render("Impostazioni", True, (255, 255, 255))
    screen.blit(btext, (600, 290))

#music

lmind = 1
mtind = 1

def lobbymusic():
    if lmind == 1:
        mixer.music.load('templates/music/lobby.wav')
        mixer.music.play(-1)
    else:
        pass

def maintheme():
    if mtind == 1:
        mixer.music.load('templates/music/backmusic.wav')
        mixer.music.play(-1)
    else:
        pass

#skins

plset = 0
cond = 1
select1 = pygame.image.load('skin/player1.png')
select2 = pygame.image.load('skin/player2.png')
select3 = pygame.image.load('skin/player3.png')
select4 = pygame.image.load('skin/player4.png')
select5 = pygame.image.load('skin/player5.png')
select6 = pygame.image.load('skin/player6.png')
select7 = pygame.image.load('skin/player7.png')
select8 = pygame.image.load('skin/player8.png')
select9 = pygame.image.load('skin/player9.png')
select10 = pygame.image.load('skin/player10.png')

pl1imgs = select1
pl2imgs = select2

def skinpage():
    screen.blit(select1, (240, 100))
    screen.blit(select2, (272, 100))
    screen.blit(select3, (304, 100))
    screen.blit(select4, (336, 100))
    screen.blit(select5, (368, 100))
    screen.blit(select6, (400, 100))
    screen.blit(select7, (432, 100))
    screen.blit(select8, (464, 100))
    screen.blit(select9, (496, 100))
    screen.blit(select10, (528, 100))
    select = font.render("Clicca sulla skin desiderata", True, (0,0,0))
    screen.blit(select, (125, 368))

def skinselect():
    select = font.render("Clicca sulla skin che si vuole cambiare", True, (0,0,0))
    screen.blit(select, (25, 168))
    pygame.draw.rect(screen, (0, 0, 0), (150, 250, 200, 100))
    btext = fontbutton.render("Player 1", True, (255, 255, 255))
    screen.blit(btext, (175, 290))
    pygame.draw.rect(screen, (0, 0, 0), (450, 250, 200, 100))
    btext = fontbutton.render("Player 2", True, (255, 255, 255))
    screen.blit(btext, (475, 290))

#keybinds

a = pygame.K_a
b = pygame.K_b
c = pygame.K_c
d = pygame.K_d
e = pygame.K_e
f = pygame.K_f
g = pygame.K_g
h = pygame.K_h
i = pygame.K_i
j = pygame.K_j
k = pygame.K_k
l = pygame.K_l
m = pygame.K_m
n = pygame.K_n
o = pygame.K_o
p = pygame.K_p
q = pygame.K_q
r = pygame.K_r
s = pygame.K_s
t = pygame.K_t
u = pygame.K_u
v = pygame.K_v
w = pygame.K_w
x = pygame.K_x
y = pygame.K_y
z = pygame.K_z
k1k = pygame.K_1
k2k = pygame.K_2
k3k = pygame.K_3
k4k = pygame.K_4
k5k = pygame.K_5
k6k = pygame.K_6
k7k = pygame.K_7
k8k = pygame.K_8
k9k = pygame.K_9
k0k = pygame.K_0
up = pygame.K_UP
down = pygame.K_DOWN
left = pygame.K_LEFT
right = pygame.K_RIGHT
rshift = pygame.K_RSHIFT
lshift = pygame.K_LSHIFT

p1mu = w
p1md = s
p1ml = a
p1mr = d
p1mk = e
p2mu = up
p2md = down
p2ml = left
p2mr = right
p2mk = rshift

def settings():
    pygame.draw.rect(screen, (0,0,0), (20,200,50,50))
    pygame.draw.rect(screen, (0,0,0), (80,200,50,50))
    pygame.draw.rect(screen, (0,0,0), (140,200,50,50))
    pygame.draw.rect(screen, (0,0,0), (80,140,50,50))
    pygame.draw.rect(screen, (0,0,0), (250,160,50,50))
    pygame.draw.rect(screen, (0,0,0), (20,400,50,50))
    pygame.draw.rect(screen, (0,0,0), (80,400,50,50))
    pygame.draw.rect(screen, (0,0,0), (140,400,50,50))
    pygame.draw.rect(screen, (0,0,0), (80,340,50,50))
    pygame.draw.rect(screen, (0,0,0), (250,360,50,50))
    mov = font.render("Movimento", True, (0,0,0))
    shoot = font.render("Calcio", True, (0,0,0))
    pl1 = font.render("Player 1", True, (0,0,0))
    pl2 = font.render("Player 2", True, (0,0,0))
    screen.blit(mov, (20, 500))
    screen.blit(shoot, (250, 500))
    screen.blit(pl1, (600, 150))
    screen.blit(pl2, (600, 350))
    pygame.draw.rect(screen, (255,0,0), (700,460,100,50))
    esci = font.render("Esci", True, (255,255,255))
    screen.blit(esci, (710, 470))


#player1

player1x = 200
player1y = 300

def player1(x, y):
    screen.blit(pl1imgs, (x, y))

#player2

player2x = 600
player2y = 300

def player2(x, y):
    screen.blit(pl2imgs, (x, y))

#palla

pallaimg = pygame.image.load('templates/imgs/ball.png')
pallax = 400
pallay = 300
plp = 0
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
scorex = 10
scorey = 10

def scoretab(x,y):
    scoreb = font.render("Score Player1 : " + str(puntib), True, (255, 255, 255))
    screen.blit(scoreb, (x, y))
    scorer = font.render("Score Player2 : " + str(puntir), True, (255, 255, 255))
    screen.blit(scorer, (10, 42))

#winscreen

def winr():
    tr = fontr.render("Vince il Rosso", True, (255, 0, 0))
    screen.blit(tr, (300, 200))
    t2 = fontb.render("premi capslock per tornare alla lobby", True, (255, 0, 0))
    screen.blit(t2, (300, 250))

def winb():
    tb = fontr.render("Vince il Blu", True, (0, 0, 255))
    screen.blit(tb, (300, 200))
    t3 = fontb.render("premi capslock per tornare alla lobby", True, (0, 0, 255))
    screen.blit(t3, (300, 250))

#gameloop

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("FIFA 2021")
icon = pygame.image.load('templates/imgs/icon.png')
background = pygame.image.load('templates/imgs/pitch.png')
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
            if mx >= 300 and mx <= 500 and my >= 250 and my <= 450:
                gamestate = 2
            if mx >= 25 and mx <= 225 and my >= 250 and my <= 450:
                gamestate = 5
            if mx >= 575 and mx <= 775 and my >= 250 and my <= 450:
                gamestate = 8
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gamestate = 0
    if gamestate == 2:
        lmind = 1
        maintheme()
        mtind = 0
        if event.type == pygame.KEYDOWN:
            #player1commands
            if event.key == p2mu:
                    player2y -= 1
                    dir = 0
            if event.key == p2ml:
                    player2x -= 1
                    dir = 1
            if event.key == p2mr:
                    player2x += 1
                    dir = 3
            if event.key == p2md:
                    player2y += 1
                    dir = 2
            if event.key == p2mk:
                    launch = 1
            #player2commands
            if event.key == p1mu:
                    player1y -= 1
                    dir = 10
            if event.key == p1ml:
                    player1x -= 1
                    dir = 11
            if event.key == p1mr:
                    player1x += 1
                    dir = 13
            if event.key == p1md:
                    player1y += 1
                    dir = 12
            if event.key == p1mk:
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
                    lsound = mixer.Sound('templates/music/launch.wav')
                    lsound.play()
                    launch = 0
                    ls = 1
                    time.sleep(0.3)
                    ls = 0
                    plp = 0
            if dir == 1 and plp == 2:
                    pallax -= 150
                    lsound = mixer.Sound('templates/music/launch.wav')
                    lsound.play()
                    launch = 0
                    ls = 1
                    time.sleep(0.3)
                    ls = 0
                    plp = 0
            if dir == 2 and plp == 2:
                    pallay += 150
                    lsound = mixer.Sound('templates/music/launch.wav')
                    lsound.play()
                    launch = 0
                    ls = 1
                    time.sleep(0.3)
                    ls = 0
                    plp = 0
            if dir == 3 and plp == 2:
                    pallax += 150
                    lsound = mixer.Sound('templates/music/launch.wav')
                    lsound.play()
                    launch = 0
                    ls = 1
                    time.sleep(0.3)
                    ls = 0
                    plp = 0
            if dir == 10 and plp == 1:
                    pallay -= 150
                    lsound = mixer.Sound('templates/music/launch.wav')
                    lsound.play()
                    launch = 0
                    ls = 1
                    time.sleep(0.3)
                    ls = 0
                    plp = 0
            if dir == 11 and plp == 1:
                    pallax -= 150
                    lsound = mixer.Sound('templates/music/launch.wav')
                    lsound.play()
                    launch = 0
                    ls = 1
                    time.sleep(0.3)
                    ls = 0
                    plp = 0
            if dir == 12 and plp == 1:
                    pallay += 150
                    lsound = mixer.Sound('templates/music/launch.wav')
                    lsound.play()
                    launch = 0
                    ls = 1
                    time.sleep(0.3)
                    ls = 0
                    plp = 0
            if dir == 13 and plp == 1:
                    pallax += 150
                    lsound = mixer.Sound('templates/music/launch.wav')
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
    if gamestate == 5:
        screen.fill((190, 239, 237))
        skinselect()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mx >= 175 and mx <= 375 and my >= 250 and my <= 450:
                gamestate = 6
            if mx >= 475 and mx <= 675 and my >= 250 and my <= 450:
                gamestate = 7
    if gamestate == 6:
        screen.fill((190, 239, 237))
        skinpage()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mx >= 240 and mx <= 271 and my >= 100 and my <= 132:
                pl1imgs = select1
                gamestate = 1
            if mx >= 272 and mx <= 304 and my >= 100 and my <= 132:
                pl1imgs = select2
                gamestate = 1
            if mx >= 304 and mx <= 335 and my >= 100 and my <= 132:
                pl1imgs = select3
                gamestate = 1
            if mx >= 336 and mx <= 367 and my >= 100 and my <= 132:
                pl1imgs = select4
                gamestate = 1
            if mx >= 368 and mx <= 399 and my >= 100 and my <= 132:
                pl1imgs = select5
                gamestate = 1
            if mx >= 400 and mx <= 431 and my >= 100 and my <= 132:
                pl1imgs = select6
                gamestate = 1
            if mx >= 432 and mx <= 463 and my >= 100 and my <= 132:
                pl1imgs = select7
                gamestate = 1
            if mx >= 464 and mx <= 495 and my >= 100 and my <= 132:
                pl1imgs = select8
                gamestate = 1
            if mx >= 496 and mx <= 527 and my >= 100 and my <= 132:
                pl1imgs = select9
                gamestate = 1
            if mx >= 528 and mx <= 560 and my >= 100 and my <= 132:
                pl1imgs = select10
                gamestate = 1
    if gamestate == 7:
        screen.fill((190, 239, 237))
        skinpage()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mx >= 240 and mx <= 271 and my >= 100 and my <= 132:
                pl2imgs = select1
                gamestate = 1
            if mx >= 272 and mx <= 304 and my >= 100 and my <= 132:
                pl2imgs = select2
                gamestate = 1
            if mx >= 304 and mx <= 335 and my >= 100 and my <= 132:
                pl2imgs = select3
                gamestate = 1
            if mx >= 336 and mx <= 367 and my >= 100 and my <= 132:
                pl2imgs = select4
                gamestate = 1
            if mx >= 368 and mx <= 399 and my >= 100 and my <= 132:
                pl2imgs = select5
                gamestate = 1
            if mx >= 400 and mx <= 431 and my >= 100 and my <= 132:
                pl2imgs = select6
                gamestate = 1
            if mx >= 432 and mx <= 463 and my >= 100 and my <= 132:
                pl2imgs = select7
                gamestate = 1
            if mx >= 464 and mx <= 495 and my >= 100 and my <= 132:
                pl1imgs = select8
                gamestate = 1
            if mx >= 496 and mx <= 527 and my >= 100 and my <= 132:
                pl2imgs = select9
                gamestate = 1
            if mx >= 528 and mx <= 560 and my >= 100 and my <= 132:
                pl2imgs = select10
                gamestate = 1
    if gamestate == 8:
        screen.fill((190,239,237))
        settings()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mx >= 20 and mx <= 70 and my >= 200 and my <= 250:
                gamestate = 9
                cond = 2
                plset = 1
            if mx >= 80 and mx <= 130 and my >= 200 and my <= 250:
                gamestate = 9
                cond = 3
                plset = 1
            if mx >= 140 and mx <= 190 and my >= 200 and my <= 250:
                gamestate = 9
                cond = 4
                plset = 1
            if mx >= 80 and mx <= 130 and my >= 140 and my <= 190:
                gamestate = 9
                cond = 1
                plset = 1
            if mx >= 250 and mx <= 300 and my >= 160 and my <= 210:
                gamestate = 9
                cond = 5
                plset = 1
            if mx >= 20 and mx <= 70 and my >= 400 and my <= 450:
                gamestate = 9
                cond = 2
                plset = 2
            if mx >= 80 and mx <= 130 and my >= 400 and my <= 450:
                gamestate = 9
                cond = 3
                plset = 2
            if mx >= 140 and mx <= 190 and my >= 400 and my <= 450:
                gamestate = 9
                cond = 4
                plset = 2
            if mx >= 80 and mx <= 130 and my >= 340 and my <= 390:
                gamestate = 9
                cond = 1
                plset = 2
            if mx >= 250 and mx <= 300 and my >= 360 and my <= 410:
                gamestate = 9
                cond = 5
                plset = 2
            if mx >= 700 and my >= 460 and my <= 510:
                gamestate = 1
    if gamestate == 9:
        screen.fill((190,239,237))
        if plset == 1:
            if cond == 1:
                if event.type == pygame.KEYDOWN:
                    if event.key == a:
                        p1mu = a
                    if event.key == b:
                        p1mu = b
                    if event.key == c:
                        p1mu = c
                    if event.key == d:
                        p1mu = d
                    if event.key == e:
                        p1mu = e
                    if event.key == f:
                        p1mu = f
                    if event.key == g:
                        p1mu = g
                    if event.key == h:
                        p1mu = h
                    if event.key == i:
                        p1mu = i
                    if event.key == j:
                        p1mu = j
                    if event.key == k:
                        p1mu = k
                    if event.key == l:
                        p1mu = l
                    if event.key == m:
                        p1mu = m
                    if event.key == n:
                        p1mu = n
                    if event.key == o:
                        p1mu = o
                    if event.key == p:
                        p1mu = p
                    if event.key == q:
                        p1mu = q
                    if event.key == r:
                        p1mu = r
                    if event.key == s:
                        p1mu = s
                    if event.key == t:
                        p1mu = t
                    if event.key == u:
                        p1mu = u
                    if event.key == v:
                        p1mu = v
                    if event.key == w:
                        p1mu = w
                    if event.key == x:
                        p1mu = x
                    if event.key == y:
                        p1mu = y
                    if event.key == z:
                        p1mu = z
                    if event.key == k1k:
                        p1mu = k1k
                    if event.key == k2k:
                        p1mu = k2k
                    if event.key == k3k:
                        p1mu = k3k
                    if event.key == k4k:
                        p1mu = k4k
                    if event.key == k5k:
                        p1mu = k5k
                    if event.key == k6k:
                        p1mu = k6k
                    if event.key == k7k:
                        p1mu = k7k
                    if event.key == k8k:
                        p1mu = k8k
                    if event.key == k9k:
                        p1mu = k9k
                    if event.key == k0k:
                        p1mu = k0k
                    if event.key == up:
                        p1mu = up
                    if event.key == down:
                        p1mu = down
                    if event.key == left:
                        p1mu = left
                    if event.key == right:
                        p1mu = right
                    if event.key == lshift:
                        p1mu = lshift
                    if event.key == rshift:
                        p1mu = rshift
            if cond == 2:
                if event.type == pygame.KEYDOWN:
                    if event.key == a:
                        p1ml = a
                    if event.key == b:
                        p1ml = b
                    if event.key == c:
                        p1ml = c
                    if event.key == d:
                        p1ml = d
                    if event.key == e:
                        p1ml = e
                    if event.key == f:
                        p1ml = f
                    if event.key == g:
                        p1ml = g
                    if event.key == h:
                        p1ml = h
                    if event.key == i:
                        p1ml = i
                    if event.key == j:
                        p1ml = j
                    if event.key == k:
                        p1ml = k
                    if event.key == l:
                        p1ml = l
                    if event.key == m:
                        p1ml = m
                    if event.key == n:
                        p1ml = n
                    if event.key == o:
                        p1ml = o
                    if event.key == p:
                        p1ml = p
                    if event.key == q:
                        p1ml = q
                    if event.key == r:
                        p1ml = r
                    if event.key == s:
                        p1ml = s
                    if event.key == t:
                        p1ml = t
                    if event.key == u:
                        p1ml = u
                    if event.key == v:
                        p1ml = v
                    if event.key == w:
                        p1ml = w
                    if event.key == x:
                        p1ml = x
                    if event.key == y:
                        p1ml = y
                    if event.key == z:
                        p1ml = z
                    if event.key == k1k:
                        p1ml = k1k
                    if event.key == k2k:
                        p1ml = k2k
                    if event.key == k3k:
                        p1ml = k3k
                    if event.key == k4k:
                        p1ml = k4k
                    if event.key == k5k:
                        p1ml = k5k
                    if event.key == k6k:
                        p1ml = k6k
                    if event.key == k7k:
                        p1ml = k7k
                    if event.key == k8k:
                        p1ml = k8k
                    if event.key == k9k:
                        p1ml = k9k
                    if event.key == k0k:
                        p1ml = k0k
                    if event.key == up:
                        p1ml = up
                    if event.key == down:
                        p1ml = down
                    if event.key == left:
                        p1ml = left
                    if event.key == right:
                        p1ml = right
                    if event.key == lshift:
                        p1ml = lshift
                    if event.key == rshift:
                        p1ml = rshift
            if cond == 3:
                if event.type == pygame.KEYDOWN:
                    if event.key == a:
                        p1md = a
                    if event.key == b:
                        p1md = b
                    if event.key == c:
                        p1md = c
                    if event.key == d:
                        p1md = d
                    if event.key == e:
                        p1md = e
                    if event.key == f:
                        p1md = f
                    if event.key == g:
                        p1md = g
                    if event.key == h:
                        p1md = h
                    if event.key == i:
                        p1md = i
                    if event.key == j:
                        p1md = j
                    if event.key == k:
                        p1md = k
                    if event.key == l:
                        p1md = l
                    if event.key == m:
                        p1md = m
                    if event.key == n:
                        p1md = n
                    if event.key == o:
                        p1md = o
                    if event.key == p:
                        p1md = p
                    if event.key == q:
                        p1md = q
                    if event.key == r:
                        p1md = r
                    if event.key == s:
                        p1md = s
                    if event.key == t:
                        p1md = t
                    if event.key == u:
                        p1md = u
                    if event.key == v:
                        p1md = v
                    if event.key == w:
                        p1md = w
                    if event.key == x:
                        p1md = x
                    if event.key == y:
                        p1md = y
                    if event.key == z:
                        p1md = z
                    if event.key == k1k:
                        p1md = k1k
                    if event.key == k2k:
                        p1md = k2k
                    if event.key == k3k:
                        p1md = k3k
                    if event.key == k4k:
                        p1md = k4k
                    if event.key == k5k:
                        p1md = k5k
                    if event.key == k6k:
                        p1md = k6k
                    if event.key == k7k:
                        p1md = k7k
                    if event.key == k8k:
                        p1md = k8k
                    if event.key == k9k:
                        p1md = k9k
                    if event.key == k0k:
                        p1md = k0k
                    if event.key == up:
                        p1md = up
                    if event.key == down:
                        p1md = down
                    if event.key == left:
                        p1md = left
                    if event.key == right:
                        p1md = right
                    if event.key == lshift:
                        p1md = lshift
                    if event.key == rshift:
                        p1md = rshift
            if cond == 4:
                if event.type == pygame.KEYDOWN:
                    if event.key == a:
                        p1mr = a
                    if event.key == b:
                        p1mr = b
                    if event.key == c:
                        p1mr = c
                    if event.key == d:
                        p1mr = d
                    if event.key == e:
                        p1mr = e
                    if event.key == f:
                        p1mr = f
                    if event.key == g:
                        p1mr = g
                    if event.key == h:
                        p1mr = h
                    if event.key == i:
                        p1mr = i
                    if event.key == j:
                        p1mr = j
                    if event.key == k:
                        p1mr = k
                    if event.key == l:
                        p1mr = l
                    if event.key == m:
                        p1mr = m
                    if event.key == n:
                        p1mr = n
                    if event.key == o:
                        p1mr = o
                    if event.key == p:
                        p1mr = p
                    if event.key == q:
                        p1mr = q
                    if event.key == r:
                        p1mr = r
                    if event.key == s:
                        p1mr = s
                    if event.key == t:
                        p1mr = t
                    if event.key == u:
                        p1mr = u
                    if event.key == v:
                        p1mr = v
                    if event.key == w:
                        p1mr = w
                    if event.key == x:
                        p1mr = x
                    if event.key == y:
                        p1mr = y
                    if event.key == z:
                        p1mr = z
                    if event.key == k1k:
                        p1mr = k1k
                    if event.key == k2k:
                        p1mr = k2k
                    if event.key == k3k:
                        p1mr = k3k
                    if event.key == k4k:
                        p1mr = k4k
                    if event.key == k5k:
                        p1mr = k5k
                    if event.key == k6k:
                        p1mr = k6k
                    if event.key == k7k:
                        p1mr = k7k
                    if event.key == k8k:
                        p1mr = k8k
                    if event.key == k9k:
                        p1mr = k9k
                    if event.key == k0k:
                        p1mr = k0k
                    if event.key == up:
                        p1mr = up
                    if event.key == down:
                        p1mr = down
                    if event.key == left:
                        p1mr = left
                    if event.key == right:
                        p1mr = right
                    if event.key == lshift:
                        p1mr = lshift
                    if event.key == rshift:
                        p1mr = rshift
            if cond == 5:
                if event.type == pygame.KEYDOWN:
                    if event.key == a:
                        p1mk = a
                    if event.key == b:
                        p1mk = b
                    if event.key == c:
                        p1mk = c
                    if event.key == d:
                        p1mk = d
                    if event.key == e:
                        p1mk = e
                    if event.key == f:
                        p1mk = f
                    if event.key == g:
                        p1mk = g
                    if event.key == h:
                        p1mk = h
                    if event.key == i:
                        p1mk = i
                    if event.key == j:
                        p1mk = j
                    if event.key == k:
                        p1mk = k
                    if event.key == l:
                        p1mk = l
                    if event.key == m:
                        p1mk = m
                    if event.key == n:
                        p1mk = n
                    if event.key == o:
                        p1mk = o
                    if event.key == p:
                        p1mk = p
                    if event.key == q:
                        p1mk = q
                    if event.key == r:
                        p1mk = r
                    if event.key == s:
                        p1mk = s
                    if event.key == t:
                        p1mk = t
                    if event.key == u:
                        p1mk = u
                    if event.key == v:
                        p1mk = v
                    if event.key == w:
                        p1mk = w
                    if event.key == x:
                        p1mk = x
                    if event.key == y:
                        p1mk = y
                    if event.key == z:
                        p1mk = z
                    if event.key == k1k:
                        p1mk = k1k
                    if event.key == k2k:
                        p1mk = k2k
                    if event.key == k3k:
                        p1mk = k3k
                    if event.key == k4k:
                        p1mk = k4k
                    if event.key == k5k:
                        p1mk = k5k
                    if event.key == k6k:
                        p1mk = k6k
                    if event.key == k7k:
                        p1mk = k7k
                    if event.key == k8k:
                        p1mk = k8k
                    if event.key == k9k:
                        p1mk = k9k
                    if event.key == k0k:
                        p1mk = k0k
                    if event.key == up:
                        p1mk = up
                    if event.key == down:
                        p1mk = down
                    if event.key == left:
                        p1mk = left
                    if event.key == right:
                        p1mk = right
                    if event.key == lshift:
                        p1mk = lshift
                    if event.key == rshift:
                        p1mk = rshift
        if plset == 2:
            if cond == 1:
                if event.type == pygame.KEYDOWN:
                    if event.key == a:
                        p2mu = a
                    if event.key == b:
                        p2mu = b
                    if event.key == c:
                        p2mu = c
                    if event.key == d:
                        p2mu = d
                    if event.key == e:
                        p2mu = e
                    if event.key == f:
                        p2mu = f
                    if event.key == g:
                        p2mu = g
                    if event.key == h:
                        p2mu = h
                    if event.key == i:
                        p2mu = i
                    if event.key == j:
                        p2mu = j
                    if event.key == k:
                        p2mu = k
                    if event.key == l:
                        p2mu = l
                    if event.key == m:
                        p2mu = m
                    if event.key == n:
                        p2mu = n
                    if event.key == o:
                        p2mu = o
                    if event.key == p:
                        p2mu = p
                    if event.key == q:
                        p2mu = q
                    if event.key == r:
                        p2mu = r
                    if event.key == s:
                        p2mu = s
                    if event.key == t:
                        p2mu = t
                    if event.key == u:
                        p2mu = u
                    if event.key == v:
                        p2mu = v
                    if event.key == w:
                        p2mu = w
                    if event.key == x:
                        p2mu = x
                    if event.key == y:
                        p2mu = y
                    if event.key == z:
                        p2mu = z
                    if event.key == k1k:
                        p2mu = k1k
                    if event.key == k2k:
                        p2mu = k2k
                    if event.key == k3k:
                        p2mu = k3k
                    if event.key == k4k:
                        p2mu = k4k
                    if event.key == k5k:
                        p2mu = k5k
                    if event.key == k6k:
                        p2mu = k6k
                    if event.key == k7k:
                        p2mu = k7k
                    if event.key == k8k:
                        p2mu = k8k
                    if event.key == k9k:
                        p2mu = k9k
                    if event.key == k0k:
                        p2mu = k0k
                    if event.key == up:
                        p2mu = up
                    if event.key == down:
                        p2mu = down
                    if event.key == left:
                        p2mu = left
                    if event.key == right:
                        p2mu = right
                    if event.key == lshift:
                        p2mu = lshift
                    if event.key == rshift:
                        p2mu = rshift
            if cond == 2:
                if event.type == pygame.KEYDOWN:
                    if event.key == a:
                        p2ml = a
                    if event.key == b:
                        p2ml = b
                    if event.key == c:
                        p2ml = c
                    if event.key == d:
                        p2ml = d
                    if event.key == e:
                        p2ml = e
                    if event.key == f:
                        p2ml = f
                    if event.key == g:
                        p2ml = g
                    if event.key == h:
                        p2ml = h
                    if event.key == i:
                        p2ml = i
                    if event.key == j:
                        p2ml = j
                    if event.key == k:
                        p2ml = k
                    if event.key == l:
                        p2ml = l
                    if event.key == m:
                        p2ml = m
                    if event.key == n:
                        p2ml = n
                    if event.key == o:
                        p2ml = o
                    if event.key == p:
                        p2ml = p
                    if event.key == q:
                        p2ml = q
                    if event.key == r:
                        p2ml = r
                    if event.key == s:
                        p2ml = s
                    if event.key == t:
                        p2ml = t
                    if event.key == u:
                        p2ml = u
                    if event.key == v:
                        p2ml = v
                    if event.key == w:
                        p2ml = w
                    if event.key == x:
                        p2ml = x
                    if event.key == y:
                        p2ml = y
                    if event.key == z:
                        p2ml = z
                    if event.key == k1k:
                        p2ml = k1k
                    if event.key == k2k:
                        p2ml = k2k
                    if event.key == k3k:
                        p2ml = k3k
                    if event.key == k4k:
                        p2ml = k4k
                    if event.key == k5k:
                        p2ml = k5k
                    if event.key == k6k:
                        p2ml = k6k
                    if event.key == k7k:
                        p2ml = k7k
                    if event.key == k8k:
                        p2ml = k8k
                    if event.key == k9k:
                        p2ml = k9k
                    if event.key == k0k:
                        p2ml = k0k
                    if event.key == up:
                        p2ml = up
                    if event.key == down:
                        p2ml = down
                    if event.key == left:
                        p2ml = left
                    if event.key == right:
                        p2ml = right
                    if event.key == lshift:
                        p2ml = lshift
                    if event.key == rshift:
                        p2ml = rshift
            if cond == 3:
                if event.type == pygame.KEYDOWN:
                    if event.key == a:
                        p2md = a
                    if event.key == b:
                        p2md = b
                    if event.key == c:
                        p2md = c
                    if event.key == d:
                        p2md = d
                    if event.key == e:
                        p2md = e
                    if event.key == f:
                        p2md = f
                    if event.key == g:
                        p2md = g
                    if event.key == h:
                        p2md = h
                    if event.key == i:
                        p2md = i
                    if event.key == j:
                        p2md = j
                    if event.key == k:
                        p2md = k
                    if event.key == l:
                        p2md = l
                    if event.key == m:
                        p2md = m
                    if event.key == n:
                        p1md = n
                    if event.key == o:
                        p2md = o
                    if event.key == p:
                        p2md = p
                    if event.key == q:
                        p2md = q
                    if event.key == r:
                        p2md = r
                    if event.key == s:
                        p2md = s
                    if event.key == t:
                        p2md = t
                    if event.key == u:
                        p2md = u
                    if event.key == v:
                        p2md = v
                    if event.key == w:
                        p2md = w
                    if event.key == x:
                        p2md = x
                    if event.key == y:
                        p2md = y
                    if event.key == z:
                        p2md = z
                    if event.key == k1k:
                        p2md = k1k
                    if event.key == k2k:
                        p2md = k2k
                    if event.key == k3k:
                        p2md = k3k
                    if event.key == k4k:
                        p2md = k4k
                    if event.key == k5k:
                        p2md = k5k
                    if event.key == k6k:
                        p2md = k6k
                    if event.key == k7k:
                        p2md = k7k
                    if event.key == k8k:
                        p2md = k8k
                    if event.key == k9k:
                        p2md = k9k
                    if event.key == k0k:
                        p2md = k0k
                    if event.key == up:
                        p2md = up
                    if event.key == down:
                        p2md = down
                    if event.key == left:
                        p2md = left
                    if event.key == right:
                        p2md = right
                    if event.key == lshift:
                        p2md = lshift
                    if event.key == rshift:
                        p2md = rshift
            if cond == 4:
                if event.type == pygame.KEYDOWN:
                    if event.key == a:
                        p2mr = a
                    if event.key == b:
                        p2mr = b
                    if event.key == c:
                        p2mr = c
                    if event.key == d:
                        p2mr = d
                    if event.key == e:
                        p2mr = e
                    if event.key == f:
                        p2mr = f
                    if event.key == g:
                        p2mr = g
                    if event.key == h:
                        p2mr = h
                    if event.key == i:
                        p2mr = i
                    if event.key == j:
                        p2mr = j
                    if event.key == k:
                        p2mr = k
                    if event.key == l:
                        p2mr = l
                    if event.key == m:
                        p2mr = m
                    if event.key == n:
                        p2mr = n
                    if event.key == o:
                        p2mr = o
                    if event.key == p:
                        p2mr = p
                    if event.key == q:
                        p2mr = q
                    if event.key == r:
                        p2mr = r
                    if event.key == s:
                        p2mr = s
                    if event.key == t:
                        p2mr = t
                    if event.key == u:
                        p2mr = u
                    if event.key == v:
                        p2mr = v
                    if event.key == w:
                        p2mr = w
                    if event.key == x:
                        p2mr = x
                    if event.key == y:
                        p2mr = y
                    if event.key == z:
                        p2mr = z
                    if event.key == k1k:
                        p2mr = k1k
                    if event.key == k2k:
                        p2mr = k2k
                    if event.key == k3k:
                        p2mr = k3k
                    if event.key == k4k:
                        p2mr = k4k
                    if event.key == k5k:
                        p2mr = k5k
                    if event.key == k6k:
                        p2mr = k6k
                    if event.key == k7k:
                        p2mr = k7k
                    if event.key == k8k:
                        p2mr = k8k
                    if event.key == k9k:
                        p2mr = k9k
                    if event.key == k0k:
                        p2mr = k0k
                    if event.key == up:
                        p2mr = up
                    if event.key == down:
                        p2mr = down
                    if event.key == left:
                        p2mr = left
                    if event.key == right:
                        p2mr = right
                    if event.key == lshift:
                        p2mr = lshift
                    if event.key == rshift:
                        p2mr = rshift
            if cond == 5:
                if event.type == pygame.KEYDOWN:
                    if event.key == a:
                        p2mk = a
                    if event.key == b:
                        p2mk = b
                    if event.key == c:
                        p2mk = c
                    if event.key == d:
                        p2mk = d
                    if event.key == e:
                        p2mk = e
                    if event.key == f:
                        p2mk = f
                    if event.key == g:
                        p2mk = g
                    if event.key == h:
                        p2mk = h
                    if event.key == i:
                        p2mk = i
                    if event.key == j:
                        p2mk = j
                    if event.key == k:
                        p2mk = k
                    if event.key == l:
                        p2mk = l
                    if event.key == m:
                        p2mk = m
                    if event.key == n:
                        p2mk = n
                    if event.key == o:
                        p2mk = o
                    if event.key == p:
                        p2mk = p
                    if event.key == q:
                        p2mk = q
                    if event.key == r:
                        p2mk = r
                    if event.key == s:
                        p2mk = s
                    if event.key == t:
                        p2mk = t
                    if event.key == u:
                        p2mk = u
                    if event.key == v:
                        p2mk = v
                    if event.key == w:
                        p2mk = w
                    if event.key == x:
                        p2mk = x
                    if event.key == y:
                        p2mk = y
                    if event.key == z:
                        p2mk = z
                    if event.key == k1k:
                        p2mk = k1k
                    if event.key == k2k:
                        p2mk = k2k
                    if event.key == k3k:
                        p2mk = k3k
                    if event.key == k4k:
                        p2mk = k4k
                    if event.key == k5k:
                        p2mk = k5k
                    if event.key == k6k:
                        p2mk = k6k
                    if event.key == k7k:
                        p2mk = k7k
                    if event.key == k8k:
                        p2mk = k8k
                    if event.key == k9k:
                        p2mk = k9k
                    if event.key == k0k:
                        p2mk = k0k
                    if event.key == up:
                        p2mk = up
                    if event.key == down:
                        p2mk = down
                    if event.key == left:
                        p2mk = left
                    if event.key == right:
                        p2mk = right
                    if event.key == lshift:
                        p2mk = lshift
                    if event.key == rshift:
                        p2mk = rshift
        bexit = font.render("Premi un tasto per impostarlo", True, (0,0,0))
        bexit2 = fontb.render("Premi esc per ritornare alle Impostazioni", True, (0,0,0))
        screen.blit(bexit, (200, 200))
        screen.blit(bexit2, (200, 400))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gamestate = 8
    pygame.display.update()
