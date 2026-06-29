# Circle
"""
import turtle
t=tuttle.turtle()
t.speed(3)
t.circle(100)
t.done()
"""
""" 
#Square
import turtle as tl
tl.speed(3)
for i in range(4):
    tl.forward(100)
    t.right(90)
t.done()
"""
"""
# Pickle
import pickle
data={'name':'Rohit',
              'course':'python',
              'Intitution':'live wire'}
with open("data","wb") as file:
    data.pickle.load(file)
print(data)
"""
"""
######## error not module found!!!!!!!!!!!!!!!!!###
# Pywhatkit
import pywhatkit as p
o=p.playonyt("https://www.youtube.com/watch?v=vb72Ot79JrQ")
s=p.search("rocket")
h=p.text_to_handwriting('hello python',save_to='w.png')
se=p.text_speeach("Hello world",save_to="play.mp3")
w=p.info("python programming",lines=3)
wi=p.senwhatmsg_instantly("+9198074XXXX","hello!!!")
wc=p.senwhatmsg("+9198074XXXX","good morning",8,0)
mi=p.sendwhatmsg_to_group_instantly("ABCDIx","hi group!")
mg=p.sendwhatmsg_to_group("ABCDIx","Hello group!",10,30)
si=p.sendwhats_image("+9198074XXXX","photo.jpg",'myimage')


# Pygame
import pygame
pygame.init()
screen=pygame.display.set_mode((600,400))
x=50
running=True
while running:
    screen.fill((255,255,255))
    pygam.draw.circle(screen,(0,0,255),(x,200,30))
    x+=2
    if x>600:
        x=0
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.display.update()
pygame.quit()
""" 
