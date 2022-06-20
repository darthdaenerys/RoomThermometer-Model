# import packages and libraries
from vpython import *
import time
import numpy as np

# vpython canvas
canvas(width=1320,height=680)

# thermometer parameters
tubelength=8
tubeoutradius=.18
tubeinradius=.1
sphereinradius=.2
sphereoutradius=.3
platelength=9
platethickness=.4
platewidth=2

# cylinders and spheres
innertube=cylinder(axis=vector(0,1,0),radius=tubeinradius,pos=vector(0,-tubelength/2,0),length=tubelength,color=color.red)
outertube=cylinder(axis=vector(0,1,0),radius=tubeoutradius,pos=vector(0,-tubelength/2,0),length=tubelength,opacity=.25)
innersphere=sphere(radius=sphereinradius,pos=vector(0,-tubelength/2,0),color=color.red)
outersphere=sphere(radius=sphereoutradius,pos=vector(0,-tubelength/2,0),opacity=.25)

attach_light(innersphere)
attach_light(innertube)

# back plate
plate=box(pos=vector(0,0,-.5),size=vector(platewidth,platelength,platethickness),texture=textures.wood)
tubeholder1=ring(pos=vector(0,tubelength-5.2,0),axis=vector(0,1,0),thickness=.05,radius=.2)
tubeholder2=ring(pos=vector(0,-tubelength+5.2,0),axis=vector(0,1,0),thickness=.05,radius=.2)
holdercylinder1=cylinder(pos=vector(0,tubelength-5.2,-.5),axis=vector(0,0,1),radius=.1,size=vector(.3,0,0))
holdercylinder2=cylinder(pos=vector(0,-tubelength+5.2,-.5),axis=vector(0,0,1),radius=.1,size=vector(.3,0,0))

text(text=str('C'),color=color.black,pos=vector(-.5,tubelength-4.5,-.3),align='center',height=0.4)
text(text=str('F'),color=color.black,pos=vector(.5,tubelength-4.5,-.3),align='center',height=0.4)

# celsius scale
cntr=-20
for i in np.linspace(-tubelength+5,tubelength-5.4,16):
    text(text=str(cntr),pos=vector(-.5,i,-.3),color=color.black,align='center',height=0.2)
    box(pos=vector(-.18,i,-.3),color=color.black,size=vector(.25,.05,.05))
    cntr+=5

# fahrenheit scale
cntr=0
for i in np.linspace(-tubelength+5.04,tubelength-5.44,14):
    text(text=str(cntr),pos=vector(.5,i,-.3),color=color.black,align='center',height=0.2)
    box(pos=vector(.18,i,-.3),color=color.black,size=vector(.25,.05,.05))
    cntr+=10

while True:
    
    # change ypos
    for ypos in np.linspace(1,7,100):
        rate(30)
        innertube.length=ypos
    for ypos in np.linspace(7,1,100):
        rate(30)
        innertube.length=ypos