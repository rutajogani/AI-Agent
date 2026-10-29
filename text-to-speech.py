from openai import OpenAI
import sounddevice as sd

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # Required by the client; Ollama runs locally.
)

def speak():
with client.audio.speech.with_streaming_response.create(
    model="phonon",
    voice="default",
    input="Hello! Phonon is speaking directly from Python.",
    response_format="pcm",
) as response:
    with sd.RawOutputStream(
        samplerate=24000,
        channels=1,
        dtype="int16",
    ) as audio:
        for chunk in response.iter_bytes(chunk_size=4096):
            audio.write(chunk)