# Project 1 — AR Workspace Focus Assistant

## Goal

Build a deployable real-time computer vision application that helps users stay focused while studying or working.

The application runs entirely locally after deployment and is controlled through gestures instead of mouse/keyboard.

This project should demonstrate:

* CNN understanding
* Object detection
* Transfer learning
* Deployment
* Product thinking
* Computer vision integration

---

# Product Flow

Open App

↓

Camera Opens

↓

User Starts Session Using Gesture

↓

Workspace Scan

↓

Dashboard Overlay Appears

↓

User Interacts Through Gestures

↓

Phone Detection Starts Countdown

↓

Alarm (if distraction persists)

↓

Gesture Ends Session

↓

Session Saved

---

# Core Features

## Object Detection

Bounding-box based detection.

Classes:

* person
* phone
* laptop
* book
* bottle
* keyboard
* mouse

Behavior:

* Show boxes during initial scan
* Hide stable boxes afterward
* Continue detecting internally
* Show only:

  * new objects
  * phone
  * alerts

---

## Gesture Controls

Supported gestures:

* Point → move cursor
* Air Tap → click
* Pinch Hold → draw / drag
* Swipe Left → previous panel
* Swipe Right → next panel
* Open Palm → pause/menu

No additional gestures in V1.

---

## Dashboard

Overlay directly on camera.

Fixed layout.

Panels:

### Session

* timer
* focus score
* session state

### Drawing

* draw
* erase
* save for current session only

### Alerts

* distraction state
* dismiss alarm

---

## Focus Logic

Session start:

* manual
* gesture only

Distraction:

Phone visible

↓

Countdown starts

↓

Phone removed:

* YES → reset countdown
* NO → trigger alarm

Alarm:

* sound
* visual
* dismiss using gesture

---

# ML Strategy

Object detector:

Pretrained lightweight backbone

*

Custom detection head

*

Partial backbone fine-tuning

Training:

* Colab / free GPU

Deployment:

* trained model only

Users never train.

---

# Deployment

No backend.

Inference runs locally.

Training and deployment are separate phases.

Target order:

Desktop deployment first.

Website deployment later.

---

# Explicitly Excluded

Do not implement:

* gender classification
* speed estimation
* face recognition
* pose estimation
* voice interaction
* cloud backend
* dynamic dashboard
* full training from scratch
* huge detector
* tracking IDs
* multi-user mode

---

# Success Criteria

A recruiter should conclude:

"This person can train, integrate, optimize, and deploy computer vision systems."