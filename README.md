# 🇮🇳 Indigenous Body Tracker

**Atmanirbhar AI - Made in India, for India.**

Lightweight, real-time YOLOv11 pose estimation model (17 keypoints) that runs at 40ms on any laptop CPU. No cloud, no GPU, no foreign dependency.

![License: MPL 2.0](https://img.shields.io/badge/License-MPL_2.0-brightgreen.svg)
![YOLOv11](https://img.shields.io/badge/Model-YOLOv11n--Pose-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-yellow)
![Made in India](https://img.shields.io/badge/Made%20in-India-orange.svg)

### Why Indigenous AI?

Indigenous AI ensures data sovereignty, cultural relevance, and true self-reliance. Built for Indian conditions, it runs efficiently on low-cost hardware without dependence on foreign black-box models. It is frugal, open, and made for Bharat — by Bharat.

### ⚡ Performance (Laptop CPU - Intel i5)

| Image Size | Speed | FPS | Use Case |
| :--- | :--- | :--- | :--- |
| 160 | ~40ms | 25 FPS | Real-time (Recommended) |
| 320 | ~150ms | 7 FPS | Balanced |
| 640 | ~250ms | 4 FPS | High Accuracy |

*ONNX is 3x faster than PyTorch.*

### 🎯 What it Detects

17 COCO keypoints: nose, eyes, ears, shoulders, elbows, wrists, hips, knees, ankles.

### 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/Indigenous-Body-Tracker.git
cd Indigenous-Body-Tracker
pip install -r requirements.txt
