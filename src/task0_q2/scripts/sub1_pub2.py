#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64

def int_callback(num1):
    num2=Int64(num1.data*10)
    pub.publish(num2)
    

if __name__ == '__main__':
    rospy.init_node("sub1_pub2")
    pub = rospy.Publisher("/topic2", Int64, queue_size=10)
    sub = rospy.Subscriber("/topic1", Int64, callback=int_callback)
    rospy.spin()