#how to make Python speak
#first you have to open the terminal and type pip install gtts

from gtts import gTTS
import os

z = 'Hello I am neobhupen'
my_language = 'en'

voice_of_gtts = gTTS(text = z, lang = my_language, slow = True)
#if you want the speed to fast instead of True in the 13th line just type False
#after the slow and = .
voice_of_gtts.save('voice_of_gtts.mp3')
os.system('voice_of_gtts.mp3')

#okay thank you