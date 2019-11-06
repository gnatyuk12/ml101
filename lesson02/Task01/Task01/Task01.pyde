def setup():
    size(700, 300)
    noFill()
    frameRate(4)
    noLoop()

def draw():
    background(255, 255, 255)
    osr = int(random(0,4))
    print(osr)

    if osr == 0:
        for x in range(50, width - 50, 50):
            for y in range(50, height - 50, 50):
                rect(x, y, 25, 25, random(0,25))
                triangle(x+ random(0,25),y, x+15+random(0,15), y+15+random(0,15), x+5+random(0,5), y+15+random(0,5))
    elif osr == 1:
        for x in range(50, width - 50, 50):
            for y in range(50, height - 50, 50):
                for i in range(0, 16, 4):
                    radius_rz = int(random(5,40))
                    ellipse(x,y, radius_rz, radius_rz)
                triangle(x-random(0,15),y, x, y-random(0,20), x+random(0,15), y+random(0,15))
    elif osr == 2:
        for x in range(50, width - 50, 30):
            for y in range(50, height - 50, 30):
                ellipse(x, y, random(0,10), random(0,10))
                rz = int(random(0,2))
                if rz==1:
                    line(x, y + random(0, 5), x + 5, y + random(0, 12))    
    else:
        for x in range(50, width - 50, 50):
            for y in range(50, height - 50, 50):
                for i in range(0, 16, 4):
                    line(x + i, y, x + i, y + 12)
                    ellipse(x+i, y, 10, 10)
                line(x+random(0,12), y+random(0,9), x + 12, y + 9)        

    
    
