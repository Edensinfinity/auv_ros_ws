#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from task0_q3.msg import bot_pose

def string_callback(msg):
    rospy.loginfo("X: %s, Y: %s, Orientation: %s",msg.x,msg.y,msg.orientation)

if __name__ == '__main__':
    rospy.init_node("subscriber")
    sub = rospy.Subscriber("/path_topic", bot_pose, callback=string_callback)
    rospy.spin()