import pygame
import sys
import numpy as np
import time
import random
import tkinter as tk


# 画像ファイルの読み込み:[背景,実機,弾,敵]
img=[pygame.image.load("image0.png"),pygame.image.load("shimada.png"),pygame.image.load("SmallShot__.png"),pygame.image.load("reimu.png"),pygame.image.load("black.png"),pygame.image.load("ButterflyShot.png")]

RED = (255,0,0)

bg_x = 0
px = 1400 #プレイヤーのX座標
py = 630 #プレイヤーのY座標
bx = 0 #弾のX座標
by = 0 #弾のY座標
ex = 400#敵のX座標
ey = 630
flag=0
trigger=0

space = 0
p_BULLET_MAX = 100 #弾の最大値
p_bull_n = 0
p_bull_x =[0]*p_BULLET_MAX
p_bull_y =[0]*p_BULLET_MAX
p_bull_f =[False]*p_BULLET_MAX

BULLET_MAX = 500 #弾の最大値
bull_n = 0
bull_x =[0]*BULLET_MAX
bull_y =[0]*BULLET_MAX
bull_f =[False]*BULLET_MAX

clock = pygame.time.Clock()

class Danmaku:
    def set_bullet():#弾のスタンバイ
        global bull_n
        bull_f[bull_n] = True
        bull_x[bull_n] = ex-50
        bull_y[bull_n] = ey+20
        bull_n = (bull_n+1)%BULLET_MAX

    def move_bullet(screen):#弾を飛ばす
        global tmr,turn,trigger
        variant=tmr%450
        if variant==0:
            turn+=1
        for i in range(BULLET_MAX):
            if bull_f[i] == True:
                    bull_y[i] = bull_y[i] -palameterY(turn,i,3)
                    bull_x[i] = bull_x[i] -palameterX(turn,i,3)
                    screen.blit(img[2],[bull_x[i],bull_y[i]])
                
                    if bull_y[i] < 0 or bull_x[i]<0 or bull_y[i]>1000 or bull_x[i]>1480:
                        bull_f[i] = False
            # print(distance(px,bull_x[i],py,bull_y[i]))
            if distance(px,bull_x[i],py,bull_y[i])<0.05:
                trigger=2
                se.play(0)
                return trigger

        if turn==2700:
            turn=0

        

class Player:
    def set_bullet():#弾のスタンバイ
        global p_bull_n
        p_bull_f[p_bull_n] = True
        p_bull_x[p_bull_n] = px-50
        p_bull_y[p_bull_n] = py+20
        p_bull_n = (p_bull_n+1)%p_BULLET_MAX

    def move_bullet(screen):#弾を飛ばす

        for i in range(p_BULLET_MAX):
            if p_bull_f[i] == True:
                    p_bull_y[i] = p_bull_y[i] -np.sin(10*i)
                    p_bull_x[i] = p_bull_x[i] -10
                    screen.blit(img[2],[p_bull_x[i],p_bull_y[i]])
                
                    if p_bull_y[i] < 0:
                        p_bull_f[i] = False

def move_player(screen,key):
    global px,py,space,varidity

    a=1
    if key[pygame.K_LSHIFT] ==1 or key[pygame.K_RSHIFT] ==1:
        a=1/2

    if key[pygame.K_UP] == 1:
        py = py - 10*a
        if py < 20:
            py = 20
    if key[pygame.K_DOWN] == 1:
        py = py + 10*a
        if py > 1204:
            py = 1204
    if key[pygame.K_LEFT] == 1:
        px = px - 10*a
        if px < 20:
            px = 20
    if key[pygame.K_RIGHT] == 1:
        px = px + 10*a
        if px > 1480:
            px = 1480
            
    if key[pygame.K_p] == 1:
        if pygame.mixer.music.get_busy() == False:
                    pygame.mixer.music.play(-1)
        if pygame.mixer.music.get_busy() == True:
                    pygame.mixer.music.stop()

    if key[pygame.K_ESCAPE] == 1:
        sys.exit()
    

    space = (space+1)*key[pygame.K_SPACE]
    varidity=random.randint(0,5)
    if space%5 == 1: #5フレーム毎に弾を飛ばす
        Player.set_bullet()
    Danmaku.set_bullet()

    screen.blit(img[1],[px-100,py])
    screen.blit(img[5],[px-20,py+20])

def move_enemy(screen):
    global ex,ey,space

    probability=random.randint(1,1000)
    if probability<=400:
        ey = ey - 10
        if ey < 80:
            ey = 80
    if 400<probability<=800:
        ey = ey + 10
        if ey > 1204:
            ey = 1204

    screen.blit(img[3],[ex-40,ey-40])



# パラメーター軌道を格納 i:変数 a,b:初期位相
def palameterX(x,i,a):
    pala_x=[0,20*np.cos(a*i/10),30*(np.cos(i))**3,10*(1+np.cos(2*i))*np.cos(i),10*np.cos(a*i/10),30*np.sqrt(2)*np.sqrt(np.cos(2*i))*np.cos(i),(np.sin(a*i+7))]
    return pala_x[x]
