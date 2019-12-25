angle = 0.0
speed = 0.005
scalefactor = 0

def setup():
   size(700, 300)
   fill(0)
   noStroke()
   
def draw():   
    background(255, 255, 255)
    translate(width/2, height/2)
    global angle
    global scalefactor
    rotate(angle)
    
    for i in range(20):
        push()
        rotate(i)
        translate(mouseX-width/2, mouseY)
        ellipse(0, 0, 10, 10)
        rotate(angle)
        pop()
        for j in range(10):
            push()
            rotate(j-150)
            translate(0, mouseY)
            fill(77,142,255)
            stroke(246,56,12)
            triangle(0,0,30,5,50,50)
            pop()
            for k in range(5):
                push()
                fill(255,226,76)
                rotate(k*TWO_PI/5)
                translate(mouseX/2, 100)
                ellipse(0,0,10,1*scalefactor)
                scale(angle)
                pop()
        for l in range(10):
            push()
            rotate(l-3)
            translate(random(0,10), mouseX)
            fill(239,39,194)
            ellipse(10,10,random(10,25),25)
            pop()
                
       
    angle = angle + speed
    scalefactor = scalefactor + 0.5
