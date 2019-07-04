from tkinter import *

class Dinosor:
    def __init__(self):
        self.x = 100
        self.y = 198
        self.life = True
        self.initY = 198
        self.jumping = False
        self.maxJump = 80
        self.img = PhotoImage(file = "./dino.gif")

    def jump(self, event = None):
        if self.y == self.initY:
            self.jumping = True

    def update(self):
        if self.jumping:
            self.y -= 10
            if self.y < self.maxJump:
                self.jumping = False
        else:
            if self.y < self.initY:
                self.y += 5
            if self.y > self.initY:
                self.y = self.initY

    def hit(self, cactus):
        hitDino1 = (self.x - 30, self.y - 40)
        hitDino2 = (self.x + 30, self.y + 40)
        hitCactus1 = (cactus.x - 20, cactus.y - 30)
        hitCactus2 = (cactus.x + 10, cactus.y + 10)
        if hitDino2[0] < hitCactus1[0]:
            return False
        elif hitCactus2[0] < hitDino1[0]:
            return False
        else:
            if hitDino2[1] < hitCactus1[1]:
                return False
            elif hitCactus2[1] < hitDino1[1]:
                return False
            else:
                print("die", hitDino1, hitDino2, hitCactus1, hitCactus2)
                self.life = False
                return True
