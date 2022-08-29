import tekihp

hp = 100
tp = 10

def battlestart():
    global hp,tp
    hp = tekihp.und(hp,tp) 
    if hp > 0:
        print("残り体力は" + str(hp))
        print("生き残った！")
        exit()
    else:
        print("You Died")
        exit() 

while True:
    s = input("戦う？")
    if s == "y":
        battlestart()
    else:
        print("戦わなければ生き残れない！")
