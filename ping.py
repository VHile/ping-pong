import turtle
from random import choice
from winsound import PlaySound, SND_ASYNC

FONT = ("Arial", 30)

window = turtle.Screen()
window.title("Ping-Pong")
window.setup(width=1.0, height=1.0)
window.bgcolor('black')
window.tracer(2)

score_l = 0
score_r = 0
speed_counter = 0
start_stop = True

s_left = turtle.Turtle(visible=False)
s_left.color('#ffeb0f')
s_left.penup()
s_left.setposition(-400, 300)
s_left.write(f"Player 1: {score_l}", font=FONT)

s_right = turtle.Turtle(visible=False)
# s_right.colormode('#a0c8f0')
s_right.color('red')
s_right.penup()
s_right.setposition(200, 300)
s_right.write(f"Player 2: {score_r}", font=FONT)

instruction = turtle.Turtle(visible=False)
instruction.color('red')
instruction.penup()
instruction.setposition(-800, 0)
instruction.write(
    """
    How to play:
    
    Press 'R' - Restart 
    Press 'Space' - pause 
    
    Left Player:
    'W' - up 
    'S' - down 
     
    Right Player:
    '↑' - up 
    '↓' - down
    """,
    font=("Arial", 20))

winner = turtle.Turtle(visible=False)
winner.color('blue')
winner.penup()
winner.setposition(-150, 150)

border = turtle.Turtle()
border.speed(0)
border.color('green')
border.begin_fill()
border.goto(-500, 300)
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()
border.goto(0, 300)
border.color('white')
border.setheading(270)

for i in range(25):
    if i % 2 == 0:
        border.pendown()
        border.forward(24)
    else:
        border.penup()
        border.forward(24)
border.hideturtle()

rocket_l = turtle.Turtle()
rocket_l.color('#ffeb0f')
rocket_l.shape('square')
rocket_l.shapesize(stretch_len=1, stretch_wid=5)
rocket_l.penup()
rocket_l.goto(-490, 0)


def move_up_l():
    y = rocket_l.ycor()
    if y >= 235:
        rocket_l.sety(250)
    else:
        rocket_l.sety(y + 60)


def move_down_l():
    y = rocket_l.ycor()
    if y <= -235:
        rocket_l.sety(-250)
    else:
        rocket_l.sety(y - 60)


rocket_r = turtle.Turtle()
rocket_r.color('red')
rocket_r.shape('square')
rocket_r.shapesize(stretch_len=1, stretch_wid=5)
rocket_r.penup()
rocket_r.goto(490, 0)


def move_up_r():
    y = rocket_r.ycor()
    if y >= 235:
        rocket_r.sety(250)
    else:
        rocket_r.sety(y + 60)


def move_down_r():
    y = rocket_r.ycor()
    if y <= -235:
        rocket_r.sety(-250)
    else:
        rocket_r.sety(y - 60)


def play_ball():
    PlaySound('Sounds/ball.wav', SND_ASYNC)


def play_loose():
    PlaySound('Sounds/loss.wav', SND_ASYNC)


def play_rocket():
    PlaySound('Sounds/rebound.wav', SND_ASYNC)


def reload():
    global score_l, score_r, start_stop
    score_l = 0
    score_r = 0
    s_left.clear()
    s_left.write(f"Player 1: {score_l}", font=FONT)
    s_right.clear()
    s_right.write(f"Player 2: {score_r}", font=FONT)
    winner.clear()
    winner.write("", font=FONT)
    ball.goto(0, 0)
    start_stop = True


def pause():
    global start_stop
    if start_stop:
        start_stop = False
    else:
        start_stop = True


ball = turtle.Turtle()
ball.color('white')
ball.shape('circle')
ball.shapesize(stretch_len=1, stretch_wid=1)
ball.speed(0)
ball.penup()
ball.dx = 2
ball.dy = 2
choice_b = 2
window.listen()
window.onkeypress(move_up_l, "w")
window.onkeypress(move_down_l, "s")

window.onkeypress(move_up_r, "Up")
window.onkeypress(move_down_r, "Down")
window.onkeypress(reload, "r")
window.onkeypress(pause, "space")

while True:
    try:
        window.update()
        if start_stop:
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

        if ball.xcor() >= 485:
            ball.goto(-470, choice([200, 100, -100, -200]))
            # ball.dx = choice([-choice_b, choice_b])
            # ball.dy = choice([-choice_b, choice_b])
            play_loose()
            score_l += 1
            s_left.clear()
            s_left.write(f"Player 1: {score_l}", font=FONT)

        if ball.ycor() >= 295:
            ball.dy = -ball.dy
            play_ball()

        if ball.xcor() <= -485:
            ball.goto(470, choice([200, 100, -100, -200]))
            # ball.dx = choice([-choice_b, choice_b])
            # ball.dy = choice([-choice_b, choice_b])
            play_loose()
            score_r += 1
            s_right.clear()
            s_right.write(f"Player 2: {score_r}", font=FONT)

        if ball.ycor() <= -295:
            ball.dy = -ball.dy
            play_ball()

        if ball.xcor() < 480 or ball.ycor() < rocket_r.ycor() - 50 or ball.ycor() > rocket_r.ycor() + 50:
            pass
        else:
            ball.dx = -ball.dx
            # if speed_counter % 1 == 0:# and ball.dx <= 6:
            #     ball.dx -= 1
            #     speed_counter += 1
            play_rocket()

        if ball.xcor() <= -480 and rocket_l.ycor() + 50 >= ball.ycor() >= rocket_l.ycor() - 50:
            ball.dx = -ball.dx
            play_rocket()

        if score_l == 10:
            start_stop = False
            ball.goto(0, 0)
            s_left.clear()
            s_left.write(f"Player 1: {score_l}", font=FONT)
            s_right.clear()
            s_right.write(f"Player 2: {score_r}", font=FONT)
            winner.clear()
            winner.write(f"   PLAYER 1 WIN\nYOUR SCORE IS: {score_l}", font=FONT)

        if score_r == 10:
            start_stop = False
            ball.goto(0, 0)
            s_left.clear()
            s_left.write(f"Player 1: {score_l}", font=FONT)
            s_right.clear()
            s_right.write(f"Player 2: {score_r}", font=FONT)
            winner.clear()
            winner.write(f"   PLAYER 2 WIN\nYOUR SCORE IS: {score_r}", font=FONT)
    except Exception:
        print("End Game")
        break


window.mainloop()

