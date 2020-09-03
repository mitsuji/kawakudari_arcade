import arcade
import random
from ichigojam import Std15

class Kawakudari(arcade.Window):

    def __init__(self):
        super().__init__(512, 384, "kawakudari")
        self.std15 = Std15(512, 384, 32, 24)
        self.frame = 0
        self.x = 15
        self.running = True

    def on_update(self, delta_time):
        if not self.running:
            return
        if self.frame % 5 == 0:
            self.std15.locate(self.x, 5)
            self.std15.putc(ord('0'))
            self.std15.locate(random.randrange(32), 23)
            self.std15.putc(ord('*'))
            self.std15.scroll()
            if not self.std15.scr(self.x,5) == 0:
                self.running = False
        self.frame += 1
    
    def on_draw(self):
        self.std15.draw()

    def on_key_press(self, key, key_modifiers):
        if(key == arcade.key.LEFT):
            self.x -=1
        if(key == arcade.key.RIGHT):
            self.x +=1


def main():
    game = Kawakudari()
    arcade.run()

if __name__ == "__main__":
    main()
    
