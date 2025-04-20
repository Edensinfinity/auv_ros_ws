#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64

def int_callback(num2):
    num3=int(num2.data)+5
    rospy.loginfo(num3)
    

if __name__ == '__main__':
    rospy.init_node("sub2")
    sub = rospy.Subscriber("/topic2", Int64, callback=int_callback)
    rospy.spin()