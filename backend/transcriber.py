from faster_whisper import WhisperModel
import numpy as np
import tempfile
import soundfile as sf
import os

# Use GPU with float16 (recommended for most use cases)
model = WhisperModel("tiny", compute_type="float16")  # Enable GPU acceleration with float16

BUFFER_SIZE = 32000 * 4  # 4 seconds of audio buffer (32000 samples/sec * 4 sec)

class RealTimeAudioProcessor:
    def __init__(self):
        self.buffer = np.zeros((0,), dtype=np.float32)

    async def process(self, websocket):
        await websocket.accept()
        try:
            while True:
                # Receive audio chunks from the WebSocket
                data = await websocket.receive_bytes()
                float_audio = np.frombuffer(data, dtype=np.float32)

                self.buffer = np.concatenate((self.buffer, float_audio))

                # Keep the buffer size fixed at 4 seconds (32000 * 4)
                if len(self.buffer) > BUFFER_SIZE:
                    self.buffer = self.buffer[-BUFFER_SIZE:]

                # Process every 2 seconds of audio when buffer is big enough
                if len(self.buffer) >= 32000 * 2:  # Process 2 seconds worth of audio
                    chunk = self.buffer[-32000*2:]  # Get the last 2 seconds of audio
                    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
                        sf.write(f.name, chunk, 16000)  # Write the chunk to a temporary file
                        text = self._transcribe(f.name)  # Transcribe the file
                        os.unlink(f.name)  # Clean up the temporary file
                        await websocket.send_text(text)  # Send transcribed text back to client
        except Exception as e:
            print(f"WebSocket error: {e}")

    def _transcribe(self, audio_path):
        # Use faster-whisper to transcribe the audio file
        segments, _ = model.transcribe(audio_path, language="en", beam_size=5)
        return " ".join([seg.text for seg in segments])
