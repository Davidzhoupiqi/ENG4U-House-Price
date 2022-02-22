# Mozilla Public License 2.0
# By David Zhou (ShixYuu Mafuyuu)
# Designed for DSM Linux System

import matplotlib.pyplot as plt
import numpy as np
import math

M = float(input("The price of Houseing NOW: ")) 
k = float(input("The increased on houseing price per year: ")) 
S = float(input("The Average Salary per Year: ")) 
YS = int(input("How many years you want to plot: "))
fig, ax = plt.subplots()
x = np.arange(-1,YS,1)

y1  = M*(1+k)**(x-1)
y2  = S*x
ax.plot(x,y1,label='The price of housing')
ax.plot(x,y2,label='Your wealth')
ax.legend()
plt.show()