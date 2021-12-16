from resemblyzer import preprocess_wav, VoiceEncoder
from scipy.io.wavfile import write


def process(wav_fpath):
    wav = preprocess_wav(wav_fpath)
    encoder = VoiceEncoder("cpu")
    _, cont_embeds, wav_splits = encoder.embed_utterance(wav, return_partials=True, rate=16)

    # Output denoised wave after removing the pauses
    write('DenoisedInputFiles/DenoisedSignal.wav', 16000, wav)
    return cont_embeds, wav_splits
