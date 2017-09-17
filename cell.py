class Cell:
    def __init__(self, r, g, b, liv):
        self.red = r
        self.green = g
        self.blue = b
        self.alive = False

    def updateHealth(self,liv):
        self.alive = liv

    def updateColor(self, r,g,b):
        self.red = r
        self.green = g
        self.blue = b

    def copyCell(self, x):
        self.alive = x.alive
        self.red = x.red
        self.green = x.green
        self.blue = x.blue
