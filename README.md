# 🏎️ AeroVision | F1 Brand Audit Beta
**Powered by driven13collective**

### Overview
AeroVision uses AI to verify aerodynamic branding and sponsorship placement in high-speed F1 footage.

### How to Use
1. **Upload**: Drag and drop your MP4 footage into the upload zone.
2. **Audit**: Click "Start Audit" to begin the AI verification process.
3. **Review**: Check the results table for brand confidence scores.

### Technical Stack
- **Frontend/Backend**: Reflex (Python)
- **AI Model**: YOLOv8 (best.pt)
- **Deployment**: Lightning AI

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd AeroVision Project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Fetch AI model weights**
   ```bash
   python fetch_weights.py
   ```

4. **Run the application**
   ```bash
   reflex run
   ```

The application will be available at `http://localhost:3000`

---

## 📁 Project Structure

```
AeroVision Project/
├── aero_audit_pro/       # Main application package
│   ├── aero_vision.py    # Reflex UI components
│   └── state.py          # Application state management
├── assets/               # Brand logos and UI assets
├── Dockerfile            # Container configuration
├── fetch_weights.py      # Model weights downloader
├── requirements.txt      # Python dependencies
└── rxconfig.py          # Reflex configuration
```

---

## 🔧 Configuration

The application can be configured through `rxconfig.py` for:
- Port settings
- API endpoints
- Model parameters
- Deployment options

---

## 🐳 Docker Deployment

Build and run with Docker:

```bash
docker build -t aerovision .
docker run -p 3000:3000 aerovision
```

---

## 📊 Features

- ✅ Real-time AI-powered brand detection
- ✅ Dark mode UI optimized for professional workflows
- ✅ Confidence scoring for each brand detection
- ✅ Timestamp tracking for audit compliance
- ✅ Drag-and-drop video upload
- ✅ YOLOv8 deep learning integration

---

## 🤝 Contributing

Interested in improving AeroVision? Reach out to **driven13collective**.

---

## 📝 License

*License information to be added*

---

**Built for the future of F1 sponsorship verification** 🏁
