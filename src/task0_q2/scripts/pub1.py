#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64

if __name__ == '__main__':
    rospy.init_node("pub1")
    pub = rospy.Publisher("/topic1", Int64, queue_size=10)
    number = 2
    rate=rospy.Rate(1)
    while not rospy.is_shutdown():
        pub.publish(number)
        number=number*2
        rate.sleep()