import pygame as p
import pygame.locals
import math
import time
import winsound
import random as r

def circles(r, g, b, x, y):
    color = r,g,b
    position = x,y
    width = 14
    p.draw.circle(screen,color,position,width)
    
def paddle(r, g, b, position_x, position_y, s, h):
    color = r,g,b
    position = position_x, position_y, s, h
    p.draw.rect(screen,color,position)

def button(x,y, tex, text_size):
    if x <= mouse[0] <= x+140 and y <= mouse[1] <= y+40:
        paddle(120, 120, 120, x, y, 110, 40)
            
    else:
        paddle(0, 0, 230, x, y, 110, 40)
        screen.blit(tex ,text_size)

def dis(x,y, tex, text_size, box_size_h, box_size_w):
    paddle(0, 0, 230, x, y, box_size_w, box_size_h)
    screen.blit(tex ,text_size)
        
pygame.init()
p.display.set_caption("Sling 'n' pong")
colour = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)
white = (255, 255, 255)

again = True
main_m = True
ex = False
font = p.font.Font(None, 34)
point_f = p.font.Font(None, 44)

one_play = font.render('1 player' , True , white)
two_play = font.render('2 player' , True , white)

play_one = font.render('Player 1' , True , white)
play_two = font.render('Player 2' , True , white)


controls = font.render("Controls", True, white)
title = font.render("Sling 'n' pong" , True , white)
b_quit= font.render('Quit' , True , white)

left = font.render("A" , True , white)
left_text = font.render("Left" , True , white)

right = font.render("D" , True , white)
right_text = font.render("Right" , True , white)

P1_Up = font.render("W" , True , white)
P1_Down = font.render("S" , True , white)

P2_Up = font.render("I" , True , white)
P2_Down = font.render("K" , True , white)

up_text = font.render("Up" , True , white)
down_text = font.render("Down" , True , white)

back = font.render("Back" , True , white)

P1_W = 0
P2_W = 0

history = [0]

h_hist = max(history)

while True:
    screen = p.display.set_mode((600,500))

    if main_m == True:
        P1 = False
        P2 = False
        how_tp = False
        
        
        mouse = p.mouse.get_pos()
        button(160, 200, one_play, (170, 210))
        button(340, 200, two_play, (350, 210))
        button(250, 275,controls, (255, 285))
        button(250, 345, b_quit, (280, 360))
        screen.blit(title, (225,50))
        
        p.display.update()
        
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:

                #mouse control for the one player mode button
                if 160-1 <= mouse[0] <= 160+100 and 200 <= mouse[1] <= 200+40:
                    P1 = True
                    main_m = False

                #mouse control for the 2 player mode button
                if 350-1 <= mouse[0] <= 350+100 and 200 <= mouse[1] <= 200+40:
                    P2 = True
                    main_m = False

                if 250-1 <= mouse[0] <= 250+100 and 275 <= mouse[1] <= 275+40:
                    how_tp = True
                    main_m = False
                    
                #Mouse control for the quit button
                if 250-1 <= mouse[0] <= 250+100 and 345 <= mouse[1] <= 345+40:
                    p.quit()
                    ex = True

        if ex == True:
            break
        continue        
    elif main_m == False:
        pass
               
    if again == True:
        velocity_x = 5
        velocity_y = 3

        but_col = (100, 100, 100)
        but_col_hov = (0, 220, 235)

        adv = False
        ex = False
        mul = False

        pos_x = 200
        pos_y = 300

        pad_x = 300
        pad_y = 400

        pad_x1 = 30
        pad_y1= 250

        pad_x2 = 555
        pad_y2 = 250

        pad_velocity = 5
        pad_velocity2 = 5

        clock = pygame.time.Clock()

        width = screen.get_width()

        height = screen.get_height()

        butt_width = 180
        butt_height = 200

        mutt_width = 310
        mutt_height = 200

        point = 1
        again = False
        add = True
    elif again == False:
        pass

