import pygame
import sys
import random
bg_y = 0
px = 315
py = 235
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
red = (255,0,0)
blue = (0,0,255)
bluegreen = (0,255,255)
life = 3   
inv = 0
cnt = 0
randwid = random.randint(50,150)
randy = random.randint(110,410-randwid) 
randx = random.randint(170,470-randwid)
clock = pygame.time.Clock()
def hit(x1,y1,width,height):
    global life,inv 
    xs = int(width/2 + 5)
    ys = int(height/2 + 5)
    lex = abs(x1 + width/2 - px - 5)
    ley = abs(y1 + height/2 - py - 5)
    if lex < xs and ley < ys and inv == 0:
        life -= 1
        inv = 50
def move_player(screen,key):
    global px,py
    pygame.draw.rect(screen,black,[px,py,10,10])
    if key[pygame.K_UP] == 1:
        py = py - 5
        if py < 110:
            py = 110
    if key[pygame.K_DOWN] == 1:
        py = py + 5
        if py > 400:
            py = 400
    if key[pygame.K_LEFT] == 1:
        px = px - 5
        if px < 170:
            px = 170
    if key[pygame.K_RIGHT] == 1:
        px = px + 5
        if px > 460:
            px = 460
    if inv > 0:
        pygame.draw.rect(screen,(0,255,0),[px,py,10,10])
    if inv == 0:
        pygame.draw.rect(screen,bluegreen,[px,py,10,10])
def life_management():
    global life, inv
    if inv > 0:
        inv -= 1
    if life == 2:
        pygame.draw.rect(screen,black,[350,440,20,20])
    if life == 1:
        pygame.draw.rect(screen,black,[310,440,20,20])
    if life == 0:
        pygame.draw.rect(screen,black,[270,440,20,20])
        game_end()
def game_end():
    global clock
    screen.fill(black)
    font = pygame.font.Font(None,80)
    screen.blit(font.render("GAME OVER",True,white),[160,240])
#def damage():
#    pygame.draw.rect(screen,blue,[200,300,20,20])
#    hit(200,300,20,20)
def attack1():
    global cnt,randwid,randy,randx
    if cnt == 0:
        randwid = random.randint(50,150)
        randy = random.randint(110,410-randwid) 
        randx = random.randint(170,470-randwid)
    pygame.draw.rect(screen,(cnt,cnt,0),[randx,randy,randwid,randwid])
    cnt += 1
    if cnt == 255:
        pygame.draw.rect(screen,red,[randx,randy,randwid,randwid])
        hit(randx,randy,randwid,randwid)
        pygame.draw.rect(screen,black,[170,110,300,300])
        cnt = 0
    if inv > 0:
        pygame.draw.rect(screen,(0,255,0),[px,py,10,10])
    if inv == 0:
        pygame.draw.rect(screen,bluegreen,[px,py,10,10])
def main(): 
    global screen
    pygame.init()
    pygame.display.set_caption("Battle")
    screen = pygame.display.set_mode((640,480))
    pygame.draw.rect(screen,white,[160,100,320,320])
    pygame.draw.rect(screen,black,[170,110,300,300])
    pygame.draw.rect(screen,red,[270,440,20,20])
    pygame.draw.rect(screen,red,[310,440,20,20])
    pygame.draw.rect(screen,red,[350,440,20,20])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        key = pygame.key.get_pressed()
        move_player(screen,key)
        attack1()
        life_management()
        pygame.display.update()
        clock.tick(70)
if __name__ == "__main__":
    main()