import sounddevice as sd
from scipy.io.wavfile import write
from io import BytesIO

def record_audio(duration=3.5, freq=44400):
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    sd.wait()
    
    # Return a BytesIO object for the recording
    audio_buffer = BytesIO()
    write(audio_buffer, freq, recording)
    
    return audio_buffer
