def und(life,enemylife):
    global px,py,white,black,red,cnt,y,inv,myhp,maxhp,maxhp,e_maxhp,enemyhp,ecnt,mysize
    import pygame
    import sys
    import random
    maxhp = life
    myhp = life
    e_maxhp = enemylife
    enemyhp = enemylife
    px = 315
    py = 410
    mysize = 20
    white = (255,255,255)
    black = (0,0,0)
    red = (200,0,0)
    inv = 0
    cnt = 0
    ecnt = 0
    y = 50
    def hit(dmg,x1,y1,width,height):
        global inv ,myhp
        ms = int(mysize/2)
        xs = int(width/2 + ms)
        ys = int(height/2 + ms)
        lex = abs(x1 + width/2 - px - ms)
        ley = abs(y1 + height/2 - py - ms)
        if lex < xs and ley < ys and inv == 0:
            myhp -= dmg
            inv = 50
    def pcl():
        if inv > 0:
            pygame.draw.rect(screen,(0,255,0),[px,py,mysize,mysize])
        if inv == 0:
            pygame.draw.rect(screen,(0,255,255),[px,py,mysize,mysize])
    def move_player(screen,key):
        global px,py
        pygame.draw.rect(screen,black,[px,py,mysize,mysize])
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
        global inv
        if inv > 0:
            inv -= 1
        pygame.draw.rect(screen,red,[170,590,200,30])
        pygame.draw.rect(screen,(180,0,180),[171+int(myhp/maxhp*200),590,int((1-myhp/maxhp)*200),30])
        txt = "HP:" + str(myhp) + "/" + str(maxhp)
        font = pygame.font.Font(None,25)
        pygame.draw.rect(screen,black,[390,590,100,30])
        screen.blit(font.render(txt,True,white),[390,590])
    def enemylife_management():
        global enemyhp,ecnt
        pygame.draw.rect(screen,(150,150,0),[500,100,50,470])
        pygame.draw.rect(screen,(64,0,64),[500,100,50,(1-enemyhp/e_maxhp)*470])
        txt1 = "EnemyHP:"
        txt2 = str(enemyhp) + "/" + str(e_maxhp)
        font = pygame.font.Font(None,25)
        pygame.draw.rect(screen,black,[500,0,140,100])
        screen.blit(font.render(txt1,True,white),[500,40])
        screen.blit(font.render(txt2,True,white),[500,60])
        ecnt += 1
        if ecnt == 50:
            enemyhp -= 1
            ecnt = 0
    def atk1(dmg,r1,r2):
        global cnt,randwid,randy,randx,randhei
        if cnt == 0:
            randwid = random.randint(r1,r2)
            randhei = random.randint(r1,r2)
            randy = random.randint(260,560-randhei) 
            randx = random.randint(170,470-randwid)
        if cnt < 250:
            pygame.draw.rect(screen,(cnt,cnt,cnt),[randx,randy,randwid,randhei])
            cnt += 5
        if  cnt >= 250:
            pygame.draw.rect(screen,red,[randx,randy,randwid,randhei])
            hit(dmg,randx,randy,randwid,randhei)
            cnt += 1
        if cnt == 255:
            pygame.draw.rect(screen,black,[170,260,300,300])
            cnt = 0
        pcl()
    def atk2(dmg,spd,Lock_on):
        global y,randx2,x1,x2
        if y == 50:
            randx2 = random.randint(170,450)
            if Lock_on == True:
                x1 = px
                x2 = py
            if Lock_on == False:
                x1 = randx2
                x2 = randx2 +80
        if y < 535:
            pygame.draw.rect(screen,white,[x1,y,20,100])
            pygame.draw.rect(screen,white,[y-80,x2,100,20])
            pygame.draw.rect(screen,black,[x1,y-spd,20,spd])
            pygame.draw.rect(screen,black,[y-80-spd,x2,spd,20])
            pygame.draw.rect(screen,white,[160,250,320,10])
            pygame.draw.rect(screen,white,[160,250,10,320])
            pygame.draw.rect(screen,white,[470,250,10,320])
            pygame.draw.rect(screen,white,[160,560,320,10])
            y += spd
            pcl()
        if y >= 540-spd:
            pygame.draw.rect(screen,black,[x1,y-spd,20,100])
            pygame.draw.rect(screen,black,[y-80-spd,x2,100,20])
            y = 50
            pcl()
        hit(dmg,x1,y,20,100)
        hit(dmg,y-80,x2,100,20)
    def __init__(): 
        global screen
        pygame.init()
        pygame.display.set_caption("Battle")
        screen = pygame.display.set_mode((640,640))
        pygame.draw.rect(screen,white,[160,250,320,320])
        pygame.draw.rect(screen,black,[170,260,300,300])
        pygame.draw.rect(screen,red,[170,590,200,30])
        txt = "HP:" + str(myhp) + "/" + str(maxhp)
        font = pygame.font.Font(None,25)
        screen.blit(font.render(txt,True,white),[390,590])
    def main():
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            key = pygame.key.get_pressed()
            move_player(screen,key)
            atk1(20,10,200)
            atk2(20,5,False)
            life_management()
            enemylife_management()
            pygame.display.update()
            clock.tick(50)
            if myhp <= 0 or enemyhp == 0:
                break
    __init__()
    main()
    return(myhp)
if __name__ == "__main__":
    print(und(50,10))