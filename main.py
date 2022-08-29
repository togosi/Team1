def und(life,maxhp,enemylife,pwr,spd,Lock_on,a1,a2,a2_rev,a3):
    global px,py,white,black,red,cnt_atk1,cnt_atk3,inv,myhp,e_maxhp,enemyhp,ecnt,mysize,y1,y2,rx,ry
    import pygame
    import sys
    import random
    #maxhp = life
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
    cnt_atk1 = 0
    ecnt = 0
    y1 = 50
    y2 = 640
    cnt_atk3 = 0
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
            if py > 560 - mysize:
                py = 560 - mysize
        if key[pygame.K_LEFT] == 1:
            px = px - 5
            if px < 170:
                px = 170
        if key[pygame.K_RIGHT] == 1:
            px = px + 5
            if px > 470 - mysize:
                px = 470 - mysize
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
        global cnt_atk1,randwid,randy,randx,randhei
        if cnt_atk1 == 0:
            randwid = random.randint(r1,r2)
            randhei = random.randint(r1,r2)
            randy = random.randint(260,560-randhei) 
            randx = random.randint(170,470-randwid)
        if cnt_atk1 < 250:
            pygame.draw.rect(screen,(cnt_atk1,cnt_atk1,cnt_atk1),[randx,randy,randwid,randhei])
            cnt_atk1 += 5
        if  cnt_atk1 >= 250:
            pygame.draw.rect(screen,red,[randx,randy,randwid,randhei])
            hit(dmg,randx,randy,randwid,randhei)
            cnt_atk1 += 1
        if cnt_atk1 == 255:
            pygame.draw.rect(screen,black,[170,260,300,300])
            cnt_atk1 = 0
        pcl()
    def atk2(dmg,spd,Lock_on):
        global y1,x1,x2
        if y1 == 50:
            randx1 = random.randint(170,450)
            if Lock_on == True:
                x1 = px
                x2 = py
            if Lock_on == False:
                x1 = randx1
                x2 = randx1 +80
        if y1 < 540-spd:
            pygame.draw.rect(screen,white,[x1,y1,20,100])
            pygame.draw.rect(screen,white,[y1-80,x2,100,20])
            pygame.draw.rect(screen,black,[x1,y1-spd,20,spd])
            pygame.draw.rect(screen,black,[y1-80-spd,x2,spd,20])
            pygame.draw.rect(screen,white,[160,250,320,10])
            pygame.draw.rect(screen,white,[160,250,10,320])
            pygame.draw.rect(screen,white,[470,250,10,320])
            pygame.draw.rect(screen,white,[160,560,320,10])
            y1 += spd
            pcl()
        if y1 >= 540-spd:
            pygame.draw.rect(screen,black,[x1,y1-spd,20,100])
            pygame.draw.rect(screen,black,[y1-80-spd,x2,100,20])
            y1 = 50
            pcl()
        hit(dmg,x1,y1,20,100)
        hit(dmg,y1-80,x2,100,20)
    def atk2_rev(dmg,spd,Lock_on):
        global y2,x3,x4
        if y2 == 640:
            randx2 = random.randint(170,450)
            if Lock_on == True:
                x3 = px
                x4 = py
            if Lock_on == False:
                x3 = randx2
                x4 = randx2 +80
        if y2 > 260-spd:
            pygame.draw.rect(screen,white,[x3,y2,20,100])
            pygame.draw.rect(screen,black,[x3,y2+100-spd,20,spd])
            pygame.draw.rect(screen,white,[y2-80,x4,100,20])
            pygame.draw.rect(screen,black,[y2-80+100+spd,x4,spd,20])
            pygame.draw.rect(screen,white,[160,250,320,10])
            pygame.draw.rect(screen,white,[160,250,10,320])
            pygame.draw.rect(screen,white,[470,250,10,320])
            pygame.draw.rect(screen,white,[160,560,320,10])
            y2 -= spd
            pcl()
        if y2 <= 260:
            pygame.draw.rect(screen,black,[x3,y2,20,100])
            pygame.draw.rect(screen,black,[y2-80+spd,x4,100+spd,20])
            y2 = 640
        hit(dmg,x3,y2,20,100)
        hit(dmg,y2-80,x4,100,20)
    def atk3(dmg,spd):
        global rx,ry,cnt_atk3,px,py
        if cnt_atk3 == 0:
            rx = random.randint(160,470)
            ry = random.randint(260,560)
        if px > rx:
            px -= int(spd/2)
        if px < rx:
            px += int(spd/2)
        if py > ry:
            py -= int(spd/2)
        if py < ry:
            py += int(spd/2)
        size = 50 + cnt_atk3*spd/2
        pygame.draw.rect(screen,black,[px-spd,py-spd,mysize+spd,spd])
        pygame.draw.rect(screen,black,[px-spd,py-spd,spd,mysize+spd])
        pygame.draw.rect(screen,black,[px+mysize,py-spd,spd,mysize+spd*2])
        pygame.draw.rect(screen,black,[px-spd,py+mysize,mysize+spd,spd])
        pygame.draw.rect(screen,white,[160,250,320,10])
        pygame.draw.rect(screen,white,[160,250,10,320])
        pygame.draw.rect(screen,white,[470,250,10,320])
        pygame.draw.rect(screen,white,[160,560,320,10])
        pygame.draw.rect(screen,white,[int(rx-size/2),int(ry-size/2),int(size),int(size)])
        pcl()
        hit(dmg,int(rx-size/2),int(ry-size/2),int(size),int(size))
        cnt_atk3 += 1
        if size >= 150:
            pygame.draw.rect(screen,black,[int(rx-size/2),int(ry-size/2),int(size),int(size)])
            cnt_atk3 = 0
    def atkmanager(Lock_on,a1,a2,a2_rev,a3):
        if a1 == "T":
            atk1(pwr,50,200)
        if a2 == "T":
            if Lock_on == "T":
                atk2(pwr,spd,True)
            if Lock_on == "F":
                atk2(pwr,spd,False)
        if a2_rev == "T":
            if Lock_on == "T":
                atk2_rev(pwr,spd,True)
            if Lock_on == "F":
                atk2_rev(pwr,spd,False)
        if a3 == "T":
            atk3(pwr,spd)
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
    def main(Lock_on,a1,a2,a2_rev,a3):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            key = pygame.key.get_pressed()
            move_player(screen,key)
            atkmanager(Lock_on,a1,a2,a2_rev,a3)
            life_management()
            enemylife_management()
            pygame.display.update()
            clock.tick(50)
            if myhp <= 0 or enemyhp == 0:
                break
    __init__()
    main(Lock_on,a1,a2,a2_rev,a3)
    pygame.quit()
    return(myhp)
if __name__ == "__main__":
    print(und(100,100,20,10,5,"F","F","F","F","T"))