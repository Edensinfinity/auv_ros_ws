My approach was to try to make a publisher and a subscriber that refer to the same rostopic within the same rosnode. \
First, I ran into an issue because my subscriber was the one that was publishing the next msg but without any initial msg in the topic the subscriber would never get input and ask for the next msg. \
So, I tried to publish an initial msg into the topic before defining my Subscriber but that did not work. \
After some thinking, I found out that if there is no subscriber connected to a rostopic, the msg will not persist and will be lost. \
So, I tried publishing the initial msg after defining my Subscriber but that also did not work, because I did not put a rospy.sleep() statement in between to let the subscriber properly finish. \
Once I put the rospy.sleep() it worked. \
\
Version 1: I have written a node that will get input of who it is that is talking and what their message is, since we cannot run the same node in two terminals getting who is talking at any moment is necessary. \
\
Final Version: By Adding 1 or 2 to the beginning of your message, we figure out whether Jolyne is talking or Joestar.
