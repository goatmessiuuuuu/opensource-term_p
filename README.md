#  **Open Source SW termproject**
#### *Lane Detection*
###### -computer vision technique used to identify and track the lane markings on the road  It plays a crucial role in many applications such as autonomous driving, driver assistance systems, and lane departure warning systems.
---
### **Lane  Detection process** 
#### **: Project that recognizes the direction of lane change in the process of lane change to the left**
![ds](image/image-2323.jpg)
---

>>> ***steps***
: Preprocessing  ->  Region of Interest(ROI) Selection  -> Edge Detection  -> Lane Line Extraction  -> Lane Tracking -> Lane Visualization 
- (1) The input image is preprocessed to enhance relevant features and reduce noise. Common preprocessing techniques include grayscale conversion, Gaussian blurring, and edge detection.
- (2) A region of interest is defined to focus only on the area of the image where the lane markings are expected to appear. This helps reduce computational complexity and false detections.
- (3) Edge detection algorithms, such as the Canny edge detector, are applied to detect the edges of the lane markings. This step helps identify the high-contrast boundaries between the lane and the surrounding road.
- (4) The detected edges are further processed to extract the lane lines. Techniques such as Hough transform or curve fitting can be used to identify and represent the lane lines.
- (5) In order to maintain continuity and robustness, the lane lines are tracked over consecutive frames or video streams. This helps handle variations in lighting conditions, road curvature, and other factors.
- (6) Finally, the detected lane lines are visualized on the original image or video stream to provide a clear indication of the detected lanes.
---
## RESULT
![ds](image/open-source-add.png)
### *Project that recognizes the direction of lane change in the process of lane change to the left*
![ds](image/add2imgimg.png)
---
## document

---

