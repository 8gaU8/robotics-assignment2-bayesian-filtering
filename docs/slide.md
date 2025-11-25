---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #ffffffff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: "IMLEX Yuya Haga"
header: "Assignment 2: *Object Tracking by Kalman Filter*"
---

<!-- ![bg left:40% 80%](https://marp.app/assets/marp.svg) -->

# **_Object Tracking by Kalman Filter_**

YOLO meets Kalman Filter

![Truck Video width:600px ](./assets/yolo-example.png)

---

# Background

- Object tracking is a fundamental task in computer vision with applications in surveillance, robotics, and autonomous vehicles.
- However, low-computational cost methods are still in demand for real-time applications on resource-constrained devices (edge-computing, IoT...).
- Using lightweight object detection models combined with filtering techniques can provide efficient tracking solutions.

 ***→ YOLO nano + Kalman Filter for efficiency***

---

# Methods

- Object Detection
  - **YOLOv11n**: a lightweight object detection model
  - **input**: video frames
  - **output**: bounding boxes of detected objects for each frame
- Tracking Algorithm
  - **Kalman Filter**
  - **input**: detected bounding boxes
  - **output**: estimated positions of objects over time

---

# Results


<video src="./assets/truck_kf_result_video.mov" controls loop muted autoplay></video>

tracking a moving truck using YOLOv11n and Kalman Filter.


---

# Discussion
- Postprocessing of Detection Results
- Occlusions and Missed Detection
- Multiple Object Tracking

<!-- As shown in the results, the obtained tracking trajectory by the Kalman Filter is smoother than the observation trajectory from the YOLOv11n model. This indicates that the Kalman Filter effectively reduces noise and fluctuations in the observations, resulting in a more stable and accurate tracking of the truck's position over time.

However, this project has some limitations:

1. Multiple Object Tracking: The current implementation only tracks a single truck in the video. In real-world scenarios, there may be multiple trucks or other vehicles present. Extending the Kalman Filter to handle multiple objects would be necessary for practical applications.
2. Occlusions and Missed Detections: In some frames, the YOLOv11n model may fail to detect the truck due to occlusions or other factors. In this project, such cases were completed by linear interpolation before applying the Kalman filter. However, more sophisticated methods for handling occlusions and missed detections could improve tracking performance.
3. Postprocessing of Detection Results: The output of the YOLOv11n model is bounding boxes. In this project, the corner point of the bounding box was used as the observation for the Kalman Filter. However, such a point may not accurately represent the position of the truck. Developing a method to extract more representative points from the bounding boxes could enhance tracking accuracy. -->
