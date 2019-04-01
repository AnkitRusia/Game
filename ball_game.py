def b_i():


          import pygame
          import time
          import random
          



          pygame.init()



          screen_length = 1250
          screen_height = 630
          screen_size = [screen_length , screen_height]
          gamescreen = pygame.display.set_mode(screen_size)
          pygame.display.set_caption('kanha is great')

          clock = pygame.time.Clock()


          board = pygame.image.load('board.png')
          ball = pygame.image.load('ball.png')
          board1 = pygame.image.load('board1.png')
          bound = pygame.image.load('bound.png')


          file = 'game_loop.mp3'
          pygame.mixer.init()
          pygame.mixer.music.load(file)






          def text_object(text,font,text_color):
               
               textsurface = font.render(text,True,text_color)
               return textsurface,textsurface.get_rect()


          def message_display (text,text_color) :
               largetext = pygame.font.Font('freesansbold.ttf',50)
               textsurf, textrect = text_object(text,largetext,text_color)
               textrect.center = (400,300)
               gamescreen.blit(textsurf,textrect)
               pygame.display.update()
               time.sleep(2)
               game_loop()

          def button(msg , b_x, b_y, b_c_i , b_c_a, b_wide, b_height , action) :
               pygame.draw.rect(gamescreen,b_c_i,(b_x, b_y , b_wide , b_height))

               mouse = pygame.mouse.get_pos()
               click = pygame.mouse.get_pressed()
               
               
               if b_x+100 > mouse[0] > b_x and b_y+50 > mouse[1] > b_y :
                    pygame.draw.rect(gamescreen,b_c_a,(b_x, b_y , b_wide , b_height))
                    if click[0] == 1 :
                         if action == "start" :
                              game_loop()
                         elif action == "quit" :
                              pygame.quit()
                              quit()
                          
                         

               color = (180,251,197) 
               smalltext = pygame.font.Font("freesansbold.ttf",20)
               textsurf,textrect = text_object(msg,smalltext,color)
               textrect.center = ((b_x + 50),(b_y + 25))
               gamescreen.blit(textsurf,textrect)
                   



          def intro():
               while True :
                    blue = (50,50,195)
                    

                    for event in pygame.event.get():
                         if event.type == pygame.QUIT :
                              pygame.quit()
                              quit()
                    gamescreen.fill(blue)
                    green_d = (10,150,10)
                    green_l = (10,255,10)
                    red_d = (150 , 0,0)
                    red_l = (255 , 0,0)
                    color_s = (237,150,80) 
                    smalltext = pygame.font.Font("freesansbold.ttf",70)
                    textsurf,textrect = text_object("     PLAY IN HOME !",smalltext,color_s)
                    textrect.center = ((400),300)
                    gamescreen.blit(textsurf,textrect)
                         
                    button("START", 140 , 470 ,green_d , green_l , 100 , 40 , "start")
                    button("QUIT", 990 , 470 ,red_d , red_l , 100 , 40 , "quit")
                    
                    
                    pygame.display.update()
                    clock.tick(15)


          def bound_w():
               gamescreen.blit(bound,(0,0))
          def board_pos(x,y):
               gamescreen.blit(board,(x,y))

          def ball_pos(x,y):
               gamescreen.blit(ball,(x,y))

          def board1_pos(x,y):
               ball_ref = random.randrange(50,60)
               gamescreen.blit(board1,((x - ball_ref),y))
##          def crash() :
##               lost_c = (250 ,5 , 5)
##               message_display('   YOU LOST !!!',lost_c)


               
          def game_loop():
               ball_x = screen_length * 0.5
               ball_y = screen_height * 0.5
               ball_speed = 3
               ball_dir_x = 1
               ball_dir_y = -1
               car_game_point =0 
               score = 0

               board_move_x = 0
               board_speed = 10
               board_pos_x = screen_length * 0.456
               
               black = (0,0,0)
               pygame.mixer.music.play(-1)
               while True :
                    
                    
                    
                    for event in pygame.event.get():
                         if event.type == pygame.QUIT:
                              pygame.quit()
                              quit()
                         if event.type == pygame.KEYDOWN :
                           if event.key == pygame.K_LEFT :
                              board_move_x = (-1 * board_speed)
                           elif event.key == pygame.K_RIGHT :
                                board_move_x = board_speed
                         if event.type == pygame.KEYUP :
                            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT :
                                 board_move_x = 0

                    gamescreen.fill(black)
                    
                    bound_w()
                    if board_pos_x < 9  :
                         board_pos_x = 9
                    if board_pos_x > 999 :
                         board_pos_x = 999
                    
                    board_pos((board_pos_x),(screen_height * 0.92))

                    board1_pos((ball_x),(screen_height * 0.03))
                    color_score = (250 ,250 , 200)
                    smalltext = pygame.font.Font("freesansbold.ttf",20)
                    textsurf,textrect = text_object("SCORE : "+str(score),smalltext,color_score)
                    textrect.center = (50,13)
                    gamescreen.blit(textsurf,textrect)
                    

                    if ball_x < 5 or ball_x > 1200 :
                         ball_dir_x *= -1
                         #pygame.mixer.Sound.play(bounce)

                    
                    if ball_y < 40 :
                         ball_dir_y *= -1

                    if (board_pos_x < ball_x < (board_pos_x+230)) and (ball_y > 570 ) :
                         ball_dir_y *= -1
                         ball_speed += (ball_speed * 0.2)
                         board_speed += (board_speed * 0.12)
                         score += 1
                         #pygame.mixer.Sound.play(bounce)


                    
                    if ball_y > 620 :
                         car_game_point += 1
                         if car_game_point > 3 :
                              
                             import car_game

                         color_score = (250 ,250 , 200)
                         smalltext = pygame.font.Font("freesansbold.ttf",50)
                         textsurf,textrect = text_object("lost : "+str(car_game_point),smalltext,color_score)
                         textrect.center = (100,53)
                         gamescreen.blit(textsurf,textrect)

                         
                         
                         

                    
                    ball_pos(ball_x,ball_y)
                    ball_x += (ball_speed * ball_dir_x)
                    ball_y += (ball_speed * ball_dir_y)


                    board_pos_x += board_move_x
                    
                    pygame.display.update()
                    clock.tick(30)


          intro() 
                       
          pygame.quit()
          quit()



