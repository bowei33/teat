#! /usr/bin/env python
import rospy
rospy.init_node("lesson2")

for i in range(1,10):
    for j in range(1,10):
        print('%d*%d=%2ld'%(i,j,i*j),end=' ')
    print()
