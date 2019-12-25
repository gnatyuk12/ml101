rot = 0
freq = 0.000005

def setup():
    size(1300, 600)
    #frameRate(15)
    
def draw():
    background(242)
    global rot
    
    
    pushMatrix()
    #translate(350,300)
    translate(width/2,height/2)
    rotate(radians(-90))
    for i in range(50):
        rotate(radians(rot/120)) 
        circl = 100 + 150 * sin(millis()*freq*i)
        r = map (circl, 100, 50, 5, 1)
        fill(255, 0, 0)
        stroke(255, 0, 94)
        #ellipse(circl*cos(i), circl*sin(i), r, r)
        drawShape(circl*cos(i), circl*sin(i))
        rot = rot + 0.00005
    for i in range(200):
        rotate(radians(rot/8)) 
        circl = 100 + 180 * sin(millis()*freq*i)
        r = map (circl, 150, 100, 5, 1)
        fill(10,134,247)
        noStroke()
        ellipse(circl*cos(i), circl*sin(i), r/2, r/2)
        rot = rot + 0.00005
    popMatrix()


def drawShape(w, h):
    push()
    translate(w, h)
    scaler = 5 # размер шейпов
    s = 1 # установите 1, чтобы получить резуотиаи как на рис. 26
    for s in range(s):
        beginShape() # рисуем сложную форму по точкам через curveVertex()
        
        # параметры суперформулы
        m = 6
        n1 = 1
        n2 = 1
        n3 = 6

        points = superFormula(m, n1, n2, n3)
        
        for i in range(len(points)):
            curveVertex(points[i][0] * scaler, points[i][1] * scaler)
        
        endShape()
        
    pop()

        
def superFormula(m, n1, n2, n3):
    numPoints = 360
    phi = TWO_PI / numPoints
    points = []
    for i in range(numPoints):
        points.append(superFormulaPoint(m, n1, n2, n3, phi*i)) 
    return points

def superFormulaPoint(m, n1, n2, n3, phi):
    r = 0
    a = 1
    b = 1
    
    t1 = 0 
    t2 = 0
    
    x = 0
    y = 0
    
    t1 = cos(m * phi / 4) / a
    t1 = abs(t1)
    t1 = pow(t1, n2)
    
    t2 = sin(m * phi / 4 ) / b
    t2 = abs(t2)
    t2 = pow(t2, n3)
    
    r = pow(t1 + t2, 1/n1)
    if abs(r) == 0:
        x = 0
        y = 0
    else:
        r = 1 / r
        x = r * cos (phi)
        y = r * sin (phi)

    return (x, y)
