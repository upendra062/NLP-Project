from pydub import AudioSegment
from pydub.utils import which

AudioSegment.converter = which("ffmpeg")

# AudioSegment.converter = "/home/jiwitesh/ffmpeg-3.2/ffmpeg"
# AudioSegment.ffmpeg = "/home/jiwitesh/ffmpeg-3.2/ffmpeg"
# AudioSegment.ffprobe ="/home/jiwitesh/ffmpeg-3.2/ffmpeg"


def StoreDiarizedOutput(labelling):
    # Creating different audios based on the labelling/timeframes received.
    output = {}
    for x, y, z in labelling:
        if x in output:
            output[x].append((y, z))
        else:
            output[x] = [(y, z)]

    values = []
    items = output.items()
    for item in items:
        values.append(item[1])

    audio = AudioSegment.from_wav('DenoisedInputFiles/DenoisedSignal.wav')
    # audio = ffmpeg.input('Denoise/Denoise_commercial_mono.wav')
    voices = []
    for i in values:
        n = audio[0]
        for j in i:
            start_time, stop_time = j
            n += audio[(start_time * 1000):(stop_time * 1000)]
        voices.append(n)

    for i, j in enumerate(voices):
        j.export(f'SeparatedOutputFiles/speaker{i}.wav', format="wav")
    return