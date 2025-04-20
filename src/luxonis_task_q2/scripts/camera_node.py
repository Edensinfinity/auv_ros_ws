import rospy
import depthai as dai
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

if __name__ == '__main__':
    rospy.init_node('image_publisher', anonymous=True)
    img_pub=rospy.Publisher("/camcolour",Image,queue_size=10)
    pipeline=dai.Pipeline()
    cam=pipeline.create(dai.node.ColorCamera)
    cam.setPreviewSize(300, 300)
    cam.setBoardSocket(dai.CameraBoardSocket.CAM_A)
    cam.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
    cam.setInterleaved(False)
    cam.setColorOrder(dai.ColorCameraProperties.ColorOrder.RGB)

    xOut = pipeline.create(dai.node.XLinkOut)
    xOut.setStreamName("camOut")
    # Here we will send camera preview (ImgFrame) to the host via XLink.
    # Host can then display the frame to the user
    cam.preview.link(xOut.input)

    with dai.Device(pipeline) as device:
        videoqueue=device.getOutputQueue(name="camOut",maxSize=4, blocking=False)
        bridge=CvBridge()
        while not rospy.is_shutdown():
            videoIn = videoqueue.tryGet()
            if videoIn is not None:
                frame=videoIn.getCvFrame()
                ros_image = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
                img_pub.publish(ros_image)
                rospy.sleep(0.1)