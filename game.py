import pygame
import sys
from pygame.locals import *
# from Function import limit

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("C:\code_write\pygame\k\mm_shot.mp3")
pygame.mixer.music.play(-1)
music_shot =pygame.mixer.Sound("C:\code_write\pygame\k\music_shot2.mp3")
Disscreen =pygame.display.set_mode((1400,600))
pic = pygame.image.load
Ima = pic("C:\code_write\pygame\pic\Fire.girl.2.jpg")
Ima_2 = pic("C:\code_write\pygame\pic\p.long.jpg")
React = Ima.get_rect()
draw = Disscreen.blit
x= 100
y= 400
px=0
py=0
acce=0
p=1
n=x
m=y-28
a3=0
text =""
a4=1
a5=0
a6=0
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # py=0
    # move()
    # x=x+vx
    # y=y+vy

    Press = pygame.key.get_pressed()
    if Press[K_k] and p :
       py =-10
       p=0
       a5+=1
    if not Press[K_k] and p==0:
        # if p==0:
            p=1
        # py=py+1
        # p=0
        # print(2)
    if a5==2:
        p=0
    if Press[K_d]:
        x=x+6
        Ima = pic("C:\code_write\pygame\pic\Fire.girl.2.jpg")
        a4=1
    if Press[K_a]:
        x-=6
        Ima = pic("C:\code_write\pygame\pic\Fire.girl.1.jpg")
        a4=2
    # jump()
    x=x+px
    y=y+py   
    py=py-acce 
    # print(1)
    if y<400 and py >=0:       
        acce=-1
    elif y<400 and py<0:
        acce=-0.5   
    if y>=400:
        y=400
        acce=0
        py=0
        p=1
        a5=0
        # p=1 
    React.center = (x,y)
    # if not Press[K_j]:
    #     text =""
    #     n=x
    if Press[K_j] :
        text = "___"
        a6+=1
        if a6>=10:
            music_shot.play()
            a6=0
        # p=0
        if a4==1:                                                                                         
            a3=100
        elif a4==2:
            a3=-100
        if n>=1400 or n<=0:
            n=x
            m=y-28
    
    Text_shot = pygame.font.Font(None,50).render(text,True,(206,180,50)) 
    
    Disscreen.fill((0,0,0))
    draw(Ima_2,(0,0))
    n+=a3
    m=y-28
    draw(Text_shot,(n,m))
    # draw(Ima,(x,y)) 
    draw(Ima,React)

    pygame.display.update()
    pygame.time.Clock().tick(60)
    