#-----------------------------------------------The  controls for P1 and P2
    if how_tp == True:

        clock.tick(60)
        screen.fill((0,0,0))

        screen.blit(one_play, (75,50))
        screen.blit(two_play, (400,50))
        
        screen.blit(left_text, (30,150))
        screen.blit(right_text, (130,150))


        dis(40, 100, left, (50, 110), 40, 40)
        dis(140, 100, right, (150, 110), 40, 40)

        screen.blit(play_one, (345,110))
        
        dis(320, 160, P1_Up,(330, 170), 40, 40)
        dis(420, 160, P1_Down,(430, 170), 40, 40)

        screen.blit(up_text, (310, 210))
        screen.blit(down_text, (410, 210))

        screen.blit(play_two, (345,260))

        dis(320, 310, P2_Up,(330, 320), 40, 40)
        dis(420, 310, P2_Down,(430, 320), 40, 40)

        screen.blit(up_text, (310, 360))
        screen.blit(down_text, (410, 360))

        button(50, 400, back, (70, 410))

        mouse = p.mouse.get_pos()
        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                if 50 <= mouse[0] <= 50+100 and 400 <= mouse[1] <= 400+40:
                    main_m = True
                    continue

        
        p.display.update()

        
    if P2 == True:
#-----------------------------------------------Gameplay
        col = (255, 255, 255)
        points = str(point-1)

        text = font.render((points),True, white)
        
        start = font.render('Restart' , True , white)


        textRect = text.get_rect()
        textRect2 = text.get_rect()
        textRect3 = text.get_rect()

        textRect = (180, 100)
        textRect2 = (butt_width, butt_height)
        textRect3 = (mutt_width, mutt_height)
        
        clock.tick(60)
        screen.fill((0,0,0))

#--------------------------------------------Mouse control
        mouse = p.mouse.get_pos()
        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                if butt_width-1 <= mouse[0] <= butt_width+100 and butt_height <= mouse[1] <= butt_height+40:
                    p.quit()
                    ex = True
                    
                if mutt_width-1 <= mouse[0] <= mutt_width+100 and mutt_height <= mouse[1] <= mutt_height+40:
                    again = True

                if 245-1 <= mouse[0] <= 245+100 and 300 <= mouse[1] <= 300+40:
                    main_m = True
                    again = True
                    continue
                    
        if again == True:
            continue
        elif ex == True:
            break

#-------------------------------------------------
        keys = p.key.get_pressed()

#-----------------------------------P1 Control
        if keys[p.K_s]:
            pad_y1+=pad_velocity

        if keys[p.K_w]:
            pad_y1-=pad_velocity

        if pad_y1 >= 400 and keys[p.K_s]:
             pad_velocity = 0

        elif keys[p.K_w] and pad_y1 >= 400:
            pad_velocity = 5

        if pad_y1 < 5 and keys[p.K_w]:
            pad_velocity = 0

        elif keys[p.K_s] and pad_y1 < 5:
            pad_velocity = 5

#-----------------------------------

#-----------------------------------P2 Control
        if keys[p.K_k]:
            pad_y2+=pad_velocity2

        if keys[p.K_i]:
            pad_y2-=pad_velocity2

        if pad_y2 >= 400 and keys[p.K_k]:
             pad_velocity2 = 0

        elif keys[p.K_i] and pad_y2 >= 400:
            pad_velocity2 = 5

        if pad_y2 < 5 and keys[p.K_i]:
            pad_velocity2 = 0

        elif keys[p.K_k] and pad_y2 < 5:
            pad_velocity2 = 5
#-------------------------------------

#-----------------------------------Outcome of the player's victory
        if pos_x > 580:
            if add == True:
                P1_W=P1_W+1
            add = False
            velocity_x = 0
            velocity_y = 0
            pad_velocity = 0
            
            text = font.render(("Player 1 Won the game"),True, col)
            tally = point_f.render(("{0} - {1}".format(str(P1_W), str(P2_W))) , True , white)
            MM = point_f.render("Menu" , True , white)
            
            screen.blit(text, textRect)
            screen.blit(tally, (275, 400))
            
            button(butt_width, butt_height-5,b_quit, (180+25, 200+5))
            button(mutt_width, mutt_height-5, start, (310+15, 200+5))
            button(245, 300, MM, (255,305))
            p.display.update()
            continue
            
        if pos_x < 20:
            if add == True:
                P2_W=P2_W+1
                
            add = False
            velocity_x=0
            velocity_y = 0
            pad_velocity = 0
            text = font.render(("Player 2 Won the game"),True, col)
            
            tally = point_f.render(("{0} - {1}".format(str(P1_W), str(P2_W))) , True , white)
            MM = point_f.render("Menu" , True , white)
            
            screen.blit(text, textRect)
            screen.blit(tally, (275, 400))
            
            button(butt_width, butt_height-5,b_quit, (180+25, 200+5))
            button(mutt_width, mutt_height-5, start, (310+15, 200+5))
            button(245, 300, MM, (255,305))
            p.display.update()
            continue
#--------------------------------------------------------------

