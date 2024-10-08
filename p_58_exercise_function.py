def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal()!=True:
    if wall_in_front():
        turn_left()
    if right_is_clear():
        turn_right()
    if wall_on_right() and wall_in_front():
        turn_left()
    if wall_in_front() and right_is_clear():
        turn_right()
    move()


    def turn_right():
        turn_left()
        turn_left()
        turn_left()


    def jump():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()


    while not at_goal():
        if wall_in_front():
            jump()
        else:
            move()


#Hurdle 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
