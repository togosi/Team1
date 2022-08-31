#2面のマップはまだ1面と同じです
#pygameでやってます
#ENDLESSとか言っているがちゃんと目的地はある（多分）

#ファイル名のCSは「Convenience Store」の略。・・・最初から狙っていたわけではない。さっき気づいた。

# def und(life,maxhp,enemylife,pwr,spd,Lock_on,a1,a2,a2_rev,a3):

#残りやることリスト（流石に全部は無理だと思う）
#ゲームクリア処理・ゲームオーバー処理・第2面の迷路の作成・効果音によってBGMが途切れないようにする処理・効果音やBGMの音量調整

#できればほしいもの
#被ダメージ時の効果音、スイッチ押したらマグマの一部が床になるギミック、一筆書きで階段出現ギミック、雨のごとく降ってくる小さな四角または丸の攻撃、図形が回転してくる攻撃（難しそう）
#ギミックでの詰み防止用のリセット機能、体力と現在の面の表示

#原始人よけるの簡単すぎた・・・

import pygame
import sys


pl_x = 1
pl_y = 28
imgWall = pygame.image.load("superki.png")
imgKusa = pygame.image.load("kusa.png")
imgWarp = pygame.image.load("worp.png")
imgPlayer = pygame.image.load("maetati.png")
imgHa = pygame.image.load("ha.png")
imgWareyuka = pygame.image.load("wareyuka.png")
imgYuka = pygame.image.load("yuka.png")
imgMaguma = pygame.image.load("maguma.png")
imgKaidan = pygame.image.load("kaidan.png")

maze_clock = pygame.time.Clock()

import random
import CS_battle2b

idx = 0
tmr = 0


