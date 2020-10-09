from django.shortcuts import render
import pywt
from scipy.io import wavfile
# Create your views here.
def index(request):
    return render(request, 'index.html')

def add(request):
    #wavefile = '/one.wav'
    # read the wavefile
    #sampling_frequency, signal = scipy.io.wavfile.read(wavefile)
    #
    #scales = (1, len(signal))
    #coefficient, frequency = pywt.cwt(signal, scales, 'wavelet_type')
    #samplerate, data = wavfile.read('one.wav')

    #context: {
       # "coefficient": samplerate,
       # "frequency": data,
   # }
    return render(request, 'add.html')