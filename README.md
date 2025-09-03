# 🎓 AI Alphabet Teacher

An interactive AI-powered system designed to teach children the alphabet through voice recognition, camera-based letter detection, and text-to-speech feedback. The system combines multiple AI technologies to create an engaging learning experience for young learners.

## 📖 Project Overview

The AI Alphabet Teacher is a multimodal educational tool that helps children learn letters through:

- **Voice Recognition**: Children can speak letters and receive immediate feedback
- **Camera Detection**: Real-time letter detection using computer vision (YOLO model)
- **Text-to-Speech**: Audio feedback and pronunciation coaching
- **Progress Tracking**: Star-based reward system and learning progress monitoring
- **Interactive Web Interface**: Child-friendly UI with colorful design

## 🏗️ System Architecture

The project consists of three main components:

1. **Main Flask Server** (`ai-alphabet-teacher.ipynb`) - Handles ASR, TTS, and learning logic
2. **YOLO Detection Server** (`yolo_server.py`) - Computer vision for letter detection
3. **Web Interface** (`test.html`) - Frontend application

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Webcam for letter detection
- Microphone for voice input
- GPU recommended for faster processing (optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MO7AMEDNABIL/AI_Alphabet_Teacher
   cd ai-alphabet-teacher
   ```

2. **Install dependencies**
   ```bash
   pip install flask flask-cors torch whisper pyngrok opencv-python ultralytics TTS
   ```

3. **Download YOLO model**
   - Place your trained YOLO model file as `best.pt` in the project directory
   - The model should be trained to detect alphabet letters A-Z

## 🖥️ Running the System

### Method 1: Local Development

1. **Start the main Flask server**
   ```bash
   python app.py
   ```
   - The server will start on `http://localhost:3000`
   - ngrok URL will be displayed in the console

2. **Start the YOLO detection server**
   ```bash
   ai-alphabet-teacher.ipynb
   ```
   - Runs on `http://127.0.0.1:5001`

3. **Open the web interface**
   - Open `test.html` in your web browser
   - Update the `base` URL in the JavaScript to match your ngrok URL

### Method 2: Using Kaggle with GPU (Recommended)

For faster processing, you can run the servers on Kaggle which provides free GPU access:

#### Setting up Main Server on Kaggle:

1. Create a new Kaggle notebook
2. Upload your project files
3. Install dependencies:
   ```python
   !pip install flask flask-cors torch whisper pyngrok TTS
   ```

4. Run the main server:

if __name__ == "__main__":
    public_url = ngrok.connect(3000)
    print(f"🚀 Alphabet Teacher Server running at: {public_url}")
    print(f"📚 Ready to teach letters with enhanced phonetic recognition!")
    app.run(host="0.0.0.0", port=3000)

5. **Important**: Get the ngrok URL from the output and update your frontend

#### Setting up YOLO Server on Kaggle:

1. Create another Kaggle notebook to train the yolo model on data from roboflow
2. Install YOLO dependencies local:
   ```python
   !pip install ultralytics opencv-python flask flask-cors
   ```

3. Run the YOLO server:
   ```python
   # In Kaggle cell
   import subprocess
   import threading
   
   def run_yolo_server():
       subprocess.run(["python", "yolo_server.py"])
   
   yolo_thread = threading.Thread(target=run_yolo_server)
   yolo_thread.start()
   ```

### ⚠️ Important: Updating ngrok URLs

**The ngrok URL changes every time you restart the server.** You must:

1. Copy the new ngrok URL from the server console output
2. Update the `base` variable in `index.html`:
   ```javascript
   const base = "https://your-new-ngrok-url.ngrok-free.app";
   ```
3. If using separate servers, also update the YOLO server URL in the camera detection fetch call

## 📋 Dependencies

### Core Dependencies
```
flask>=2.3.0
flask-cors>=4.0.0
torch>=2.0.0
openai-whisper>=20231117
pyngrok>=7.0.0
TTS>=0.22.0
opencv-python>=4.8.0
ultralytics>=8.0.0
```

### System Requirements
- **RAM**: Minimum 4GB, recommended 8GB+
- **Storage**: 2GB free space for models
- **Camera**: Any USB or built-in webcam
- **Microphone**: For voice input
- **Internet**: Required for ngrok tunneling

## 🎮 How to Use

### For Children:

1. **Start Learning**: Open the web page and click "Show Me a Letter!" 
2. **Camera Detection**: Hold up letter cards, drawings, or objects shaped like letters
3. **Voice Practice**: Press and hold the microphone button, say a letter clearly
4. **Get Feedback**: Receive immediate audio and visual feedback
5. **Track Progress**: Earn stars for correct pronunciations

### For Parents/Teachers:

1. **Set Child's Name**: Enter the child's name for personalized experience
2. **Choose Letters**: Select specific letters to practice
3. **Monitor Progress**: View learning statistics and completed letters
4. **Reset Progress**: Clear progress to start fresh

## 🔧 Configuration Options

### ASR Settings
- Model: Whisper "tiny.en" (fast, English-only)
- Can be changed to "base" or "small" for better accuracy

### TTS Settings  
- Model: "tts_models/en/ljspeech/glow-tts"
- Optimized for clear, child-friendly speech

### YOLO Detection
- Confidence threshold: 0.8 (adjustable in code)
- Detection timeout: 5 seconds
- Supports A-Z letter recognition

## 🐛 Troubleshooting

### Common Issues:

1. **Microphone not working**
   - Check browser permissions
   - Ensure HTTPS connection (required for microphone access)

2. **Camera not detected**
   - Verify camera permissions
   - Check if camera is being used by other applications

3. **ngrok URL not working**
   - Copy the exact URL from server console
   - Update both `base` URL and any hardcoded URLs in frontend

4. **Slow response times**
   - Use GPU-enabled environment (Kaggle, Colab)
   - Reduce model sizes (use "tiny" instead of "base" models)

5. **YOLO model not found**
   - Ensure `best.pt` file is in the project directory
   - Verify the model is trained for letter detection

## 📁 File Structure

```
ai-alphabet-teacher/
├── app.py                 # Main Flask server (ASR/TTS)
├── yolo_server.py         # YOLO detection server
├── index.html             # Web interface
├── best.pt               # YOLO model file
├── README.md             # This file
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly with children
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenAI Whisper for speech recognition
- Ultralytics YOLO for object detection  
- Coqui TTS for text-to-speech
- ngrok for tunnel services

**Happy Learning!** 🎉📚
