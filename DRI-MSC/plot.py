# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 10:23:34 2021

@author: Mahsa
"""
#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2013-2021 German Aerospace Center (DLR) and others.
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0/
# This Source Code may also be made available under the following Secondary
# Licenses when the conditions for such availability set forth in the Eclipse
# Public License 2.0 are satisfied: GNU General Public License, version 2
# or later which is available at
# https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later

# @file    plot_summary.py
# @author  Daniel Krajzewicz
# @author  Laura Bieker
# @author  Michael Behrisch
# @date    2013-11-11

# import lxml.etree
# # xmlstr is your xml in a string
# root = lxml.etree.fromstring(r'C:\Users\Mahsa\Desktop\Crossroad\Deliver\Code\DRI-MSC\intelligent_lights_output_file.xml')
# results = root.findall('duration')
# print(results)

from xml.dom import minidom
import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]
doc = minidom.parse('output.xml')
staffs = doc.getElementsByTagName("tripinfo")
for staff in staffs:
        simulation_episodes_id = staff.getAttribute("simulation_episodes_id")
        queue_length = staff.getAttribute("queue_length")
        x.append(simulation_episodes_id)
        y.append(queue_length)



fig, ax = plt.subplots()
ax.plot(x,y,color='green', linestyle='dashed', linewidth = 3)
ax.set_xticks([10,20,30, 40,50,60,70,80])
ax.set_xticklabels(['10','20','30','40', '50', '60', '70','80'])
ax.set_yticks([-90, 10, 110, 210, 310,410,510,610])
ax.set_yticklabels(['0','100','200','300', '400', '500', '600','700'])
plt.show()


