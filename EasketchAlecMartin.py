
from earsketch import *

init()
setTempo(80)

fitMedia(OS_CLAP01, 1,1,3)
fitMedia(RD_ROCK_POPRHYTHM_MAINDRUMS_6, 2,1,3)
fitMedia(HOUSE_DEEP_PIANO_001, 3,1,4)
fitMedia(YG_ELECTRO_PIANO_HIGH_1, 4,3,4)
#Effects
setEffect(1, DELAY, DELAY_TIME, 500)
setEffect(1, VOLUME, GAIN,  0, 1, -10, 4)
setEffect(3, VOLUME, GAIN, -20, 1, 12, 3)
setEffect(4, VOLUME, GAIN, 12, 1, 12, 3)

finish()
