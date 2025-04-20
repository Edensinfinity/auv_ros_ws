I first just copied what was there in previous question with the necessary changes to package names.\
Then, I added edge detection functionality.\
Then, I found out that I can send the image as an Image type by importing it from sensor_msgs.msg \
So, I changed the code to a ROS format, adding in the rosnode and publisher, etc.\
I tried publishing the frame directly, but that didn’t work.\
I found out that I had to use CVBridge, to convert the frame to a ROS Image Message.\
Then, I made the subscriber node, and used CVBridge again to convert the ROS Image Message back into a CVimage which I could then show using the same commands as q4.
