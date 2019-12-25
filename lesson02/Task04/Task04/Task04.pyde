rot = 0
freq = 0.000005

def setup():
    size(1300, 600)
    
def draw():
    background(242)
    global rot
    
    pushMatrix()
    #translate(350,300)
    translate(width/2,height/2)
    rotate(radians(-90))
    for i in range(300):
        rotate(radians(rot/120)) 
        circl = 100 + 150 * sin(millis()*freq*i)
        r = map (circl, 100, 50, 5, 1)
        fill(255, 0, 94)
        noStroke()
        ellipse(circl*cos(i), circl*sin(i), r, r)
        rot = rot + 0.00005
    for i in range(200):
        rotate(radians(rot/8)) 
        circl = 100 + 180 * sin(millis()*freq*i)
        r = map (circl, 150, 100, 5, 1)
        fill(10,134,247)
        noStroke()
        ellipse(circl*cos(i), circl*sin(i), r/2, r/2)
        for n in range(3):
            rotate(radians(PI/4))
            circl= 5 + 2 * sin(millis()*freq*i)
            r = map (circl, 10, 50,1,1)
            fill(4)
            noStroke()
            ellipse(circl*sin(i), circl*tan(i), r, r*2)
            #triangle(0, circl*sin(i), circl*tan(i),0, r/2,r)
        rot = rot + 0.00005
    popMatrix()
