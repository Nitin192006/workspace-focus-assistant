# ML Plan

## Objective

Train a lightweight real-time object detector for the Workspace Focus Assistant.

---

# Framework

PyTorch

TorchVision Detection API

---

# Detector

SSDLite

---

# Backbone

MobileNetV3 Large

---

# Training Strategy

Pretrained backbone

↓

Replace detection head

↓

Fine-tune backbone

---

# Dataset

Microsoft COCO

Classes:

- person
- cell phone
- laptop
- book
- bottle
- keyboard
- mouse

No manual data collection.

---

# Compute

Google Colab (Free GPU)

---

# Export

PyTorch

↓

ONNX

↓

ONNX Runtime

---

# Deployment

Local inference.

No backend.

---

# Success Metrics

- Stable training
- Good mAP
- Real-time inference
- Small model
- Easy deployment

---

# Project Philosophy

The objective is not to obtain the highest possible benchmark score.

The objective is to build, understand, train, evaluate, optimize, and deploy an end-to-end computer vision system suitable for real-world usage and portfolio demonstration.