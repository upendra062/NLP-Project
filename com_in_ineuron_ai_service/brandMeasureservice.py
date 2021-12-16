
from pathlib import Path
from com_in_ineuron_ai_preprocessing.SingalPreprocessing import *
from com_in_ineuron_ai_labelling.SignalLabelsPrediction import signalLabelPrediction
from com_in_ineuron_ai_labelling.SignalLabelling import *
from com_in_ineuron_ai_finaloutputsignal.StoreDiarizedOutput import StoreDiarizedOutput


class BrandMeasureService:

    def performSpeakerDiarization(self, audio_file_path):
        wav_fpath = Path(audio_file_path)
        cont_embeds, wav_splits =process(wav_fpath)
        labels=signalLabelPrediction(cont_embeds)
        labelling = create_labelling(labels,wav_splits)
        output=StoreDiarizedOutput(labelling)


