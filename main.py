import spacy
import tkinter
from tkinter.filedialog import askopenfile
import Text_Processing
import Speech_Processing

def readFile():
    file = askopenfile(mode = 'rb', filetypes = [("Text Files", "*.txt")])
    fileContents = ""
    for i in file:
        fileContents += str(i, 'utf-8')
    return fileContents

def main():
  contents = readFile()
  print(contents)


if __name__ == "__main__":
    main()