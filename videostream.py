import cv2
import numpy as np

model_path='frozen_inference_graph_coco.pb'
config_file_path='mask_rcnn_inception_v2_coco_2018_01_28.pbtxt'
colors=np.random.randint(125,255,(80,3))

#image=cv2.imread('image.png')
cap=cv2.VideoCapture('test.mp4')
while True:
    ret,frame=cap.read()
    #load the model and the configuration file
    model=cv2.dnn.readNetFromTensorflow(model_path,config_file_path)
    #resize the image
    img=cv2.resize(frame,(650,650))
    #extract the dimensions through the shape
    height,width,channels=img.shape
    #create the background image, essentially an image that has the same size as our original
    #image
    black_image=np.zeros((height,width,3),np.uint8)
    #select the background image color
    black_image[:]=(0,164,255)

    #Get the blob, we use swapRB because the image for tensorflow is of the RGB format
    blob=cv2.dnn.blobFromImage(img,swapRB=True)
    #set blob as the input
    model.setInput(blob)
    boxes,masks=model.forward(["detection_out_final","detection_masks"])

    #print(boxes.shape) # (1,1,100,7)
    #print(masks.shape)

    number_of_objects=boxes.shape[2]

    #getting details of the box

    for i in range(number_of_objects):
        box=boxes[0,0,i]
        class_id=box[1]
        score=box[2]
        if score<0.5:
            continue
        x=int(box[3]*width)
        y=int(box[4] * height)
        x2=int(box[5] * height)
        y2=int(box[6] * height)
        #draw a rectangular bounding box over the detected object
        cv2.rectangle(img,(x,y),(x2,y2),(255,0,0),3)
        #generate rois of the objects detected on the plain black image
        roi=black_image[y:y2,x:x2]
        roi_height,roi_width,_=roi.shape
        mask=masks[i,int(class_id)] #hold the mask in the mask variable
        mask=cv2.resize(mask,(roi_width,roi_height))
        ret,mask=cv2.threshold(mask,0.5,255,cv2.THRESH_BINARY)
        #cv2.imshow('black image',)
        #cv2.waitKey(0)==ord('q')
        #cv2.destroyAllWindows()
        contours,_=cv2.findContours(np.array(mask,np.uint8),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        color=colors[int(class_id)]
        for cnt in contours:
            cv2.fillPoly(roi,[cnt],(int(color[0]),int(color[1]),int(color[2])))
    cv2.imshow("Final",np.hstack([img,black_image]))
    overlay_frame = ((0.5*black_image)+(0.5*img)).astype("uint8")
    cv2.imshow("Overlay Frame", overlay_frame)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

