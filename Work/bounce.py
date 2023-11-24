# bounce.py
#
# Exercise 1.5
ball_height = 100
bounce = 0
while bounce < 10:
    ball_height = ball_height* 0.6
    bounce += 1
    print(bounce, round(ball_height, 2))