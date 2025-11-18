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
