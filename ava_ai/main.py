from audio.audio_recorder import record_audio
from transcription.transcribe_audio import transcribe_audio
from config.settings import load_config
from pathlib import Path

def main():
    config_path = Path.cwd()/'ava_ai'/'config.ini'
    config = load_config(config_path)
    DEEPGRAM_API_KEY = config['DEEPGRAM_API_KEY']
    
    print("Recording...")
    audio_data = record_audio(duration=3.5)
    
    print("Transcribing audio...")
    transcribe_audio(audio_data, DEEPGRAM_API_KEY)

if __name__ == "__main__":
    main()
