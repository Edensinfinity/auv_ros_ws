To get familiar I tried watching a few videos on OpenCV, but they seemed to deal with just regular getting the image and displaying, without using depthai, etc. \
Since the question doesn’t really specify it to be a stereo camera, I assumed its a regular colour camera first and tried to display that. \
I looked at the Luxonis documentation for pipelines, nodes, color camera, XLinkOut and RGB Scene. \
\
So first I make the colorcamera node and the XLinkOut node (for returning the image to host).\
I figured that since we only need to show camera output, a XLinkIn (for getting commands from the host) is not required.\
Then I started the pipeline with a video queue.\
Then infinitely, frame tries to get an image from the videoqueue, and when it is present, cv2.imshow, shows the frame.\
But before that I had to use getCvFrame(), to convert the raw videoIn into numpy array that OpenCV can use. Initially, I tried to just show the raw videoIn and it did not work.\
Finally cv2.waitKey(1) gives a delay so that we dont fry our cpu, and so that there is enough time to process the image.\
