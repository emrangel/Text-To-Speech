import PyPDF2
import pyttsx3
from gtts import gTTS
from io import BytesIO
import time

def func(value):
    return ''.join(value.splitlines())
    
def extract_text(file):
  '''To extract text from chosen PDF file'''
  #file = filedialog.askopenfile(mode='rb', title='Choose a PDF file', filetypes=[('Text Files','*pdf')])
  if file != None:
    pdfReader = PyPDF2.PdfFileReader(file)
    global mytext
    mytext = ""
    for pageNum in range(pdfReader.numPages):
      pageObj = pdfReader.getPage(pageNum)
      mytext += pageObj.extractText()
    file.close()
    mytext = func(mytext)
    return mytext
    

# def speak_text(mytext, path):
# 	"""
# 	function to invoke TTS engine to speak the pdf text
# 	"""
  
# 	engine = pyttsx3.init()
# 	voices = engine.getProperty("voices") 
# 	engine.setProperty('voice', voices[0].id)
# 	engine.setProperty('rate', 150)
# 	engine.save_to_file(mytext, path)
# 	engine.runAndWait()
# 	engine.stop()

def speak_text(mytex, path):

  mytex = gTTS(text = str(mytext),lang='es',slow = False)
  mytex.save(path)

#
def speaks(mytext):
    mp3_fp = BytesIO()
    tts = gTTS(text = str(mytext),lang='es',slow = False)
    tts.write_to_fp(mp3_fp)
    #mp3_fp.seek(0)
    mp3_fp.read()
    #print(mp3_fp.getbuffer().tobytes())
    return mp3_fp.getbuffer().tobytes()


