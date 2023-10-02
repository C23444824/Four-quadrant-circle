def setup():
    size(500,500)
    
def draw():
    noStroke()
    
    # <>
    # ==
    # <=
    # >=
    # and 
    # or 
    
    if mouseX < width / 2:
        if mouseY < height / 2:
            fill(255,0,0)
        else:
            fill(0,255,0)
        
    else:
        if mouseY < height / 2:
            fill(0,0,255)
        else:
            fill(255,255,0)
    
    
    circle(mouseX,mouseY,50)


    
    
