import pygame
import ball_game
global star_t
star_t = 1


global star_d
star_d = 1


pygame.init()

gs_wide =1200
gs_len = 600
gs_size = (gs_wide,gs_len)
gscr = pygame.display.set_mode(gs_size)
pygame.display.set_caption("kanha is graet")

clock = pygame.time.Clock()

char = pygame.image.load('ball.png')
brick = pygame.image.load('brick.png')
ground = pygame.image.load('ground.png')
gate1 = pygame.image.load('gate1.png')
star = pygame.image.load('star.png')
p = pygame.image.load('p.png')
pw = pygame.image.load('pw.png')
pw1 = pygame.image.load('pw1.png')

global walk
walk = 5


def char_pos(x,y):
     global star_t ; global star_d
     global walk

     
     if walk % 5 == 0 :
       gscr.blit(p,(x,y))
     
     if walk % 2 == 0 :
       gscr.blit(pw,(x,y))

     if walk % 3 == 0 :
       gscr.blit(pw1,(x,y))     


     
     if ( 20 < x < 74 and 5 < y < 20):
          star_t = 0 
     if (1075 < x < 1128 and 358 < y < 370 ) :                                        
          star_d = 0
     if 990 < x < 1120 and 65 < y < 85 :
                    ball_game.b_i()
     

def bricks_wall():
     gscr.blit(ground,(10,560))
     gscr.blit(ground,(85,560))
     gscr.blit(ground,(138,560))
     gscr.blit(ground,(305,560))
     gscr.blit(ground,(565,560))
     gscr.blit(ground,(680,560))
     gscr.blit(ground,(765,560))
     gscr.blit(ground,(880,560))
     ########  1  #######
     gscr.blit(ground,(1020,465))
     gscr.blit(ground,(500,465))
     ########  2  #######
     gscr.blit(ground,(300,370))     
     gscr.blit(ground,(700,370))
     gscr.blit(ground,(835,370))
     ########  3  #######
     gscr.blit(ground,(835,275))
     gscr.blit(ground,(935,275))
     gscr.blit(ground,(210,275))
     gscr.blit(ground,(60,275))
     ########  4  #######
     gscr.blit(ground,(200,185))
     gscr.blit(ground,(360,185))
     gscr.blit(ground,(780,185))
     ########  5  #######
     gscr.blit(ground,(30,95))
     ####### GATE  #######
     gscr.blit(gate1,(1020,6))


def stars():
     global star_t ; global star_d
     if star_t == 1 :
       gscr.blit(star,(36,35))
     if star_d == 1 :
       gscr.blit(star,(1100,415))
     

def gravity(c_p_y, c_m_y_t, f ):
     ######## f0 ###########
     if c_p_y < f and c_m_y_t == 0 :
               c_p_y +=10
     return c_p_y




def game_loop():
     char_pos_x = 15
     char_pos_y = 462
     char_move_x = 0
     char_move_y = 0
     char_move_y_t = 0
     global walk 

     
     ground = 462
     black = (20,50,50)
     while True :
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

               if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_UP :
                         char_move_y_t = 15
                         
                    if event.key == pygame.K_LEFT :
                         char_move_x = -7 ; walk =3
                    if event.key == pygame.K_RIGHT :
                         char_move_x = 7 ; walk =2
               if event.type == pygame.KEYUP :
                  if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT :
                       char_move_x = 0 ; walk =5
                         
      
          char_pos_x += char_move_x



          ########       jump      #######     
          if char_move_y_t > 0 :
               char_move_y = 8
               char_pos_y -= char_move_y
               char_move_y_t -= 1
               
               
               
          #######        gravity   ########
          if char_pos_y < 441 and  char_pos_y > 305 :
               if  480 < char_pos_x < 656 or 1005 < char_pos_x < 1176 :
                    ground = 362
               else :
                    ground = 462
          if char_pos_y <= 341 and  char_pos_y > 251:
               if  290 < char_pos_x < 446 or 650 < char_pos_x < 846 or 820 < char_pos_x < 976 :        
                    ground = 274  
               else :
                    ground = 462
          if char_pos_y <= 211 and  char_pos_y > 141:
               if  823 < char_pos_x <  1080 or 210 < char_pos_x < 366 or 50 < char_pos_x < 215:
                   ground = 184
               else :
                    ground = 462
          if char_pos_y <= 141 and  char_pos_y > 50:
               if  195 < char_pos_x < 500 or 770 < char_pos_x < 915:
                    ground = 85
               else :
                    ground = 462
          if char_pos_y <= 50 and  char_pos_y > 0:
               if  15 < char_pos_x < 176 :
                    ground = 5
               else :
                    ground = 462
          
          char_pos_y = gravity(char_pos_y,char_move_y_t, ground ) 
          ###  gravity(c_p_y, c_m_y_t, f )
          
          
          

          
               
          ######    DISPLAY    ###########
          gscr.fill(black)
          bricks_wall()
          stars()
          char_pos(char_pos_x, char_pos_y)
          

          
          pygame.display.update()
          clock.tick(30)



game_loop()
                         
