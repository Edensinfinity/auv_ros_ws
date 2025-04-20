#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def string_callback(msg2: String):
    rospy.loginfo(msg2)
    person=input("Enter your name: ")
    message=input("Enter your message: ")
    msg=person+": "+message
    pub.publish(msg)
    

if __name__ == '__main__':
    rospy.init_node("chatnode")
    msg1="Chat Node has started"
    pub = rospy.Publisher("/chat_topic", String, queue_size=10)
    sub = rospy.Subscriber("/chat_topic", String, callback=string_callback)
    rospy.sleep(1)          #Gives time for subscriber to finish setting up
    pub.publish(msg1)
    rospy.spin()