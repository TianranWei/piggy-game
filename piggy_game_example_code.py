# -*- coding: UTF-8 -*-
# A Python Piggy Game for my Darling.
# By @BigPiggy

import turtle
import time
import random
import easygui

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @BigPiggy")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
wn.addshape("./pig_background_resized-50-50.gif")
head.shape("./pig_background_resized-50-50.gif")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

# Welcome window

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        controler = random.randint(0,4)
        if controler == 0:
            easygui.msgbox("啊啊啊啊啊啊 撞墙啦！")
        if controler == 1:
            easygui.msgbox("嗷 摸摸猪脑袋")
        if controler == 2:
            easygui.msgbox("咚~~")
        if controler == 3:
            easygui.msgbox("哼！臭墙！")
        if controler == 4:
            easygui.msgbox("可能~~我撞了南墙才会回头吧！！")
        
        


        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        del segments[:]

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    
    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("./pig_background_resized-50-50.gif")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 
        
        # Special messages
        if score ==300:
            msg_1()

            
        def msg_1():
            msg_1 = easygui.buttonbox("啊啊啊啊啊啊，恭喜你！！贪吃猪终于吃饱了！你成为了第一个打通了贪吃猪游戏的猪猪！彩蛋是你的啦！",title="彩蛋彩蛋！",choices=["我要看我要看！","冷漠走开","愿世界和平"])
            if(msg_1 == "我要看我要看！"):
                msg_2()
            elif msg_1 == "冷漠走开":
                msg_back()
            elif msg_1 == "愿世界和平":
                msg_peace()

        def msg_back():
            easygui.msgbox("啊啊啊 你快回来～～～", ok_button = "那 那好吧")
            msg_1()

        def msg_peace():
            easygui.msgbox("照我脸上亲一口，世界和平全都有！",ok_button = "那 那亲你一下吧")
            msg_1()
        
        def msg_2():
            msg_2 = easygui.buttonbox("玩家需要先回答几个问题喔！\
                    \
                    问题一：？",title="彩蛋彩蛋！",choices=["快乐星球","某外图书馆","海底捞"])
            if(msg_2 == "某外图书馆"):
                msg_3()
            else:
                msg_not_piggy_2()

        def msg_not_piggy_2():
            easygui.msgbox("啊啊啊啊你不是我的！")
            msg_2()

        def msg_3():
            msg_3 = easygui.buttonbox("哇！好厉害！不过这个问题的答案有其他人也知道，所以还是要继续回答喔~\
                \
                问题二：？",title="彩蛋彩蛋！",choices=["a","b","aaaa！"])
                
            if msg_3 == "a":
                msg_not_piggy_3()
            else:
                msg_4()

        def msg_not_piggy_3():
            easygui.msgbox("You are not my piggy!!")
            msg_3()

        def msg_4():
            msg_4 = easygui.msgbox("哈哈哈，看来你是真的！那 那我就要祝我们纪念日快乐啦！",title="彩蛋彩蛋！")

            wn.bye()

            
    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            easygui.msgbox("啊啊啊啊啊啊 撞到猪屁股啦！")
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            del segments[:]

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()