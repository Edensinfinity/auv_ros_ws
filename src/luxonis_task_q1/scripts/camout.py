import depthai as dai
import cv2
import numpy as np

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
    while True:
        videoIn = videoqueue.tryGet()
        if videoIn is not None:
            frame=videoIn.getCvFrame()
            cv2.imshow("camOut",frame)
        key=cv2.waitKey(1)
