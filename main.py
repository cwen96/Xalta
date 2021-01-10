import spacy
import tkinter
from tkinter.filedialog import askopenfile
import Text_Processing
import Speech_Processing
from google.cloud import speech
import io
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\Users\\Chris\\Desktop\\GitHub\\nwHacks2021\\gold-rope-301305-872a7baadfbc.json'

def readFile():
    file = askopenfile(mode = 'rb', filetypes = [("Text Files", "*.txt")])
    fileContents = ""
    for i in file:
        fileContents += str(i, 'utf-8')
    return fileContents

def readAudio():
    file = askopenfile(mode = 'rb', filetypes = [("all video format", ".wav")])
    fileContents = file.read()
    audio = speech.RecognitionAudio(content=fileContents)
    return audio

def main():
  #contents = readFile()
  #textProcessing = Text_Processing.Text_Processing(contents)
  audioContents = readAudio()
  audioProcessing = Speech_Processing.Speech_Processing(audioContents)
  audioProcessing.SpeechToText()




if __name__ == "__main__":
    main()