"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""
#https://people.csail.mit.edu/hubert/pyaudio/#docs

import pyaudio
import wave
import audioop

def name():
    return 'mic'

def collect(bits=50):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 48000
    RECORD_SECONDS = 2

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []
    print "* recording"
    #for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    for i in range(0, bits):
        data = stream.read(CHUNK)
        # root mean square (research this?)
        rms = int(audioop.rms(data, 2))
        frames.append(0 if rms % 2 == 0 else 1)

    print "* done recording"
    stream.stop_stream()
    stream.close()
    p.terminate()

    return frames
