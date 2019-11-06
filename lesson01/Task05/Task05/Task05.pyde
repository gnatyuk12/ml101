pixels2D = [ [0, 250, 235, 201], 
             [100, 150, 30, 250],
             [0, 250, 235, 201],
             [100, 150, 30, 250] ]
pixel_size = 50
x=0
y=0
canvas_size = len(pixels2D) * pixel_size
i2=0
j2=0

def setup():
    size(canvas_size, canvas_size)
    background(255, 255, 255)
    noLoop() # draw() выполнится только один раз

def draw():   
    for i in pixels2D:
        global y,i2,j2
        for j in i:
            global x
            random_color = random(0, 255)
            if i2==j2:
                fill(239, 26, 36)
                rect(x, y, pixel_size, pixel_size)
                print("hi")
            else:
                fill(random_color)
                rect(x, y, pixel_size, pixel_size)
            x = x + pixel_size 
            j2=j2+1
        x=0
        y = y + pixel_size
        i2=i2+1
        j2=0
        
print(pixels2D[0][0])
print(pixels2D[1][1])
