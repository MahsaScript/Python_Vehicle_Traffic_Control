# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 08:24:13 2021

@author: Mahsa
"""

from xml.dom import minidom
import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]
doc = minidom.parse(r'output.xml')
staffs = doc.getElementsByTagName("tripinfo")
for staff in staffs:
        simulation_episodes_id = staff.getAttribute("simulation_episodes_id")
        queue_length = staff.getAttribute("queue_length")
        x.append(simulation_episodes_id)
        y.append(int(queue_length))

# plt.plot(x,y)
fig, ax = plt.subplots()
ax.plot(x,y,color='red')

# ax.plot([10, 11, 12,13],[700, 600, 500, 400],color='red')
ax.set_xticks([0,25,50,75, 100,125,150,175,200])
ax.set_xticklabels(['0','25','50','75','100', '125', '150', '175','200'])
ax.set_yticks([0, 50, 100, 150, 200, 250, 300 ,350,400])
ax.set_yticklabels(['0','100','150','200', '250', '300', '350','400','450'])
plt.xlabel('Simulation episodes')
plt.title('DRI-MSC')
# naming the y axis
plt.ylabel('Queue length')