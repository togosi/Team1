import pygame
import sys
import random
bg_y = 0
px = 315
py = 410
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
red = (200,0,0)
blue = (0,0,255)
life = 100
inv = 0
cnt = 0
randwid = random.randint(50,150)
randy = random.randint(210,510-randwid) 
randx = random.randint(170,470-randwid)
clock = pygame.time.Clock()
def hit(dmg,x1,y1,width,height):
    global life,inv 
    xs = int(width/2 + 5)
    ys = int(height/2 + 5)
    lex = abs(x1 + width/2 - px - 5)
    ley = abs(y1 + height/2 - py - 5)
    if lex < xs and ley < ys and inv == 0:
        life -= dmg
        inv = 50
def pcl():
    if inv > 0:
        pygame.draw.rect(screen,(0,255,0),[px,py,10,10])
    if inv == 0:
        pygame.draw.rect(screen,(0,255,255),[px,py,10,10])
def move_player(screen,key):
    global px,py
    pygame.draw.rect(screen,black,[px,py,10,10])
    if key[pygame.K_UP] == 1:
        py = py - 5
        if py < 260:
            py = 260
    if key[pygame.K_DOWN] == 1:
        py = py + 5
        if py > 550:
            py = 550
    if key[pygame.K_LEFT] == 1:
        px = px - 5
        if px < 170:
            px = 170
    if key[pygame.K_RIGHT] == 1:
        px = px + 5
        if px > 460:
            px = 460
    pcl()
def life_management():
    global life, inv
    if inv > 0:
        inv -= 1
    pygame.draw.rect(screen,(128,128,0),[171+int(life/100*200),590,int((1-life/100)*200),30])
    ltxt = "HP:" + str(life) + "/100"
    font = pygame.font.Font(None,25)
    pygame.draw.rect(screen,black,[390,590,100,30])
    screen.blit(font.render(ltxt,True,white),[390,590])
    if life == 0:
        game_end()
def game_end():
    global clock
    screen.fill(black)
    font = pygame.font.Font(None,80)
    screen.blit(font.render("GAME OVER",True,white),[160,340])
    exit()
def attack1(dmg):
    global cnt,randwid,randy,randx
    if cnt == 0:
        randwid = random.randint(50,150)
        randy = random.randint(260,560-randwid) 
        randx = random.randint(170,470-randwid)
    if cnt < 250:
        pygame.draw.rect(screen,(cnt,cnt,cnt),[randx,randy,randwid,randwid])
        cnt += 5
    if  cnt >= 250:
        pygame.draw.rect(screen,red,[randx,randy,randwid,randwid])
        hit(dmg,randx,randy,randwid,randwid)
        cnt += 1
    if cnt == 255:
        pygame.draw.rect(screen,black,[170,260,300,300])
        cnt = 0
    pcl()
def __init__(): 
    global screen
    pygame.init()
    pygame.display.set_caption("Battle")
    screen = pygame.display.set_mode((640,640))
    pygame.draw.rect(screen,white,[160,250,320,320])
    pygame.draw.rect(screen,black,[170,260,300,300])
    pygame.draw.rect(screen,red,[170,590,200,30])
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        key = pygame.key.get_pressed()
        move_player(screen,key)
        attack1(20)
        life_management()
        pygame.display.update()
        clock.tick(70)
if __name__ == "__main__":
    __init__()
    main()