def meiq():
    global pl_x,pl_y,maxhitpoint,imgWall,imgKusa,imgWarp,imgPlayer,idx,field_n
    white = (255,255,255)
    black = (0,0,0)
    #red = (200,0,0)

    def irirkougeki():
        global hp,maxhitpoint,idx,tmr,field_n
        at = random.randint(1,200)
        if 1 <= at <= 3 and hp >= 0:
            #バトル開始画面を作ったのでそこで遭遇音が流れるようにした　追記2bでもういちど元に戻した
            pygame.mixer.music.load("遭遇音.mp3")
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(1)
            atk_screen = pygame.display.get_surface()
            font = pygame.font.Font(None,75)
            txt = "A Monster Appeared!"
            atk_screen.blit(font.render(txt,True,white),[50,300])
            pygame.display.update()

            initcnt = 0
            while True:
                initcnt += 1
                if initcnt >= 50:
                    atk_screen.fill(black)
                    break
                maze_clock.tick(50)

                    #initcntが50以上になるまでスクリーンに文章を表示して待機するようにした


            # if tmr == 1:
            #     pygame.mixer.music.load("8-bit_Aggressive1.mp3")
            #     pygame.mixer.music.set_volume(0.5)
            #     pygame.mixer.music.play(-1)
            if at == 1:
                idx = 8
                #pygame.time.delay(1200)
                pygame.mixer.music.load("Game_Center.mp3")
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(-1)               
                hp = CS_battle2b.und(hp,maxhitpoint,6+field_n*4,6+field_n*4,3+field_n*2,"T","F","T","T","F","F")#十字攻撃
                if hp > 0:
                    idx = field_n
                else:
                    idx = 9
                
            elif at == 2:
                
                idx = 8
                #pygame.time.delay(1200)
                pygame.mixer.music.load("Beans_man.mp3")
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(-1) 
                hp = CS_battle2b.und(hp,maxhitpoint,6+field_n*4,6+field_n*4,5,"T","F","F","F","T","F")#引き寄せ
                if hp > 0:
                    idx = field_n
                else:
                    idx = 9

            elif at ==3 :
                
                idx = 8
                #pygame.time.delay(1200)
                pygame.mixer.music.load("Beans_man.mp3")
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(-1)                 
                hp = CS_battle2b.und(hp,maxhitpoint,10,10,15,"T","F","F","F","F","T")#上からビーム
                if hp > 0:
                    idx = field_n
                else:
                    idx = 9
            tmr = 0

    def move_player(key):
        global pl_x, pl_y, idx,imgPlayer,field_n,tmr
        
        if key[pygame.K_UP] == 1 and idx == field_n:
            if maze[pl_y-1][pl_x] != 1: pl_y = pl_y - 1
            imgPlayer = pygame.image.load("usirotati.png")
            if maze[pl_y][pl_x] == 2:
                pygame.mixer.music.load("ワープやタイムスリップする音.mp3")
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(1)
                # imgPlayer = pygame.image.load("usirotati.png")
                # pygame.display.update()
                # pygame.time.delay(200)
                # imgPlayer = pygame.image.load("migitati.png")
                # pygame.display.update()
                # pygame.time.delay(200)
                # imgPlayer = pygame.image.load("maetati.png")
                # pygame.display.update()
                # pygame.time.delay(200)
                # imgPlayer = pygame.image.load("hidaritati.png")
                # pygame.display.update()
                # pygame.time.delay(200)
                # imgPlayer = pygame.image.load("usirotati.png")
                # pygame.display.update()
                # pygame.time.delay(200)
                # imgPlayer = pygame.image.load("migitati.png")
                # pygame.display.update()
                # pygame.time.delay(200)
                # imgPlayer = pygame.image.load("maetati.png")
                # pygame.display.update()
                # pygame.time.delay(200)
                # imgPlayer = pygame.image.load("hidaritati.png")
                # pygame.display.update()
                #ワープの演出を作ろうとしたけれども失敗。
                pygame.time.delay(1000)

                field_n = field_n+1
                idx = field_n
                tmr=0
                pl_x = 1
                pl_y = 28                    
                #クリアして次の面へ行く処理
                
            elif maze[pl_y][pl_x] != 2:
                irirkougeki()
                #行った先がゴールでなければ、敵とエンカウントするかどうかの試行(irirkougeki)が入る
                #この辺もうちょっときれいにできそうだけどまあ後でいいや


        if key[pygame.K_DOWN] == 1 and idx == field_n:
            if maze[pl_y+1][pl_x] != 1: pl_y = pl_y + 1
            imgPlayer = pygame.image.load("maetati.png")
            if maze[pl_y][pl_x] == 2:
                pygame.mixer.music.load("ワープやタイムスリップする音.mp3")
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(1)
                pygame.time.delay(1000)
                field_n = field_n+1
                idx = field_n
                tmr=0                    
                pl_x = 1
                pl_y = 28  
                #クリアして次の面へ
            elif maze[pl_y][pl_x] != 2:
                irirkougeki()


        if key[pygame.K_LEFT] == 1 and idx == field_n:
            if maze[pl_y][pl_x-1] != 1: pl_x = pl_x - 1
            imgPlayer = pygame.image.load("hidaritati.png")
            if maze[pl_y][pl_x] == 2:
                pygame.mixer.music.load("ワープやタイムスリップする音.mp3")
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(1)
                pygame.time.delay(1000)
                field_n = field_n+1
                idx = field_n
                tmr=0                    
                pl_x = 1
                pl_y = 28  
                #クリアして次の面へ
            elif maze[pl_y][pl_x] != 2:
                irirkougeki()


        if key[pygame.K_RIGHT] == 1 and idx == field_n:
            if maze[pl_y][pl_x+1] != 1: pl_x = pl_x + 1
            imgPlayer = pygame.image.load("migitati.png")
            if maze[pl_y][pl_x] == 2:
                pygame.mixer.music.load("ワープやタイムスリップする音.mp3")
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(1)
                pygame.time.delay(1000)
                field_n = field_n+1
                idx = field_n
                tmr=0                    
                pl_x = 1
                pl_y = 28  
                #クリアして次の面へ
            elif maze[pl_y][pl_x] != 2:
                irirkougeki()


    def draw_dungeon(bg):
        global imgWall,imgKusa,imgWarp,imgPlayer,pl_x,pl_y,field_n,imgMaguma,imgKaidan
        for y in range (30):
            for x in range(30):
                if maze[y][x] == 1:#壁またはマグマの表示
                    if field_n ==1:
                        bg.blit(imgWall, [x*20+10, y*20+10])
                    elif field_n == 2:
                        bg.blit(imgMaguma, [x*20+10, y*20+10])
                elif maze[y][x] == 0:#草または床の表示　2面を割れ床によって後戻り不可な仕様にするだけでも難易度は上がりそう
                    if field_n ==1:
                        bg.blit(imgKusa, [x*20+10, y*20+10])
                    elif field_n == 2:
                        bg.blit(imgYuka, [x*20+10, y*20+10])
                if maze[y][x] == 2:#各面のゴール地点
                    if field_n ==1:
                        bg.blit(imgKusa, [x*20+10, y*20+10])
                        bg.blit(imgWarp, [x*20+10, y*20+10])
                    elif field_n == 2:
                        bg.blit(imgYuka, [x*20+10, y*20+10])
                        bg.blit(imgKaidan, [x*20+10, y*20+10])
                if x == pl_x and y == pl_y: # 主人公の表示
                    bg.blit(imgPlayer, [x*20+10, y*20+10])


    def main():
        global key,idx,tmr,hp,maxhitpoint,field_n
        pygame.init()
        pygame.display.set_caption("THE ENDLESS JOURNEY TO THE CONVENIENCE STORE")
        screen = pygame.display.set_mode((640, 640))
        

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            tmr = tmr + 1
            key = pygame.key.get_pressed()

            if idx == 0:
                if tmr == 1: #最初の一回目のみBGMを流す
                    pygame.mixer.music.load("8-bit_Aggressive1.mp3")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)
                screen.fill((0,0,0))
                font = pygame.font.Font(None,80)
                txt = font.render("Press space key",True,(255,255,255))
                screen.blit(txt,[100,400])
                font = pygame.font.Font(None,25)
                txt = font.render("made by CS:python-team1",True,(255,255,255))
                screen.blit(txt,[400,600])
                imgcon = pygame.image.load("画像1.png").convert()
                imgcon = pygame.transform.scale(imgcon, (1280/2, 720/2)) 
                colorkey_con = imgcon.get_at((0,0))
                imgcon.set_colorkey(colorkey_con, pygame.RLEACCEL)
                screen.blit(imgcon, (0,10))
                imgtitle = pygame.image.load("convenience.png").convert()
                imgtitle = pygame.transform.scale(imgtitle, (1280/2, 720/2)) 
                colorkey = imgtitle.get_at((0,0))
                #colorkey = (255, 255, 255)でも入力できる模様
                imgtitle.set_colorkey(colorkey, pygame.RLEACCEL)
                screen.blit(imgtitle, (0,10))
                pygame.display.update()

                if key[pygame.K_SPACE] == 1:
                    maxhitpoint = 20
                    hp=maxhitpoint
                    idx = 1
                    tmr = 0
                    field_n = idx

            elif idx == 1:
                if tmr == 1:
                    pygame.mixer.music.load("魔法使いと振り子時計_2.mp3")
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play(-1)
                move_player(key)
                draw_dungeon(screen)
                pygame.display.update()
                maze_clock.tick(10)

            elif idx == 2:
                if tmr == 1:
                    pygame.mixer.music.load("不吉な森.mp3")
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play(-1)
                move_player(key)
                draw_dungeon(screen)
                pygame.display.update()
                maze_clock.tick(10)

            elif idx == 9:
                if tmr == 1:
                    pygame.mixer.music.load("8bit_Game_Menu.mp3")
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play(-1)
                screen.fill(black)
                font = pygame.font.Font(None,70)
                txt = "You couldn't reach"
                screen.blit(font.render(txt,True,(128,0,128)),[80,200])
                txt = "the convenience store..."
                screen.blit(font.render(txt,True,(128,0,128)),[80,250])
                pygame.display.update()
                #maze_clock.tick(10)
                pygame.time.delay(3000)
                pygame.quit()
                sys.exit()

    maze = [
        [1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1,],#５ｘ５単位にすることで見やすくしているつもり
        [1,0,0,0,0, 1,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,2,1,],
        [1,0,0,1,0, 1,1,1,0,0, 0,1,1,1,1, 1,0,0,0,0, 0,0,0,1,0, 1,1,1,0,1,],
        [1,0,1,0,0, 0,0,1,0,1, 0,1,0,0,0, 1,1,1,1,1, 1,1,1,1,0, 1,0,0,0,1,],
        [1,1,0,0,0, 0,0,1,0,1, 0,1,1,1,0, 0,1,0,0,0, 0,0,0,0,0, 1,0,1,0,1,],#4

        [1,0,1,0,1, 0,0,1,0,1, 0,0,0,0,1, 1,0,1,1,1, 1,1,1,1,1, 1,0,1,0,1,],
        [1,0,1,0,1, 0,0,1,0,1, 1,1,1,1,1, 0,0,1,0,0, 0,0,0,0,0, 0,0,1,0,1,],
        [1,0,1,0,1, 0,0,1,0,0, 0,0,0,0,1, 0,1,1,0,0, 0,0,1,1,1, 1,1,1,0,1,],
        [1,0,1,0,1, 0,0,0,1,0, 1,1,1,0,1, 0,1,1,1,1, 1,1,0,1,0, 0,0,0,0,1,],
        [1,0,1,1,1, 1,0,0,0,1, 0,0,0,0,1, 0,0,0,0,0, 0,1,0,1,1, 0,0,0,0,1,],#9

        [1,0,1,0,0, 0,0,0,0,1, 0,1,1,1,1, 1,1,1,1,1, 0,1,0,1,1, 1,1,0,0,1,],
        [1,0,1,0,0, 0,0,0,0,1, 0,1,0,1,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,1,0,1,],
        [1,0,0,1,1, 0,0,0,0,1, 0,1,0,1,0, 0,1,1,1,1, 1,1,1,1,0, 1,0,1,0,1,],
        [1,0,0,0,1, 1,1,0,0,1, 0,0,0,1,0, 0,1,0,0,0, 0,0,0,0,0, 1,0,1,0,1,],
        [1,1,1,0,0, 0,0,1,0,1, 1,1,0,0,0, 0,1,0,1,1, 0,1,1,1,1, 1,0,1,0,1,],#14

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
        #mazeは余裕があれば引数として関数に入れられるようにしたい

    main()

if __name__ == "__main__":
    meiq()











'''もとの迷路

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

        '''