def palameterY(y,i,b):
    pala_y=[0,20*np.sin(b*i/10),30*(np.sin(i))**3,10*(1+np.cos(2*i))*np.sin(i),10*np.sin(b*i/8),30*np.sqrt(2)*np.sqrt(np.cos(2*i))*np.sin(i),(np.sin(b*i))] 
    return pala_y[y]


def distance(px,bx,py,by):
    return(np.abs((px-20-bx)*2+(py+20-by)*2))

def draw_text(screen,x,y,text,size,col):#文字表示の関数
    font = pygame.font.Font(None,size)
    s = font.render(text,True,col)
    x = x - s.get_width()/2
    y = y - s.get_height()/2
    screen.blit(s,[x,y])

def main():

        global bg_x,screen,tmr,turn,trigger,px,py,bx,by,ex,ey,se,p_BULLET_MAX,p_bull_n,p_bull_x ,p_bull_y ,p_bull_f
        BULLET_MAX = 500 #弾の最大値
        bull_n = 0
        bull_x =[0]*BULLET_MAX
        bull_y =[0]*BULLET_MAX
        bull_f =[False]*BULLET_MAX
        px = 1400 #プレイヤーのX座標
        py = 630 #プレイヤーのY座標
        bx = 0 #弾のX座標
        by = 0 #弾のY座標
        ex = 400
        ey = 630
        tmr=0
        turn=0

        p_BULLET_MAX = 100 #弾の最大値
        p_bull_n = 0
        p_bull_x =[0]*p_BULLET_MAX
        p_bull_y =[0]*p_BULLET_MAX
        p_bull_f =[False]*p_BULLET_MAX

        BULLET_MAX = 500 #弾の最大値
        bull_n = 0
        bull_x =[0]*BULLET_MAX
        bull_y =[0]*BULLET_MAX
        bull_f =[False]*BULLET_MAX

        while True:
            pygame.init()
            pygame.display.set_caption("シューティングゲーム")
            screen = pygame.display.set_mode((1480,1365))

            try:
                pygame.mixer.init(frequency = 44100)    # 初期設定
                pygame.mixer.music.load("toho_a.ogg")
                se = pygame.mixer.Sound("picuun.ogg")
            except:
                print("oggファイルが見当たらないか、オーディオ機器が接続されていません")

            if trigger==1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()


                bg_x = (bg_x+16)%1480 
                screen.blit(img[0],[bg_x-1480,0])
                screen.blit(img[0],[bg_x,0])

                key = pygame.key.get_pressed()
                move_player(screen,key)
                move_enemy(screen)
                Player.move_bullet(screen)
                Danmaku.move_bullet(screen)
                tmr+=1

                pygame.display.update()
                clock.tick(30)

            if trigger ==2:
                screen.fill((0,0,0))
                draw_text(screen,740,500,"GAMEOVER",100,RED)
                draw_text(screen,740,800,"SCORE:"+str(tmr),100,(255,255,255))
                draw_text(screen,740,1000,"SPACE:RESTART",100,(255,255,255))
                draw_text(screen,740,1100,"ESC:EXIT",100,(255,255,255))
                pygame.display.update()
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE] == 1:
                    trigger=1
                    main()
                elif key[pygame.K_ESCAPE] == 1:
                    sys.exit()
                    root=0


   

def title1_clickbutton():
    global titleLb
    titleCv.delete(draft_title)



    titleLb=[tk.Label(root,text="SPACEで弾を発射",font=("ロダン Pro EB",25),fg="black",compound="bottom"),
             tk.Label(root,text="↑↓←→で移動",font=("ロダン Pro EB",25),fg="black",compound="bottom")
            ,tk.Label(root,text="SHIFTを押して低速移動",font=("ロダン Pro EB",25),fg="black",compound="bottom")
            ,tk.Label(root,text="できるだけ長く弾幕から逃げ続けよう！",font=("ロダン Pro EB",25),fg="black",compound="bottom")]


    for i in range(len(titleLb)):
        titleLb[i].place(relx=0.01,rely=0.15*i)

        root.after(4000,title2_clickbutton)

def title2_clickbutton():
    global trigger
    trigger=1
    titleCv.delete("all")
    for i in range(len(titleLb)):
        titleLb[i].destroy()
    start_button.place_forget()
    root.destroy()
    if __name__ == "__main__":
        main()


def title():
    global root
    global titleCv
    global start_button,draft_title

    

    titleCv = tk.Canvas(root,width=640,height=800,bg="white")
    titleCv.pack()
    start_button = tk.Button(root,text="Click to start",font=("ロダン Pro EB",30),fg="black",command=title1_clickbutton,compound="bottom")
    start_button.place(x=196,y=650)    
    
    title_bg = tk.PhotoImage(file="title_bg.png")
    titleCv.create_image(322,402,image=title_bg)
    draft_title = tk.PhotoImage(file="5000choyen_1.png")
    titleCv.create_image(360,250,image=draft_title)

    root.mainloop()

root = tk.Tk()
root.resizable(False,False)
title()




    
