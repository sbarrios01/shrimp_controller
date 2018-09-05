import math
import time
import random
import numpy
from shrimp_red import red
import shrimp_observer
from shrimp_postprocess import post
import shrimp_control
from shrimp_serial import shrimp2serial

serial = shrimp2serial()
referenceData = list (math.floor(math.cos(((2*math.pi)/127)*i)*127) for i in range (0,255))
#inputData = list (math.floor((math.sin(((2*math.pi)/127)*i)*(1.0+(random.random()-0.5)/10))*127) for i in range (0,255))
inputData=[]
outputData=[]
random.seed()
x1=[]
x2=[]
red_x1 = red()
red_x2 = red()
G1 = 0.1
G2 = 2
wZ_12_1 = []
wZ_12_2 = []
T = 0.00001#Cambiar por el periodo
x2refk1 = []
u = []
postP = post()
postP.max=67000
for i in range (0,255):
	print (referenceData[i], end=' ', flush=True)
	#x1.append((inputData[i]*2*math.pi)/5504)
	#x2.append(((inputData[i]/5588)*12)/8.71)
print("---------------------")
for s in range (0,1):
	for i in range (0,255):
		inputData.append(serial.read())
		x1.append((inputData[i]*2*math.pi)/5504)
		x2.append(((inputData[i]/5588)*12)/8.71)
		wZ_12_1.append(red_x1.step(x1[i],[x1[i],x2[i]],x2[i],G1))
		wZ_12_2.append(red_x2.step(x2[i],[x1[i],x2[i]],0.5,G2)) #Cambianr 0.5 por u
		x2refk1.append(shrimp_observer.observe(T,referenceData[i],wZ_12_1[i]-referenceData[i],wZ_12_1[i]))#Add delays
		u.append(shrimp_control.control(numpy.array([[wZ_12_1[i]],[wZ_12_2[i]]]),numpy.array([[referenceData[i]],[x2refk1[i]]])))
		outputData.append(postP.postprocess(u[i][1,1]))
		#outputData.append((inputData[i]*2)-((referenceData[i])))
		serial.write(outputData[i])
		print (outputData[i], end=' ', flush=True)
		
		time.sleep(1/10)
		
serial.close()
		