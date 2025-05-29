from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random




def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 400, 0, 600, 0, 1)
    glMatrixMode(GL_MODELVIEW)


def drawpixel(x, y):
    glPointSize(1)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()

initialz = 0
def zonefinder(x1, y1, x2, y2):
    zone = 0
    global initialz
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) >= abs(dy):
        if dx >= 0:
            if dy >= 0:
                zone=0
            else:
                zone= 7
        else:
            if dy >= 0:
                zone = 3
            else:
                zone = 4
    else:
        if dx >= 0:
            if dy >= 0:
                zone = 1
            else:
                zone = 6
        else:
            if dy >= 0:
                zone = 2
            else:
                zone = 5
    initialz = zone


def drawasZero(x, y, zone):
    if zone == 0:
        drawpixel(x, y)
    elif zone == 1:
        drawpixel(y, x)
    elif zone == 2:
        drawpixel(-y, x)
    elif zone == 3:
        drawpixel(-x, y)
    elif zone == 4:
        drawpixel(-x, -y)
    elif zone == 5:
        drawpixel(-y, -x)
    elif zone == 6:
        drawpixel(y, -x)
    elif zone == 7:
        drawpixel(x, -y)


def MPLDraw(x1, y1, x2, y2, zone):
    dx = x2 - x1
    dy = y2 - y1
    incE = 2 * dy
    incNE = 2 * (dy - dx)
    d = 2 * dy - dx
    x = x1
    y = y1
    while x < x2:
        drawasZero(x, y, zone)
        if d < 0:
            d += incE
            x += 1
        else:
            d += incNE
            x += 1
            y += 1


def drawLine(x1, y1, x2, y2):
    zonefinder(x1, y1, x2, y2)
    global initialz
    if initialz ==0:
        MPLDraw(x1, y1, x2, y2, 0)
    elif initialz == 1:
        MPLDraw(y1, x1, y2, x2, 1)
    elif initialz == 2:
        MPLDraw(y1, -x1, y2, -x2, 2)
    elif initialz == 3:
        MPLDraw(-x1, y1, -x2, y2, 3)
    elif initialz == 4:
        MPLDraw(-x1, -y1, -x2, -y2, 4)
    elif initialz == 5:
        MPLDraw(-y1, -x1, -y2, -x2, 5)
    elif initialz == 6:
        MPLDraw(-y1, x1, -y2, x2, 6)
    elif initialz == 7:
        MPLDraw(x1, y1, -x2, -y2, 7)




def restart():
    glColor3f(0, 1, 1)  # Bright teal 
    drawLine(10, 580, 50, 580)
    drawLine(30, 560, 10, 580)
    drawLine(10, 580, 30, 600)

def pauseonoff():
    glColor3f(1, 0.75, 0) # Amber
    drawLine(190, 590, 190, 560)
    drawLine(210, 590, 210, 560)

def play():
    glColor3f(1, 0.75, 0)
    drawLine(210, 580, 190, 600)
    drawLine(190, 560, 210, 580)
    drawLine(190, 600, 190, 560)

def exitbutton(): #red
    glColor3f(1, 0, 0)
    drawLine(390, 600, 350, 560)
    drawLine(390, 560, 350, 600)

def buttonborder():
    glColor3f(.3, .3, .3)
    drawLine(0, 550, 600, 550)


a = random.randrange(-200, 200, 5) #diamond er position random hobe
b = 0
diaR = max(random.random(), 0.3)
diaG = max(random.random(), 0.3)
diaB = max(random.random(), 0.3) #diamond er color jeno bright hoy

def drawdiamond():
    global a, b, diaR, diaG, diaB
    glColor3f(diaR, diaG, diaB)
    glBegin(GL_POLYGON)
    glVertex2f(200 + a, 555 + b)  # top
    glVertex2f(193 + a, 540 + b)  # left
    glVertex2f(200 + a, 525 + b)  # bottom
    glVertex2f(207 + a, 540 + b)  # right
    glEnd()


