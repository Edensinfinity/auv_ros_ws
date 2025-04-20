#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from task0_q3.msg import bot_pose

class bot:
    def __init__(self):
        self.pose=bot_pose()
        self.pose.x=0
        self.pose.y=0
        self.pose.orientation="Facing North"
    
    def forward(self):
        if(self.pose.orientation=="Facing North"):
            self.pose.y+=5
        elif(self.pose.orientation=="Facing South"):
            self.pose.y-=5
        elif(self.pose.orientation=="Facing East"):
            self.pose.x+=5
        else:
            self.pose.x-=5

    def backward(self):
        if(self.pose.orientation=="Facing North"):
            self.pose.y-=5
        elif(self.pose.orientation=="Facing South"):
            self.pose.y+=5
        elif(self.pose.orientation=="Facing East"):
            self.pose.x-=5
        else:
            self.pose.x+=5

    def left(self):
        if(self.pose.orientation=="Facing North"):
            self.pose.x-=5
        elif(self.pose.orientation=="Facing South"):
            self.pose.x+=5
        elif(self.pose.orientation=="Facing East"):
            self.pose.y+=5
        else:
            self.pose.y-=5

    def right(self):
        if(self.pose.orientation=="Facing North"):
            self.pose.x+=5
        elif(self.pose.orientation=="Facing South"):
            self.pose.x-=5
        elif(self.pose.orientation=="Facing East"):
            self.pose.y-=5
        else:
            self.pose.y+=5

    def turnleft(self):
        if(self.pose.orientation=="Facing North"):
            self.pose.orientation="Facing West"
        elif(self.pose.orientation=="Facing South"):
            self.pose.orientation="Facing East"
        elif(self.pose.orientation=="Facing East"):
            self.pose.orientation="Facing North"
        else:
            self.pose.orientation="Facing South"

    def turnright(self):
        if(self.pose.orientation=="Facing North"):
            self.pose.orientation="Facing East"
        elif(self.pose.orientation=="Facing South"):
            self.pose.orientation="Facing West"
        elif(self.pose.orientation=="Facing East"):
            self.pose.orientation="Facing South"
        else:
            self.pose.orientation="Facing North"

    def turn180(self):
        if(self.pose.orientation=="Facing North"):
            self.pose.orientation="Facing South"
        elif(self.pose.orientation=="Facing South"):
            self.pose.orientation="Facing North"
        elif(self.pose.orientation=="Facing East"):
            self.pose.orientation="Facing West"
        else:
            self.pose.orientation="Facing East"

if __name__ == '__main__':
    rospy.init_node("publisher")
    pub = rospy.Publisher("/path_topic", bot_pose, queue_size=10)
    rospy.loginfo("Possible Commands: Forward, Backward, Left, Right, Turn Left, Turn Right, Turn 180")
    rate=rospy.Rate(0.1)

    message=bot()
    message.orientation="Facing North"
    while not rospy.is_shutdown():
        command=input("Enter Command: ")
        if(command=="Forward"):
            message.forward()
        elif(command=="Backward"):
            message.backward()
        elif(command=="Left"):
            message.left()
        elif(command=="Right"):
            message.right()
        elif(command=="Turn Left"):
            message.turnleft()
        elif(command=="Turn Right"):
            message.turnright()
        elif(command=="Turn 180"):
            message.turn180()               #Since Turning 180 would require double the time
            rate.sleep()
        else:
            rospy.loginfo("Unrecognized Command")
        rate.sleep()
        pub.publish(message.pose)