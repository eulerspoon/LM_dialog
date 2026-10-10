import torch
import soundfile as sf

class TTSModel:
    def __init__(self, language="ru"):
        self.model, _ = torch.hub.load(
            repo_or_dir="snakers4/silero-models",
            model="silero_tts",
            language=language,
            speaker="v5_ru",
        )

        self.model.to(torch.device('cpu'))


    def synthesize_speech(self, text, speaker="xenia", output="output.wav"):

        audio = self.model.apply_tts(text=text, speaker=speaker)
    
        sf.write(output, audio, samplerate=48000)

        return output