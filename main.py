import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect ball collision with wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect ball collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect R paddle miss
    if ball.xcor() > 390:
        ball.reset_game()
        score.l_point()

    # detect L paddle miss
    if ball.xcor() < -390:
        ball.reset_game()
        score.r_point()



screen.exitonclick()
