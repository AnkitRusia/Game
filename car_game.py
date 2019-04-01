import pygame
import time
import random

pygame.init()
gameDisplay = pygame.display.set_mode((1250,600)) 
pygame.display.set_caption('kanha is great')
clock = pygame.time.Clock()  

color_r = (10,10,200)
pause = False ############## new*  ########################

gameimg = pygame.image.load('car1.png')
bound = pygame.image.load('bound.png')

global m_s
m_s = 0

def text_object(text,font):
     black = (250,200,200)
     textsurface = font.render(text,True,black)
     return textsurface,textsurface.get_rect()



def button(msg , x, y , button_wide , button_height , inact_color , act_color,action):
     mouse = pygame.mouse.get_pos()
          #print(mouse)
     click = pygame.mouse.get_pressed()
     
     
     if x+100 > mouse[0] > x and y+50 > mouse[1] > y :           
       pygame.draw.rect(gameDisplay,act_color,(x,y,button_wide,button_height))
       if click[0] == 1 :  
            if action == "play" :
                 game_loop()
            elif action == "quit":
                 pygame.quit()
                 quit()
            elif action == "unpaused":
                unpaused()


            

     else :            
       pygame.draw.rect(gameDisplay,inact_color,(x,y,button_wide,button_height))
         
               
     smalltext = pygame.font.Font("freesansbold.ttf",20)
     textsurf,textrect = text_object(msg , smalltext)
     textrect.center = ((x+50),(y+25))
     gameDisplay.blit(textsurf,textrect)
     
  



##################################################################
##################################################################
def unpaused():
     global pause
     pause = False
 
     
 
def paused():
     
     while pause :
          color_red = random.randrange(5,253)
          color_blue = random.randrange(5,253)
          color_green = random.randrange(5,253)
          color_r = (color_red,color_blue,color_green)
          white = (56,78,207)
          for event in pygame.event.get() :
               if event.type == pygame.QUIT :
                    pygame.quit()
                    quit()
          gameDisplay.fill(white)
          largetext = pygame.font.Font('freesansbold.ttf',80)
          textsurf, textrect = text_object('''  PAUSE  ''',largetext)
          textrect.center = (400,300)
          gameDisplay.blit(textsurf,textrect)


          b_red = (255,0,0); b_green = (0,255,0)
          red = (150,0,0) ; green = (0,155,0)

          button("   CONTINUE", 300,500,120,50 ,green , b_green,"unpaused")
          button(" QUIT ", 800,500,100,50 ,red , b_red,"quit")
          
          pygame.display.update()
          clock.tick(15)


###################################################################################                                                                                     
###################################################################################     




def intro():
     
     while True :
          color_red = random.randrange(5,253)
          color_blue = random.randrange(5,253)
          color_green = random.randrange(5,253)
          color_r = (color_red,color_blue,color_green)
          white = (56,78,207)
          for event in pygame.event.get() :
               if event.type == pygame.QUIT :
                    pygame.quit()
                    quit()
          gameDisplay.fill(white)
          largetext = pygame.font.Font('freesansbold.ttf',50)
          textsurf, textrect = text_object('''This is car game''',largetext)
          textrect.center = (400,300)
          gameDisplay.blit(textsurf,textrect)


          b_red = (255,0,0); b_green = (0,255,0)
          red = (150,0,0) ; green = (0,155,0)

          button(" START ", 300,500,103,50 ,green , b_green,"play")
          button(" QUIT ", 800,500,100,50 ,red , b_red,"quit")
          
          pygame.display.update()
          clock.tick(15)



def car(x,y):
     gameDisplay.blit(gameimg,(x,y))
     gameDisplay.blit(bound,(0,0))



def things(thingx,thingy,thingw,thingh,color): #making thinga to crash
     pygame.draw.rect(gameDisplay,color, [thingx,thingy,thingw,thingh])

def thing_dodge(count):
     blue = (50,230,60)
     font = pygame.font.Font('freesansbold.ttf',25)
     text = font.render("Dodged : "+str(count),True,blue)
     gameDisplay.blit(text,(0,0))

     

def message_display (text) :
     largetext = pygame.font.Font('freesansbold.ttf',50)
     textsurf, textrect = text_object(text,largetext)
     textrect.center = (400,300)
     gameDisplay.blit(textsurf,textrect)
     pygame.display.update()
     time.sleep(2)
     game_loop()


     
def crash() :
     global m_s
     m_s += 1
     if m_s > 3 :
          print("if")
          time.sleep(2)
          import dave_ball
     message_display('you crashed %d times '%m_s )
     
     



def game_loop():
     x = (1200 * 0.5)
     y = (600 * 0.80)
     xc = 0
     x_change = 0
     thing_startx = random.randrange(40,1200)
     thing_y = -100
     thing_speed = 5
     thing_wide = 100
     thing_height = 100
     global pause
     
     doged = 0
     
     white = (255,255,255)
     crashed = False #to stop a game
           
     while not crashed :
          color_red = random.randrange(5,253)
          color_blue = random.randrange(5,253)
          color_green = random.randrange(5,253)
          color_r = (color_red,color_blue,color_green)
          for event in pygame.event.get(): 
               if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                 
               if event.type == pygame.KEYDOWN :
                 if event.key == pygame.K_LEFT :
                    xc = -15
                 elif event.key == pygame.K_RIGHT :
                      xc = 15
                 if event.key == pygame.K_p :
                    pause = True   
                    paused()
                 
               if event.type == pygame.KEYUP :
                  if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT :
                       xc = 0
                
               
                    
          x += xc          
          gameDisplay.fill(white)
          things(thing_startx,thing_y,thing_wide,thing_height,color_r)
          #def things(thingx,thingy,thingw,thingh,color)
          thing_y += thing_speed 
          car(x,y)
          thing_dodge(doged)
          
          if x < 34 or x > 1150 : # making boundaries
               crash()
          if thing_y > 900 :
               thing_y -= 910
               thing_startx = random.randrange(20,1230)
               doged += 1
               thing_speed += 1
               thing_wide += (doged * 1.2)
               ####(y < thing_y + thing_height) or ( y + 327 > 700)
          if   y < thing_y + thing_height < y + 131:
               if ( x > thing_startx and x < thing_startx + thing_wide) or (x + 71 > thing_startx and x + 71 < thing_startx + thing_wide) or (x + 35 > thing_startx and x + 35 < thing_startx + thing_wide) : 
                   crash()

          pygame.display.update() 
          clock.tick(60) 

intro()
game_loop()
pygame.quit()
quit()
     

s
