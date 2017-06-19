from earsketch import *

init()
setTempo(130)


#A

def myFunction(startMeasure, endMeasure):
 fitMedia(Y57_VIBES_1, 7, startMeasure, startMeasure+4)
 fitMedia(Y20_ELECTRO_1, 5, startMeasure, startMeasure+4)
 fitMedia(Y20_ELECTRO_1, 6, startMeasure+4, endMeasure)
 fitMedia(RD_EDM_DRUMBEATPART_4, 2, startMeasure+4, startMeasure+44)

myFunction(1, 11)

#B

def MyFunction(startMeasure, endMeasure):
 fitMedia(TECHNO_ACIDBASS_006, 3, startMeasure, startMeasure+4)
 fitMedia(TECHNO_ACIDBASS_009, 9, startMeasure+4, startMeasure+5)
 fitMedia(Y33_CHOIR_1, 10, startMeasure+5, startMeasure+9)
 fitMedia(TECHNO_ACIDBASS_006, 3, startMeasure+9, startMeasure+13)
 fitMedia(TECHNO_ACIDBASS_009, 9, startMeasure+13, startMeasure+14)
 fitMedia(Y33_CHOIR_1, 10, startMeasure+14, startMeasure+18)
 fitMedia(TECHNO_ACIDBASS_006, 3, startMeasure+18, startMeasure+22)
 fitMedia(TECHNO_ACIDBASS_009, 9, startMeasure+22, startMeasure+23)
 fitMedia(Y33_CHOIR_1, 10, startMeasure+23, startMeasure+27)
 fitMedia(TECHNO_ACIDBASS_006, 3, startMeasure+27, startMeasure+31)
 fitMedia(TECHNO_ACIDBASS_009, 9, startMeasure+31, startMeasure+32)
 fitMedia(Y33_CHOIR_1, 10, startMeasure+32, startMeasure+36)
  
MyFunction(9, 27)


#A

def myFunction(startMeasure, endMeasure):
 fitMedia(Y57_VIBES_1, 7, startMeasure, startMeasure+5)
 fitMedia(Y20_ELECTRO_1, 5, startMeasure, startMeasure+5)

myFunction(45, 50)





bass = OS_LOWTOM01
snare =OS_SNARE05
bassSnare = [bass, snare]
clap = OS_CLAP04
woah = HIPHOP_VOCALHIT_002

amenbeat1 = "0+0+1++1-1001++1"
amenbeat2 = "0+0+1++1-1001++1"
amenbeat3 = "0-001++1-10+--1+"
clapbeat =  "0"

for measure in range(5, 45, 4):
 makeBeat(bassSnare, 1, measure,   amenbeat1)
 makeBeat(bassSnare, 1, measure+1, amenbeat2)
 makeBeat(bassSnare, 1, measure+2, amenbeat2)
 makeBeat(bassSnare, 1, measure+3, amenbeat3)
 
for measure in range(5, 6):
 makeBeat(clap, 4, measure, clapbeat)

for measure in range(9, 10):
 makeBeat(clap, 4, measure, clapbeat)

for measure in range(18, 19):
 makeBeat(clap, 4, measure, clapbeat)
 
for measure in range(27, 28):
 makeBeat(clap, 4, measure, clapbeat)
 
for measure in range(36, 37):
 makeBeat(clap, 4, measure, clapbeat)
 
for measure in range(45, 46):
 makeBeat(clap, 4, measure, clapbeat)
 
setEffect(3, VOLUME, GAIN, -10, 9, 0, 13)
setEffect(3, VOLUME, GAIN, -10, 18, 0, 22)
setEffect(3, VOLUME, GAIN, -10, 27, 0, 31)
setEffect(3, VOLUME, GAIN, -10, 36, 0, 40)
setEffect(3, VOLUME, GAIN, -10, 9, 0, 13)
setEffect(5, VOLUME, GAIN, -30, 1, 0, 3)
setEffect(6, VOLUME, GAIN, 0, 8, -60, 10)


finish()
