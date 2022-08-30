#kobaが改造した、"main6k1.py"をランダムエンカウントで呼び出すファイルです。

#pygameに置き換える

# def und(life,maxhp,enemylife,pwr,spd,Lock_on,a1,a2,a2_rev,a3):

import pygame
import sys


#global key
pl_x = 1
pl_y = 28
imgWall = pygame.image.load("superki.png")
imgFloor = pygame.image.load("kusa.png")
imgWarp = pygame.image.load("worp.png")
imgPlayer = pygame.image.load("maetati.png")

ha = pygame.image.load("ha.png")
# hidaritati = pygame.image.load("hidaritati.png")
# maetati = pygame.image.load("maetati.png")
# migitati = pygame.image.load("migitati.png")
# usirotati = pygame.image.load("usirotati.png")
wareyuka = pygame.image.load("wareyuka.png")
yuka = pygame.image.load("yuka.png")

import random
import main6k1

idx = 0
tmr = 0


def meiq():
    # import tkinter
    # tk = tkinter
    global pl_x,pl_y,maxhitpoint,imgWall,imgFloor,imgWarp,imgPlayer,idx



    

    # key = ""
    # def key_down(e):
    #     global key
    #     key = e.keysym
    # def key_up(e):
    #     global key
    #     key = ""


    def irirkougeki():
        global hp,maxhitpoint,idx,tmr
        at = random.randint(1,50)
        if 1 <= at <= 3:
            pygame.mixer.music.load("遭遇音.mp3")
            pygame.mixer.music.play(1)
            if tmr == 1:
                pygame.mixer.music.load("8-bit_Aggressive1.mp3")
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(-1)
            if at == 1:
                
                idx = 2
                pygame.time.delay(1000)
                hp = main6k1.und(hp,maxhitpoint,10,10,5,"T","F","T","T","F","F")#十字攻撃
                idx= 1
                
            elif at == 2:
                
                idx = 2
                pygame.time.delay(1000)
                hp = main6k1.und(hp,maxhitpoint,10,10,5,"T","F","F","F","T","F")#引き寄せ
                idx= 1

            elif at ==3 :
                
                idx = 2
                pygame.time.delay(1000)
                hp = main6k1.und(hp,maxhitpoint,10,10,15,"T","F","F","F","F","T")#上からビーム
                idx= 1
            tmr = 0





    #mx = 1
    #my = 28

    # def main_proc():
    #     global mx, my, hp

    #     if key == "Up" and maze[my-1][mx] != 1:
    #         my = my - 1
    #         irirkougeki()

    #     if key == "Down" and maze[my+1][mx] != 1:
    #         my = my + 1
    #         irirkougeki()
           
    #     if key == "Left" and maze[my][mx-1] != 1:
    #         mx = mx - 1
    #         irirkougeki()
            
    #     if key == "Right" and maze[my][mx+1] != 1:
    #         mx = mx + 1
    #         irirkougeki()
            
    #     canvas.coords("MYCHR", mx*20+10, my*20+10)
    #     #if maze[my][mx]==2:
    #         #マップ2に行く関数オナシャス
    #     root.after(100, main_proc)

    def move_player(key):
        global pl_x, pl_y, idx,imgPlayer
        
        if key[pygame.K_UP] == 1 and idx == 1:
            if maze[pl_y-1][pl_x] != 1: pl_y = pl_y - 1
            imgPlayer = pygame.image.load("usirotati.png")
            irirkougeki()
        if key[pygame.K_DOWN] == 1 and idx == 1:
            if maze[pl_y+1][pl_x] != 1: pl_y = pl_y + 1
            imgPlayer = pygame.image.load("maetati.png")
            irirkougeki()
        if key[pygame.K_LEFT] == 1 and idx == 1:
            if maze[pl_y][pl_x-1] != 1: pl_x = pl_x - 1
            imgPlayer = pygame.image.load("hidaritati.png")
            irirkougeki()
        if key[pygame.K_RIGHT] == 1 and idx == 1:
            if maze[pl_y][pl_x+1] != 1: pl_x = pl_x + 1
            imgPlayer = pygame.image.load("migitati.png")
            irirkougeki()

    def draw_dungeon(bg):
        global imgWall,imgFloor,imgWarp,imgPlayer,pl_x,pl_y
        for y in range (30):
            for x in range(30):
                if maze[y][x] == 1:
                    bg.blit(imgWall, [x*20+10, y*20+10])
                elif maze[y][x] == 0:
                    bg.blit(imgFloor, [x*20+10, y*20+10])
                if maze[y][x] == 2:
                    bg.blit(imgFloor, [x*20+10, y*20+10])
                    bg.blit(imgWarp, [x*20+10, y*20+10])
                if x == pl_x and y == pl_y: # 主人公の表示
                    bg.blit(imgPlayer, [x*20+10, y*20+10])


    def main():
        global key,idx,tmr,hp,maxhitpoint
        pygame.init()
        pygame.display.set_caption("map1k2")
        screen = pygame.display.set_mode((640, 640))
        maze_clock = pygame.time.Clock()

        #make_dungeon()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            tmr = tmr + 1
            key = pygame.key.get_pressed()

            if idx == 0:
                if tmr == 1:
                    pygame.mixer.music.load("8-bit_Aggressive1.mp3")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)
                screen.fill((0,0,0))
                font = pygame.font.Font(None,80)
                txt = font.render("Press space key",True,(255,255,255))
                screen.blit(txt,[100,400])
                imgtitle = pygame.image.load("convenience.png").convert()
                imgtitle = pygame.transform.scale(imgtitle, (1280/2, 720/2)) 
                colorkey = imgtitle.get_at((0,0))
                #colorkey = (255, 255, 255)
                imgtitle.set_colorkey(colorkey, pygame.RLEACCEL)
                screen.blit(imgtitle, (0,10))
                pygame.display.update()

                if key[pygame.K_SPACE] == 1:
                    hp=200
                    maxhitpoint = 200
                    idx = 1
                    tmr = 0

            elif idx == 1:
                if tmr == 1:
                    pygame.mixer.music.load("魔法使いと振り子時計_2.mp3")
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play(-1)
                move_player(key)
                draw_dungeon(screen)
                pygame.display.update()
                maze_clock.tick(10)


                



    #root = tk.Tk()
    #root.title("map1")
    # root.bind("<KeyPress>", key_down)
    # root.bind("<KeyRelease>", key_up)
    # canvas = tk.Canvas(width=880, height=600, bg="white")
    # canvas.pack()

    maze = [
        [1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1,],#５ｘ５単位にすることで見やすくしているつもり
        [1,0,0,0,0, 1,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,2,1,],
        [1,0,0,1,0, 1,1,1,0,0, 0,1,1,1,1, 1,0,0,0,0, 0,0,0,1,0, 1,1,1,0,1,],
        [1,0,1,0,0, 0,0,1,0,1, 0,1,0,0,0, 1,1,1,1,1, 1,1,1,1,0, 1,0,0,0,1,],
        [1,1,0,0,0, 0,0,1,0,1, 0,1,1,1,0, 1,0,0,0,0, 0,0,0,0,0, 1,0,1,0,1,],#4

        [1,0,1,0,1, 0,0,1,0,1, 0,0,0,0,1, 1,0,1,1,1, 1,1,1,1,1, 1,0,1,0,1,],
        [1,0,1,0,1, 0,0,1,0,1, 1,1,1,1,1, 0,0,1,0,0, 0,0,0,0,0, 0,0,1,0,1,],
        [1,0,1,0,1, 0,0,1,0,0, 0,0,0,0,1, 0,1,1,0,0, 0,0,0,1,1, 1,1,1,0,1,],
        [1,0,1,0,1, 0,0,0,1,0, 1,1,1,0,1, 0,1,1,1,1, 1,1,0,1,0, 0,0,0,0,1,],
        [1,0,1,1,1, 1,0,0,0,1, 0,0,0,0,1, 0,0,0,0,0, 0,1,0,1,1, 0,0,0,0,1,],#9

        [1,0,1,0,0, 0,0,0,0,1, 0,1,1,1,1, 1,1,1,1,1, 0,1,0,1,1, 1,1,0,0,1,],
        [1,0,1,0,0, 0,0,0,0,1, 0,1,0,1,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,1,0,1,],
        [1,0,1,0,1, 0,0,0,0,1, 0,1,0,1,0, 0,1,1,1,1, 1,1,1,1,0, 1,0,1,0,1,],
        [1,0,1,0,1, 1,1,1,0,1, 0,0,0,1,0, 0,1,0,0,0, 0,0,0,0,0, 1,0,1,0,1,],
        [1,1,1,0,0, 0,0,0,0,1, 1,1,0,0,0, 0,1,0,1,1, 0,1,1,1,1, 1,0,1,0,1,],#14

        [1,0,0,0,1, 1,1,1,1,0, 0,0,0,1,0, 0,1,0,1,0, 1,0,0,0,0, 1,0,0,1,1,],
        [1,0,1,0,1, 0,0,0,1,1, 1,1,1,1,0, 0,1,0,1,0, 0,1,0,0,0, 1,0,1,0,1,],
        [1,0,1,0,1, 0,1,0,1,0, 0,0,0,0,0, 0,1,0,0,1, 0,1,0,0,0, 1,0,1,0,1,],
        [1,0,0,0,1, 0,1,0,1,0, 1,1,1,1,1, 1,0,0,1,0, 0,1,0,0,0, 0,0,1,0,1,],
        [1,0,1,0,1, 0,1,0,1,0, 1,0,0,0,0, 0,0,1,1,0, 0,1,1,1,1, 1,0,1,0,1,],#19

        [1,0,1,0,1, 1,1,0,1,0, 1,0,0,0,0, 0,0,0,1,0, 0,0,0,0,0, 0,0,1,0,1,],
        [1,1,1,0,0, 0,1,0,1,0, 1,1,1,1,1, 0,0,0,1,0, 0,1,1,1,0, 0,0,1,0,1,],
        [1,0,0,0,1, 0,0,0,0,0, 0,0,0,0,0, 1,0,1,0,0, 1,0,0,0,1, 0,0,0,1,1,],
        [1,0,1,1,1, 0,1,0,1,1, 1,1,1,0,0, 1,0,1,1,1, 0,0,1,1,1, 0,0,0,0,1,],
        [1,0,1,0,0, 0,1,0,1,0, 0,0,0,0,0, 1,0,0,0,0, 0,1,0,0,0, 0,0,1,0,1,],#24

        [1,0,1,1,1, 1,1,0,1,0, 1,1,1,1,1, 1,1,1,1,1, 1,0,0,1,1, 0,0,1,0,1,],
        [1,0,1,0,0, 0,0,0,1,0, 1,0,0,0,0, 0,0,0,0,0, 0,0,1,0,0, 1,0,0,0,1,],
        [1,0,1,1,1, 1,1,1,1,0, 1,0,1,1,1, 1,1,1,0,1, 1,1,0,0,0, 0,1,1,0,1,],
        [1,0,0,0,0, 0,0,0,0,0, 0,0,1,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,1,],
        [1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1,],#29
        ]                               #14                              #29

    # tree = tk.PhotoImage(file="superki.png")
    # kusa = tk.PhotoImage(file="kusa.png")
    # worp = tk.PhotoImage(file="worp.png")
    # for y in range (30):
    #     for x in range(30):
    #         if maze[y][x] == 1:
    #             canvas.create_image(x*20+10, y*20+10, image=tree)
    #         elif maze[y][x] == 0:
    #             canvas.create_image(x*20+10, y*20+10, image=kusa)
    #         elif maze[y][x] == 2:
    #             canvas.create_image(x*20+10, y*20+10, image=worp)

    #maetati = tkinter.PhotoImage(file="maetati.png")#前向きの↓プレイヤ－の画像をpngで入れてくれ
    #canvas.create_image((mx+1)*20+10, my*20+10, image=maetati, tag="MYCHR")
    main()
    #main_proc()
    #root.mainloop()

if __name__ == "__main__":
    meiq()
