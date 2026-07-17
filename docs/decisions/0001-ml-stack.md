# ADR-0001: Machine Learning Stack

## Status

Accepted

## Context

The project requires a lightweight real-time object detector that can be trained using free cloud GPUs, deployed locally, and later exported for web deployment.

The solution should maximize learning, deployment feasibility, and resume value while remaining achievable on limited compute.

## Decision

Framework:
- PyTorch
- TorchVision Detection API

Detector:
- SSDLite

Backbone:
- MobileNetV3 Large

Training:
- Partial backbone fine-tuning

Dataset:
- Microsoft COCO (filtered to project classes)

Export:
- ONNX

Runtime:
- ONNX Runtime

## Consequences

### Positive

- Lightweight
- Fast inference
- Easy deployment
- Official PyTorch ecosystem
- Strong educational value

### Negative

- Slightly lower accuracy than larger detectors
- Limited to lightweight deployment constraints

## Rationale

The chosen stack provides the best balance between engineering complexity, learning value, deployment readiness, and available compute resources.