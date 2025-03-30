# **Real-Time Audio Transcription with WebSocket**

This project uses `faster-whisper` for real-time audio transcription through a WebSocket connection. The system allows users to speak into their microphone, and the audio is transcribed and displayed live in the browser.

## **Overview**

- **Frontend**: A simple HTML page with a button to start and stop recording. The recorded audio is sent to the backend for transcription over a WebSocket connection.
- **Backend**: A FastAPI server that listens for WebSocket connections, processes the audio using `faster-whisper`, and sends transcribed text back to the frontend.

## **Tech Stack**

- **Frontend**: HTML, JavaScript (WebSocket, MediaRecorder API)
- **Backend**: Python, FastAPI, `faster-whisper`
- **Model**: Whisper (by OpenAI) with `faster-whisper` for efficient real-time transcription
- **GPU Acceleration**: Optional, but enabled by default if CUDA and cuDNN are installed.

---

## **Prerequisites**

### **1. Install Dependencies**

You need Python and **`pip`** to install the required dependencies.

#### **Backend Dependencies**

In the `backend` folder, create a Python virtual environment and install the dependencies:

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

- Install the **CPU version** of `onnxruntime`:
    ```bash
    pip install onnxruntime
    ```

- If you want to enable **GPU acceleration**, install `onnxruntime-gpu`:
    ```bash
    pip install onnxruntime-gpu
    ```

#### **Frontend Dependencies**

The frontend uses basic HTML and JavaScript, so no dependencies are required. However, ensure the `index.html` file is served over a **local server** (e.g., `http.server` in Python).

---

## **Setting Up and Running**

### **1. Backend (FastAPI) Setup**

1. **Navigate to the backend directory**:
   ```bash
   cd backend
   ```

2. **Run the FastAPI server**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

   This will start the backend server, which listens for incoming WebSocket connections.

### **2. Frontend Setup**

1. **Navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Serve the frontend**:
   You can serve the `index.html` file using a simple HTTP server. In the `frontend` directory, run:

   ```bash
   python3 -m http.server 5500
   ```

   This will serve the frontend at `http://localhost:5500` (or `http://<YOUR_LOCAL_IP>:5500` for other devices on your local network).

---

## **Usage**

1. **Start the Backend**:
   - Make sure the backend server is running on `http://0.0.0.0:8000` (accessible within the local network).

2. **Open the Frontend**:
   - Open `http://localhost:5500` (or `http://<YOUR_LOCAL_IP>:5500`) in a browser.
   - Press **"Start Recording"** to begin recording audio. The audio is sent to the backend via WebSocket for transcription.
   - Press **"Stop Recording"** to stop the recording and close the WebSocket connection.

3. **Real-Time Transcription**:
   - As you speak, the transcription will be displayed in the **output area** on the frontend in real-time.

---

## **Debugging Tips**

1. **WebSocket Connection Issues**:
   - Ensure that the **backend** is running and accessible on the local network.
   - Verify that the WebSocket URL in the frontend (`ws://<YOUR_LOCAL_IP>:8000/ws/transcribe`) points to the correct backend server IP.

2. **Microphone Access**:
   - If the browser doesn't ask for microphone access, check your browser’s **permissions**.
   - Make sure the `getUserMedia()` function is successfully accessing the microphone.

3. **GPU Issues**:
   - If you face issues related to CUDA/cuDNN, ensure that you have the correct versions of **CUDA** and **cuDNN** installed on your machine.
   - Alternatively, switch to **CPU-only mode** by installing the CPU version of `onnxruntime`.

---

## **Folder Structure**

```
real-time-transcription/
│
├── backend/
│   ├── main.py          # FastAPI app
│   ├── transcriber.py   # Audio processing and transcription logic
│   ├── requirements.txt # Python dependencies
│   └── venv/            # Virtual environment for backend
│
├── frontend/
│   └── index.html       # HTML page with recording and transcription
│
├── README.md            # Instructions for setup and running
└── requirements.txt     # (Optional) If frontend dependencies are needed
```

---

## **Troubleshooting**

1. **WebSocket Connection Fails**:
   - Ensure the backend server is running and accessible at `ws://<YOUR_LOCAL_IP>:8000/ws/transcribe`.
   - Test connectivity by accessing `http://<YOUR_LOCAL_IP>:8000` from a browser.
   
2. **Model Loading Errors**:
   - Make sure the **correct version of `onnxruntime`** is installed (either CPU or GPU).

3. **Microphone Access Denied**:
   - Grant microphone access in your browser when prompted.

---

## **License**

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

### **Summary**:

- **Backend**: Set up and run FastAPI server to process real-time audio transcription.
- **Frontend**: Serve HTML page for users to interact with the microphone and view live transcriptions.
- **Run**: Make sure both backend and frontend are running and connected via WebSocket.
