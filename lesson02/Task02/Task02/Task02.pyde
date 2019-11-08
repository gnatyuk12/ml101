angle = 0
offset = 150
step = 50
speed = 0.07
num = 20
def setup():
    size(800, 300)
    fill(0)
    noStroke()

def draw():
    background(255, 255, 255)
    global angle
    x=50
    x2=50
    #for x in range(50, width-50, 50):
    for y in range(0, 15, 2):
        myy = ysin(offset, angle, y, step)
        ellipse(x, myy, 20, 20)
        x=x+100
        
    push()  
    fill(255,0,0)  
    for y in range(0, 15, 2):
        myy = ycos(offset, angle, y, step)
        ellipse(x2, myy, 20, 20)
        x2=x2+100
    pop()
    
    angle = angle + speed
   
def ysin(offset, angle, angleplus, step):
    y = offset + sin(angle + angleplus*0.1) * step
    return y    

def ycos(offset, angle, angleplus, step):
    y = offset + cos(angle + angleplus*0.1) * step
    return y
