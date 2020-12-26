from gtts import gTTS
import os

myText = 'hier steht der gescrapte tex'

language = 'de'
output = gTTS(text='hallo, das ist ein test', lang=language, slow=False)
help(gTTS)
output.save("output.mp3")

hallo = gTTS('hello')
hallo.save('hello.mp3')
