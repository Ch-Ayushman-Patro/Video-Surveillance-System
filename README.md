# 🎯 AI & ML Enabled Intelligent Video Surveillance System

A real-time AI-powered video surveillance system that detects suspicious activities using **YOLOv8** object detection, **rule-based behavior analysis**, and displays live alerts on a modern **React** dashboard.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-18+-61DAFB?logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-5+-3178C6?logo=typescript&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00FFFF)

---

## 📋 Table of Contents

- [System Architecture](#-system-architecture)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Running the System](#-running-the-system)
- [API Endpoints](#-api-endpoints)
- [Triple-Lock Logic](#-triple-lock-logic)
- [Demo Script](#-demo-presentation-script)
- [Future Scope](#-future-scope)

---

## 🏗️ System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                    FRONTEND (React + TypeScript)             │
│  ┌────────────┐  ┌──────────────┐  ┌───────────────────┐     │
│  │ VideoFeed  │  │ AlertsPanel  │  │ DetectedObjects   │     │
│  │ (MJPEG)    │  │ (Polling)    │  │ (Polling)         │     │
│  └─────┬──────┘  └──────┬───────┘  └────────┬──────────┘     │
│        │               │                    │                │
└────────┼───────────────┼────────────────────┼────────────────┘
         │               │                    │
    MJPEG Stream    REST /api/alerts    REST /api/frame
         │               │                    │
┌────────┼───────────────┼────────────────────┼────────────────┐
│        │         BACKEND (FastAPI)          │                │
│  ┌─────▼─────────────────────────────────────▼─────┐         │
│  │              API Layer (routes.py)              │         │
│  │  /upload  /start  /stop  /status  /video_feed   │         │
│  └─────────────────────┬───────────────────────────┘         │
│                        │                                     │
│  ┌─────────────────────▼───────────────────────────┐         │
│  │          Video Processor (Pipeline)             │         │
│  │                                                 │         │
│  │  ┌──────────┐  ┌───────────┐  ┌──────────────┐  │         │
│  │  │  YOLOv8  │→ │  Tracker  │→ │  Behavior    │  │         │
│  │  │ Detector │  │ (Centroid)│  │  Analyzer    │  │         │
│  │  └──────────┘  └───────────┘  └──────┬───────┘  │         │
│  │                                      │          │         │
│  │                              ┌───────▼───────┐  │         │
│  │                              │ Alert Manager │  │         │
│  │                              │ + Snapshots   │  │         │
│  │                              └───────────────┘  │         │
│  └─────────────────────────────────────────────────┘         │
│                                                              │
│  Video Input: Uploaded .mp4/.avi/.mkv files                  │
└──────────────────────────────────────────────────────────────┘
```

---

## ✨ Features

### AI & Detection
- **YOLOv8 Object Detection** — Detects persons, bags, knives, and other surveillance-relevant objects
- **Centroid-Based Tracking** — Assigns persistent IDs to objects across frames
- **Loitering Detection** — Alerts when a person stays too long in the scene
- **Intrusion Detection** — Alerts when a person enters a restricted zone
- **Unattended Object Detection** — Alerts when a bag is left without a nearby person
- **Triple-Lock Logic** — Multi-layer verification (Detection → Behavior → Face ID placeholder)

### Dashboard
- **MJPEG Live Video Feed** — Real-time processed video with overlays
- **Drag & Drop Video Upload** — Upload surveillance videos directly from the browser
- **Alert Panel** — Severity-coded alerts with timestamps and snapshot links
- **Detected Objects Panel** — Live tracked objects with confidence bars
- **Stats Bar** — FPS, object count, alert count, uptime
- **Dark Theme** — Modern glassmorphism UI with animations

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **AI/ML** | YOLOv8 (Ultralytics), OpenCV |
| **Backend** | Python 3.10+, FastAPI, Uvicorn |
| **Frontend** | React 18, TypeScript, Vite |
| **Communication** | REST API + MJPEG Streaming |

---

## 📁 Project Structure

```
Video-Surveillance-System/
├── backend/
│   ├── app.py                      # Entry point → starts server
│   ├── requirements.txt            # Python dependencies
│   ├── .env                        # Configuration
│   ├── app/
│   │   ├── main.py                 # FastAPI app factory
│   │   ├── config.py               # Settings from .env
│   │   ├── api/
│   │   │   └── routes.py           # All REST endpoints
│   │   ├── core/
│   │   │   ├── detector.py         # YOLOv8 detection wrapper
│   │   │   ├── tracker.py          # Centroid-based tracker
│   │   │   └── behavior.py         # Rule-based behavior analysis
│   │   ├── services/
│   │   │   ├── video_processor.py  # Video pipeline orchestrator
│   │   │   └── alert_manager.py    # Alert generation & storage
│   │   ├── models/
│   │   │   └── schemas.py          # Pydantic data models
│   │   └── utils/
│   │       └── drawing.py          # OpenCV drawing helpers
│   ├── snapshots/                  # Alert screenshots (auto-created)
│   └── uploads/                    # Uploaded videos (auto-created)
│
├── frontend/
│   ├── src/
│   │   ├── App.tsx                 # Root component
│   │   ├── index.css               # Design system
│   │   ├── types/index.ts          # TypeScript interfaces
│   │   ├── hooks/usePolling.ts     # Polling hook
│   │   └── components/
│   │       ├── Dashboard.tsx       # Main layout
│   │       ├── VideoFeed.tsx       # Video display + upload
│   │       ├── AlertsPanel.tsx     # Alert list
│   │       ├── DetectedObjects.tsx # Object cards
│   │       └── StatsBar.tsx        # Live statistics
│   ├── vite.config.ts
│   └── package.json
│
└── README.md
```

---

## 📦 Prerequisites

| Tool | Version | Installation |
|------|---------|-------------|
| **Python** | 3.10+ | [python.org](https://www.python.org/downloads/) |
| **Node.js** | 18+ | [nodejs.org](https://nodejs.org/) |
| **Git** | Any | [git-scm.com](https://git-scm.com/) |

> **No GPU required.** YOLOv8 nano model runs on CPU. GPU (CUDA) is auto-detected if available.

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Video-Surveillance-System.git
cd Video-Surveillance-System
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

> The YOLOv8 model (~6MB) will auto-download on first run.

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install
```

### 4. Configuration (Optional)

Edit `backend/.env` to customize:

```env
YOLO_MODEL=yolov8n.pt           # Model size (n/s/m/l/x)
YOLO_CONFIDENCE=0.5             # Detection threshold
LOITERING_THRESHOLD_SECONDS=30  # Loitering time
INTRUSION_ZONE=0.6,0.0,1.0,1.0  # Restricted zone area
```

---

## ▶️ Running the System

### Terminal 1 — Backend

```bash
cd backend
venv\Scripts\activate    # Windows
python app.py
```

Server starts at: **http://localhost:8000**
Swagger Docs at: **http://localhost:8000/docs**

### Terminal 2 — Frontend

```bash
cd frontend
npm run dev
```

Dashboard opens at: **http://localhost:5173**

### Using the System

1. Open **http://localhost:5173** in your browser
2. **Upload a video** — drag & drop or click the upload area
3. Processing starts automatically — watch the live feed
4. **Alerts** appear in the right panel when suspicious behavior is detected
5. Click **📸 Snapshot** on any alert to see the captured frame

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/upload` | Upload video file and start processing |
| `POST` | `/api/start` | Start processing last uploaded video |
| `POST` | `/api/stop` | Stop video processing |
| `GET` | `/api/status` | System status, FPS, counts |
| `GET` | `/api/frame` | Latest detections metadata |
| `GET` | `/api/video_feed` | MJPEG video stream |
| `GET` | `/api/alerts?limit=50` | Get alert list |
| `DELETE` | `/api/alerts` | Clear all alerts |
| `GET` | `/api/snapshots/{name}` | Get snapshot image |
| `GET` | `/api/config` | Current configuration |

---

## 🔒 Triple-Lock Logic

The system uses a simplified multi-layer verification:

```
Lock 1: Object Detection (YOLOv8)     ✅ Automated
        ↓ Object confirmed in frame
Lock 2: Behavior Analysis (Rules)     ✅ Automated
        ↓ Suspicious behavior matched
Lock 3: Face Recognition              🔓 Placeholder
        ↓ (Skipped — reserved for future)
  
        ══════════════════
        ║  ALERT RAISED  ║
        ══════════════════
```

---

## 🎤 Demo Presentation Script

> **Duration:** ~5 minutes

1. **Introduction (30s):** *"This is an AI-powered video surveillance system that uses YOLOv8 for real-time object detection and rule-based behavior analysis."*

2. **Architecture (45s):** *"The system has two parts — a Python FastAPI backend running YOLOv8 detection, and a React dashboard. Video is streamed via MJPEG and alerts are polled via REST APIs."*

3. **Live Demo (2min):** Upload a video, show the live feed with bounding boxes, point out the restricted zone overlay, wait for loitering/intrusion alerts.

4. **Alerts (45s):** *"Each alert shows the Triple-Lock status — Detection confirmed, Behavior confirmed, and a placeholder for Face Recognition. You can click to view the snapshot."*

5. **Future Scope (30s):** *"In future versions, we plan to add face recognition, edge AI deployment, and multi-camera support."*

---

## 🔮 Future Scope

- **Face Recognition (Lock 3)** — Integrate face detection and identification
- **Edge AI Deployment** — Run on Raspberry Pi or NVIDIA Jetson
- **Multi-Camera Support** — Process multiple video streams simultaneously
- **WebSocket Alerts** — Replace polling with real-time push notifications
- **Cloud Storage** — Store alerts and snapshots in cloud (AWS S3, GCS)
- **Deep Learning Behavior** — Replace rules with trained behavior models
- **Mobile App** — Push notifications to mobile devices

---

## 📄 License

This project is for educational and demonstration purposes.