from fastapi import FastAPI, WebSocket
from backend.transcriber import RealTimeAudioProcessor

app = FastAPI()
processor = RealTimeAudioProcessor()

@app.websocket("/ws/transcribe")
async def websocket_endpoint(websocket: WebSocket):
    await processor.process(websocket)