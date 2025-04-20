#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def string_callback(msg2: String):
    rospy.loginfo(msg2)
    message=input("")
    if(message[0]=='1'):
        person="Jolyne"
    elif(message[0]=='2'):
        person="Joestar"
    try:
        msg=person+": "+message[1:]
        pub.publish(msg)
    except:
        msg="Entered Unsupported Text Format"
        pub.publish(msg)
    

if __name__ == '__main__':
    rospy.init_node("chatnode2")
    rospy.loginfo("Chat node has started")
    msg1="In the beginning of any message, Jolyne - Enter '1', Joestar - Enter '2'"
    pub = rospy.Publisher("/chat_topic2", String, queue_size=10)
    sub = rospy.Subscriber("/chat_topic2", String, callback=string_callback)
    rospy.sleep(1)          #Gives time for subscriber to finish setting up
    pub.publish(msg1)
    rospy.spin()