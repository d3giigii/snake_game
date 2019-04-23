width = 600
height = 600

class Snake():
    def __init__(self):
        self.arr = []
        self.arr.append([width/40, height/40])
        self.x_pos = 300
        self.y_pos = 300
        pass
    
    def show(self):
        for i in self.arr:
            square(self.x_pos, self.y_pos, width/40)
            pass
        pass
    
    def move(self, k):
        if k == UP: self.y_pos -= 15
        if k == DOWN: self.y_pos += 15
        if k == LEFT: self.x_pos -= 15
        if k == RIGHT: self.x_pos += 15
        pass
    
    def grow(self):
        print("Grew.")
        pass
    
    pass
