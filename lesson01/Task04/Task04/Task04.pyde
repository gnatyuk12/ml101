pixels2D = [ [0, 250, 235, 201], 
             [100, 150, 30, 250],
             [0, 250, 235, 201],
             [100, 150, 30, 250] ]
pixel_size = 50
x=0
y=0
canvas_size = len(pixels2D) * pixel_size

def setup():
    size(canvas_size, canvas_size)
    background(255, 255, 255)
    noLoop() # draw() выполнится только один раз

def draw():   
    for i in pixels2D:
        global y
        for j in i:
            global x
            random_color = random(0, 255)
            fill(random_color)
            rect(x, y, pixel_size, pixel_size)
            x = x + pixel_size  
        x=0
        y = y + pixel_size
