import turtle
from freegames import vector # pip install freegames
from random import randint

bird = vector(-100, 0)
balls = []
interval = 1
score = 0

def tap(x, y):
    '''Move bird up in response to screen tap'''
    up = vector(0, 30)
    bird.move(up)

def inside(point):
    '''Return True if point on screen'''
    return -200 < point.x < 200 and -200 < point.y < 200

def draw(alive):
    '''Draw screen objects.'''
    turtle.clear()
    turtle.goto(bird.x, bird.y)

    if alive:
        turtle.dot(10, 'green')
    else:
        turtle.dot(10, 'red')

    for ball,ball_size in balls:
        turtle.goto(ball.x, ball.y)
        turtle.dot(ball_size, 'black')

    turtle.goto(-200,180)
    turtle.write('Score: ' + str(score), font=("Arial", 16, "normal"))

    turtle.update()

def move():
    '''Move InGame Objects''' 
    global interval,score

    bird.y -= 2

    for ball,ball_size in balls:
        ball.x -= interval

    if randint(0,20) == 0:
        y = randint(-199, 199)
        ball = vector(199, y)
        ball_size = randint(10,20)
        balls.append((ball,ball_size))

    while len(balls) > 0 and not inside(balls[0][0]):
        balls.pop(0)
        interval += 0.01
        score +=1

    if not inside(bird):
        draw(False)
        return

    for ball,ball_size in balls:
        if abs(ball - bird) < 10:
            draw(False)
            return

    draw(True)
    turtle.ontimer(move, 20)

turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.up()
turtle.tracer(False)

turtle.onscreenclick(tap)
move()

turtle.done()
