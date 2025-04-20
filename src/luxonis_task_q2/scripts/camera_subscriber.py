import rospy
import depthai as dai
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

def image_callback(img):
    image=bridge.imgmsg_to_cv2(img, desired_encoding='bgr8')
    cv2.imshow("Image",image)
    cv2.waitKey(1)                          #To refresh the imshow() window
    rospy.loginfo("Image is shown")

if __name__ == '__main__':
    rospy.init_node("Camera_Subscriber")
    bridge=CvBridge()
    cam_sub = rospy.Subscriber("/camcolour", Image, image_callback)
    rospy.spin()