#!/usr/bin/env python3

import rospy
import math
from std_msgs.msg import Int32

def cb(message):
    for i in range(2,message.data):
        if message.data % i == 0:
            rospy.loginfo(message.data)
            return

rospy.init_node('twice')
sub = rospy.Subscriber('count_up', Int32, cb)
rospy.spin()

