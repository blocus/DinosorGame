from tkinter import *
from Dinosor import Dinosor
from Cactus import Cactus
import time
import random

def wait(t):
    fin = time.time() + t
    while time.time() < fin:
        continue


main = Tk()
c = Canvas(main, width=800, height=300, background='#4d99f7')
c.create_rectangle(0, 250, 800, 320, fill='#1ec131', width="0")
dinosor = Dinosor()
dinosorInCanvas = c.create_image(dinosor.x, dinosor.y, image=dinosor.img)
main.bind("<space>", dinosor.jump)

score = 0
scoreTxt = c.create_text(700, 50, text="Score :" + str(score), fill="white", font=('arial', 20, 'bold'))
cactusList = []
cactusInCanvasList = []
c.pack()
while dinosor.life:
    score += 1
    c.itemconfig(scoreTxt, text="Score :" + str(score))

    if len(cactusList) == 0:
        cactus = Cactus()
        cactusList.append(cactus)
        cactusInCanvasList.append(c.create_image(cactus.x, cactus.y, image=cactus.img))
    if random.random() < 0.01:
        cactus = Cactus()
        test = True
        for cact in cactusList:
            if abs(cactus.x - cact.x) < 250:
                test = False
        if test:
            cactusList.append(cactus)
            cactusInCanvasList.append(c.create_image(cactus.x, cactus.y, image=cactus.img))
    dinosor.update()

    c.coords(dinosorInCanvas, dinosor.x, dinosor.y)
    tmpList = []
    tmpCanvasList = []
    for i in range(len(cactusList)):
        cactusList[i].move()
        c.coords(cactusInCanvasList[i], cactusList[i].x, cactusList[i].y)
        if cactusList[i].x > 0:
            tmpList.append(cactusList[i])
            tmpCanvasList.append(cactusInCanvasList[i])
            dinosor.hit(cactusList[i])

    cactusList = tmpList
    cactusInCanvasList = tmpCanvasList
    c.update()
    wait(0.01)
c.delete("all")
c.create_text(400, 150, text="Game Over", fill="white", font=('arial', 50, 'bold'))
c.create_text(400, 200, text="Score " + str(score), fill="white", font=('arial', 20, 'bold'))

main.mainloop()