c = 0
catchR = 1
catchG = 1
catchB = 1
def drawcatcher():
    glColor3f(catchR, catchG, catchB)
    drawLine(140 + c, 20, 260 + c, 20)  
    drawLine(260 + c, 20, 250 + c, 5)   
    drawLine(250 + c, 5, 150 + c, 5)
    drawLine(150 + c, 5, 140 + c, 20)


def specialKey(key, x, y):
    global c, status
    if status == "playing":
        if key == GLUT_KEY_LEFT:
            c -= 25
        elif key == GLUT_KEY_RIGHT:
            c += 25
        
        #catcher jeno bounary touch kore kintu cross na kore 
        c = max(-140, min(c, 140))  
        
    glutPostRedisplay()


dcount = 0
speed = 0
status = "playing"
gameover = False

def keyBoard(key, x, y):
    y = W_Height - y
    global status,gameover, b, score, a, c, catchR, catchG, catchB, diaR, diaG, diaB, speed, dcount
    if key == b' ':
        if status == "playing":
            status = "paused"
            print('paused')
        else:
            catchR = 1
            catchG = 1
            catchB = 1
            if b == 0:
                diaR = random.random()
                diaG = random.random()
                diaB = random.random()
            status = "playing"
            if gameover==True:
                print("restarted")
                gameover = False
            else:
                print("resumed")
    glutPostRedisplay()


def mouse(button, state, x, y):
    y = W_Height - y
    global status, b, score, a, c, catchR, catchG, catchB, diaR, diaG, diaB, speed, dcount, gameover

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        # Pause/Play button
        if 180 < x < 220 and 540 < y < 600:
            if status == "playing":
                status = "paused"
                print('paused')
            else:
                status = "playing"
                print("resumed")
        # Restart button
        elif 0 < x < 55 and 540 < y < 600:
            print('Starting Over')
            status = "playing"
            gameover = False  # Reset gameover state
            a = random.randrange(-200, 200, 5)
            b = 0
            c = 0
            score = 0
            speed = 0
            dcount = 0
            # Reset diamond color 
            diaR = max(random.random(), 0.3)
            diaG = max(random.random(), 0.3)
            diaB = max(random.random(), 0.3)
            # Reset catcher color 
            catchR, catchG, catchB = 1, 1, 1
        # Exit button
        glutPostRedisplay()

        if 330 < x < 400 and 540 < y < 600:
            print("Goodbye")
            print("Final Score:", score)
            glutDestroyWindow(gamewindow) 
    
def animate():
    global b, dcount, speed
    if status == "playing":
        if b > -560:
            b -= (speed + 5)


def collision_check():
    global status, gameover, a, b, c, score, diaR, diaG, diaB, catchR, catchG, catchB, dcount, speed
    cborderL = 140 + c
    cborderR = 260 + c
    cbordertop = 20  
    dborderl = 190 + a
    dborderR = 210 + a
    dborderB = 520 + b 

    if gameover:
        pauseonoff()  #gameover er poreo same pause button dekhabe
    elif status == "playing":
        pauseonoff()
        if dborderB <= cbordertop:  
            if dborderl >= cborderR or dborderR <= cborderL:
                status = "paused"
                gameover = True
                a, b, c = 0, 0, 0
                print("Game Over!")
                print("Final Score:", score)
                diaR, diaG, diaB = 0, 0, 0
                catchR, catchG, catchB = 1, 0, 0
                score = 0
                speed = 0
                dcount = 0
            else:
                b = 0
                a = random.randrange(-190, 190, 10)
                score += 1
                diaR = random.random()
                diaG = random.random()
                diaB = random.random()
                print("Score:", score)
                dcount += 1
                if dcount == 2:
                    speed += 0.5
                    dcount = 0
    else:
        play()  

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    # =====================
    drawcatcher()
    restart()
    exitbutton()
    drawdiamond()
    buttonborder()
    animate()
    collision_check()
    # ======================
    glutSwapBuffers()
    glutPostRedisplay()

W_Width, W_Height = 200, 600
score = 0

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(400, 600)
gamewindow = glutCreateWindow(b"Catch The Diamond")
init()
glutDisplayFunc(display)
glutKeyboardFunc(keyBoard)
glutSpecialFunc(specialKey)
glutMouseFunc(mouse)
glEnable(GL_DEPTH_TEST)
glutMainLoop()