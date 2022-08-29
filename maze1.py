def maze():
    global mx,my,root
    import tkinter
    tk = tkinter

    key = ""
    def key_down(e):
        global key
        key = e.keysym
    def key_up(e):
        global key
        key = ""

    mx = 1
    my = 28

    def main_proc():
        global mx, my
        if key == "Up" and maze[my-1][mx] != 1:
            my = my - 1
        if key == "Down" and maze[my+1][mx] != 1:
            my = my + 1
        if key == "Left" and maze[my][mx-1] != 1:
            mx = mx - 1
        if key == "Right" and maze[my][mx+1] != 1:
            mx = mx + 1
        canvas.coords("MYCHR", mx*20+10, my*20+10)
        if maze[my][mx]==2:
            #マップ2に行く関数オナシャス
            print("a")
        root.after(100, main_proc)

    root = tk.Tk()
    root.title("map1")
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    canvas = tk.Canvas(width=880, height=600, bg="white")
    canvas.pack()

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

    tree = tk.PhotoImage(file="superki.png")
    kusa = tk.PhotoImage(file="kusa.png")
    worp = tk.PhotoImage(file="worp.png")
    for y in range (30):
        for x in range(30):
            if maze[y][x] == 1:
                canvas.create_image(x*20+10, y*20+10, image=tree)
            elif maze[y][x] == 0:
                canvas.create_image(x*20+10, y*20+10, image=kusa)
            elif maze[y][x] == 2:
                canvas.create_image(x*20+10, y*20+10, image=worp)

    maetati = tkinter.PhotoImage(file="maetati.png")#前向きの↓プレイヤ－の画像をpngで入れてくれ
    canvas.create_image((mx+1)*20+10, my*20+10, image=maetati, tag="MYCHR")
    main_proc()
    root.mainloop()