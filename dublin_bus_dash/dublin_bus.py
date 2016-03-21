import requests
import glob
import pygame

__author__ = 'Seamus de Cleir'

"""
    Simple app that gets the number of minutes it will take for a bus to arrive
     and reads it
"""
# Starts pygame mixer
pygame.mixer.init()
# Variables for sounds
minutes_wav = "/home/pi/dublin_dash_buttons/sounds/Minutes.wav"
departing_wav = "/home/pi/dublin_dash_buttons/sounds/departing.wav"
in_wav = "/home/pi/dublin_dash_buttons/sounds/In.wav"

# Input the your closest bus stop here
stop_id = "1495"
bus_id = "123"
# URL contain the Dublin Bus json file
url = "https://data.dublinked.ie/cgi-bin/rtpi/realtimebusinformation?stopid="+stop_id+"&format=json"


# Function to play local wav file on Windows & the length it will play
def play_sound(sound_file, t):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    pygame.time.wait(t)


def olay_press():

    # If there is an error the Hangup wav file is played
    no_minutes_wav = "/home/pi/dublin_dash_buttons/sounds/cc_HangUp.wav"

    # Requests the data from the url and turns it into a json file
    info = requests.get(url)
    info_json = info.json()

    # Errorcode 0 is a success anything greater than that is a failure
    # The Hangup sound is played and the errorcode is returned
    if int(info_json["errorcode"]) > 0:
        play_sound(no_minutes_wav, 2500)
        print("Errorcode " + info_json["errorcode"])
    else:
        # Takes the due time from the json file and searching for a matching sound file
        no_minutes = info_json["results"][0]["duetime"]
        for name in glob.glob("/home/pi/dublin_dash_buttons/sounds/*"):

            if name == "/home/pi/dublin_dash_buttons/sounds/" + no_minutes + ".wav":
                no_minutes_wav = name

        # Plays "Departing in ** Minutes"
        play_sound(departing_wav, 1000)
        play_sound(in_wav, 500)
        play_sound(no_minutes_wav, 1500)
        play_sound(minutes_wav, 1000)

