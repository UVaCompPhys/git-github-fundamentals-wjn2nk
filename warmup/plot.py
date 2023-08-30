# This is a sample Python script.
from math import pi
import math

import matplotlib.pyplot as plt
import numpy as np

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#n = float(input("Enter the number of dimensions: "))
#rad = float(input("Enter the radius: "))

#v = ((pi**(n/2))/(math.gamma((n/2) + 1)))*rad**n;

#print("Volume: ", v)

def volume(n, r):
    return ((pi**(n/2))/(math.gamma((n/2) + 1)))*(r**n)


# make data
r = np.linspace(0, 2, 20)
v = volume(5, r)

# plot
fig, ax = plt.subplots()

ax.plot(r, v, linewidth=2.0)

ax.set(xlim=(0, 2), xticks=np.arange(0.25, 2, 0.25),
       ylim=(0, 200), yticks=np.arange(0, 220, 20))

ax.set_ylabel('Volume')
ax.set_xlabel('Radius')
ax.set_title('Volume vs Radius of a Five Dimensional Sphere')
ax.grid(True)

fig.savefig("5d.png")
plt.show()

