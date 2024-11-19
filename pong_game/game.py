import arcade

SCREEN_WIDTH = 800
SCREEN_HEIHT = 600
SCREEN_TITLE = "Pong Game"

class Bar(arcade.Sprite):
    def __init__(self):
            super().__



class Game(arcade.Window):
    def __init__(self, widht,height,title ):
        super().__init__(widht,height,title)
        self.bar = Bar()


    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()


if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIHT, SCREEN_TITLE)
    arcade.run()
