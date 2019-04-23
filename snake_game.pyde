from Snake import Snake

width = 600
height = 600

snake = Snake()
direction = UP

def setup():
    size(width, height)
    frameRate(10)
    pass
    
def draw():
    background(50) 
    fill(255)
    snake.show()
    direction = keyCode
    snake.move(direction)
    
    pass
    
def keyPressed():
    print(str(keyCode) + " pressed.")
    if key == CODED: snake.move(keyCode)
    pass

def mouseClicked():
    snake.grow()
    pass
