from pico2d import load_image

class Grass:
    def __init__(self, y_position=0):
        self.image = load_image('grass.png')
        self.y_position = y_position

    def draw(self):
        self.image.draw(400, self.y_position)

    def update(self):
        pass