#!usr/bin/python
#drumsounds.py

_author_ = "Hugo Zhang"
_version_ = "1.0"

import simpleaudio as sa
import time

#songs
song_obj = 0
seven_nation_army = sa.WaveObject.from_wave_file("song.wav")


#drum audio
hihat = sa.WaveObject.from_wave_file("drum_audio/hihattrimmed.wav")
snare = sa.WaveObject.from_wave_file("drum_audio/snaredrumtrimmed.wav")
bass = sa.WaveObject.from_wave_file("drum_audio/bassdrumtrimmed.wav")
hitom = sa.WaveObject.from_wave_file("drum_audio/hitomtrimmed.wav")
midtom = sa.WaveObject.from_wave_file("drum_audio/midtomtrimmed.wav")

#random audio
elephant = sa.WaveObject.from_wave_file("random_audio/elephant.wav")
clave = sa.WaveObject.from_wave_file("random_audio/clave.wav")
cowbell = sa.WaveObject.from_wave_file("random_audio/cowbell.wav")
dasani = sa.WaveObject.from_wave_file("random_audio/dasani.wav")
moomba = sa.WaveObject.from_wave_file("random_audio/moomba.wav")

def play_hi_hat():
    play_obj = hihat.play()
    
def play_snare():
    play_obj = snare.play()
    
def play_bass():
    play_obj = bass.play()
    
def play_high_tom():
    play_obj = hitom.play()
    
def play_mid_tom():
    play_obj = midtom.play()
    
def play_elephant():
    play_obj = elephant.play()
    
def play_clave():
    play_obj = clave.play()
    
def play_cowbell():
    play_obj = cowbell.play()

def play_dasani():
    play_obj = dasani.play()
    
def play_moomba():
    play_obj = moomba.play()

def play_song():
    global song_obj
    song_obj = seven_nation_army.play()

def stop_song():
    global song_obj
    song_obj.stop()