#------------------------------------Ball's physics
        if pos_y > 490:
            velocity_y=-velocity_y
            
        if pos_y < 10:
            velocity_y=-velocity_y

        if pos_x == pad_x1+20 and pos_y <= pad_y1+110 and pos_y >= pad_y1-10:
            velocity_x=-velocity_x
            #winsound.Beep(700, 60)

        if pos_x == pad_x2-5 and pos_y <= pad_y2+110 and pos_y >= pad_y2-10:
            velocity_x=-velocity_x

            #winsound.Beep(700, 60)
        
        circles(235, 235, 105, pos_x, pos_y)
        paddle(0, 0, 235,  pad_x1, pad_y1, 10, 100)
        paddle(235, 0, 0,  pad_x2, pad_y2, 10, 100)
        
        if adv == False:
            p.display.update()
            time.sleep(3)
        else:
            pass
        adv = True

        pos_x+=velocity_x
        pos_y+=velocity_y
#-----------------------------------------------------

        p.display.update()

#----------------------------------------------------One player mode 
    if P1 == True:
        velocity_x = velocity_x
        velocity_y = velocity_y
        col = (255, 255, 255)
        font = p.font.Font(None, 34)
        points = point

        text = font.render((str(points-1)),True, col)
        score = font.render(("Score:"),True, col)
        
        speed = font.render(("Speed:"),True, col)
        vel = font.render((str(round(velocity_x, 2))),True, col)

        high = font.render(("Highest:"),True, col)

        start = font.render('Restart' , True , white)
        
        textRect = text.get_rect()

        textRect = (300, 100)
        textRect3 = (mutt_width, mutt_height)
        clock.tick(60)
        screen.fill((0,0,0))

        mouse = p.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                if butt_width-1 <= mouse[0] <= butt_width+100 and butt_height <= mouse[1] <= butt_height+40:
                    p.quit()
                    ex = True
                        
                if mutt_width-1 <= mouse[0] <= mutt_width+100 and mutt_height <= mouse[1] <= mutt_height+40:
                    again = True

                if 245-1 <= mouse[0] <= 245+100 and 300 <= mouse[1] <= 300+40:
                    main_m = True
                    again = True
                    continue
                        
            if again == True:
                continue
            
            elif ex == True:
                break

    #--------------------------------Control
        keys = p.key.get_pressed()

        if keys[p.K_d] and pad_x < 500:
            pad_x+=pad_velocity

        if keys[p.K_a] and pad_x > 1:
            pad_x-=pad_velocity

        if pos_x > 590:
            velocity_x=-velocity_x
        if pos_x < 10:
            velocity_x=-velocity_x

    #-----------------------------------Game over    
        if pos_y > 490:
            velocity_y=0
            velocity_x=0
            Over = font.render(("Game Over"),True, col)
            screen.blit(Over, (220,50))
            history.append(points-1)
            
            highest = font.render((str(max(history))),True, col)
            MM = point_f.render("Menu" , True , white)
            screen.blit(highest, (320, 400))
            screen.blit(high, (220, 400))
            
            button(butt_width, butt_height-5,b_quit, (180+25, 200+5))
            button(mutt_width, mutt_height-5, start, (310+15, 200+5))
            button(245, 300, MM, (255,305))
            p.display.update()
            continue
    #-------------------------------------------
        
        if pos_y < 10:
            velocity_y=-velocity_y

        if pos_x <= pad_x+95 and pos_x >= pad_x -1 and pos_y <= pad_y+2 and pos_y >= pad_y-5:
            velocity_y=-velocity_y
            point+=1
            mul = False

        elif pos_x <= pad_x+110 and pos_x >= pad_x+95 and pos_y <= pad_y+2 and pos_y >= pad_y-5:
            velocity_y=-velocity_y
            velocity_x=-velocity_x
            point+=1
            mul = False

        pos_x+=velocity_x
        pos_y+=velocity_y
            
        if points % 5 == 0 and mul == False:
            rate = r.randint(1,2)
            if rate == 1:
                velocity_x = velocity_x * 1.082
            elif rate== 2:
                velocity_y = velocity_y * 1.06
            pad_velocity = pad_velocity * 1.002
            mul = True
        
        circles(255, 255, 255, pos_x, pos_y)
        paddle(255, 255, 255,  pad_x, pad_y, 100, 10)
        screen.blit(text, textRect)
        screen.blit(score, (220, 100))
        screen.blit(speed, (10, 10))
        screen.blit(vel, (100, 10))
        
        p.display.update()
    

