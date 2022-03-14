from django.shortcuts import render

import speech_recognition
import pyttsx3 as tts
from neuralintents import GenericAssistant
import sys


recognizer = speech_recognition.Recognizer()
speaker = tts.init()
speaker.setProperty('rate', 150) #rate is property, 150 is the value #Creating an object to access the Todo-list
todo_list = ['Go Shopping', 'Clean Room']




# Create your views here.
def baseEverywhere(request):
    pass


def home(request):
    baseEverywhere(request=request)
    context = {
    }
    return render(request, 'chatbot.html', context=context)
