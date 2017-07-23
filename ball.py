import simplegui
import random

#Intial position of the paddle
point_one = [70, 270]
point_two = [90, 270]


#Initial speed of the ball
x_speed = 5
y_speed = -6

#Current location of the ball
position_x = 0
position_y = 0

ball_moving = False

def ball_move():
    
    global position_x, position_y
    global x_speed, y_speed
    global point_one, point_two
      
    if(ball_moving):
        wall_check()
        position_x += x_speed
        position_y += y_speed
    else:
        position_x = (point_two[0] + point_one[0]) / 2
        position_y = 270 - 10 
        point_one = [70, 270]
        point_two = [110, 270]
    
def wall_check():
    global x_speed,y_speed
    global ball_moving
    global position_x, position_y
    global point_one, point_two
    
    #Check to see if the ball touches top wall
    if(position_y < 10):
        y_speed = - y_speed
    #Check to see if the ball touches the right wall
    elif (position_x > 240):
        x_speed = -x_speed
    #Check to see if the ball touches the left wall
    elif (position_x < 10):
        x_speed = -x_speed 
    #Check to see if the ball touches the paddle
    elif(position_x > point_one[0] and position_x < point_two[0] and
        position_y > 270 - 10 ):
        y_speed = - y_speed
    #Check to see if the ball fell down
    elif (position_y > 290):
        ball_moving = False
        
    
def paddle_move(key):
     global ball_moving   
     ball_moving = True   
            
     if key == simplegui.KEY_MAP['right']:
            point_one[0] += 16
            point_two[0] += 16
     elif key == simplegui.KEY_MAP['left']:
            point_one[0] -= 16
            point_two[0] -= 16    
  
def draw(canvas): 
    canvas.draw_circle((position_x, position_y), 1, 10, "blue")
    canvas.draw_line(point_one, point_two, 1, "red")
    
frame = simplegui.create_frame('Testing', 250, 300)
frame.set_canvas_background("white")
frame.set_draw_handler(draw)
frame.set_keydown_handler(paddle_move)
timer = simplegui.create_timer(90,ball_move)
labe1 = frame.add_label('Press Right key to start')


timer.start()
frame.start()
