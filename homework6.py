import pylab as pl 
import math


timestep=0.01
g=9.8
l=1
angle=0.2
time=0
q=1
D=2
F=0.2
deltaang=0

w=0

Ang=[]
totaltime=[]
wt=[]
logang=[]
Delta=[]

Ang.append(angle)
totaltime.append(time)
wt.append(w)
logang.append(0)
Delta.append(0)

while time<100:
	deltalog=0
	ww=w
	w=ww-((g/l)*math.sin(angle)+q*ww+F*math.sin(D*time))*timestep
	angle=angle+w*timestep
	delta=w*timestep
	if angle>math.pi:
		angle-=2*math.pi
	if angle+math.pi<0:
		angle+=2*math.pi
	time+=timestep
	totaltime.append(time)
	Ang.append(angle)
	wt.append(w)
	Delta.append(delta)
	if w!=0:
		deltalog=math.log10(abs(w*timestep))
	if w!=0:
		logangle=math.log10(abs(w*timestep))
	else :
		logangle=math.log10(abs(ww*timestep))
	logang.append(logangle)


pl.plot(totaltime,logang,'r')
pl.xlabel('time')
pl.ylabel('log')
pl.show