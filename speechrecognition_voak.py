# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:08:39 2023

@author: Sangeeth. P
"""
from vosk import Model, KaldiRecognizer
import pyaudio

#Read the model
#Model download path : https://alphacephei.com/vosk/models
model = Model(r'C:\Python\vosk_model\en_base\vosk-model-small-en-us-0.15')
recognizer = KaldiRecognizer(model, 16000)

# Recognition from the microphone
cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True,frames_per_buffer=8192)
stream.start_stream()

while True:
        data = stream.read(4096)  # Adjust the chunk size as needed
        if recognizer.AcceptWaveform(data) :
            result = recognizer.Result()
            print(result)

            #result = recognizer.FinalResult()
            print(recognizer.FinalResult())