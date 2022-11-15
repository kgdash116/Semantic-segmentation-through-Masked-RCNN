# Semantic-segmentation-through-Masked-RCNN
Note:This works for videos as well, a test video is added for testing. This works equally well with webcams too.
For webcam usage just replace the "test.mp4" in Videocapture with 0.

In this project Semantic Segmentation is conducted using a Masked RCNN model and through trained COCO weights.

The test image is given as follows:
![image](https://user-images.githubusercontent.com/101527504/201783154-bb3af4ae-d660-4d34-8ed9-2c37e4f574ea.png)

A horizontal concatenated view is presented on which the left side depicts the detected objects with bounding boxes drawn over them, and the image on the right
is the masks that segment the object.
![image](https://user-images.githubusercontent.com/101527504/201783481-2d97e8f8-0602-4949-a991-cb5e4e4d97e3.png)


The output of the model is such that it displays bounding boxes over the detected objects as well as a mask segmenting the detected object from the background.
The output is given as follows, it is represented as an overlay of the masks over the original image:

![image](https://user-images.githubusercontent.com/101527504/201783453-9468b5a3-a56c-4a8e-ba10-7afeb9ddc7e6.png)
