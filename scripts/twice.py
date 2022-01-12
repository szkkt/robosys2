#!/usr/bin/env python3

import rospy
import math
from std_msgs.msg import Int32

m = 0
def cb(message):
    global m
    m = math.sqrt(message.data)
    #rospy.loginfo(message.data)
    for i in range(2,message.data):
        if message.data % i == 0:
            rospy.loginfo(message.data)
            return
        #if message.data % i ==0:
         #   rospy.loginfo('so')
          #  return

rospy.init_node('twice')
sub = rospy.Subscriber('count_up', Int32, cb)
rospy.spin()

