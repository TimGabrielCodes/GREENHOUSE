from time import sleep, time
import matplotlib.pyplot as plt
    
import matplotlib.animation as animation
import random
from matplotlib import style
from datetime import datetime
 
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
xs = []
ys = []
i=0

def updateChart(y,x):
    
    # xs.append(float(x))
    xs.append(x)
    ys.append(float(y))
    ax1.clear()
    
    ax1.plot(xs, ys) 
  
    
    
def animate(data):
    # print("data to plot {%f}", data)
    updateChart(data, datetime.now())     
 
    # print(xs)  
    # print(ys)
    
    
     
while (i<100):
    
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()
    xs.clear()
    ys.clear()
   
    # print("Na Ment!!!")
    i+=1
    sleep(2)
 
