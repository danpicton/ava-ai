from deepgram import DeepgramClient, PrerecordedOptions, PrerecordedResponse
from pprint import pprint
import json

def transcribe_audio(audio_data, api_key):
    deepgram = DeepgramClient(api_key)
    payload = {'buffer': audio_data, 'mimetype': 'audio/wav'}
    options = PrerecordedOptions(smart_format=True, summarize="v2", model='nova-2')
    response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options).to_dict()
    # pprint(json.loads(response.to_json()))
    print(response['results']['channels'][0]['alternatives'][0]['transcript'])
    # pprint()
