# -*- coding: utf-8-*-
#Written by Silvério Santos

import re
import json
from mpd import MPDClient

WORDS = ["PLAY"]

PRIORITY = 1

def handle(text, mic, profile):
    mpdCl = get_mpdClient()   
    
    # User decides to play or stop 
    mic.say("What do you want to do: play, stop or update?")
    action = mic.activeListen()
    
    if action == "PLAY":
        found = mpd_search(mpdCl, mic)
        if len(found) == 0:
            mic.say("No titles found.")
        else:
            mpd_play(mpdCl, mic, found)
            
    elif action == "UPDATE":
        mpd_update(mpdCl, mic)
    else:
        mpd_stop(mpdCl, mic)        
    
    close_mpdmpdCl(mpdCl)

def get_mpdClient():
    mpdCl = MPDClient()
    mpdCl.timeout = 10
    mpdCl.idletimeout = None
    mpdCl.connect("localhost", 6600)
    return mpdCl

def mpd_search(mpdCl, mic):
    # User says the artist
    mic.say("What artist would you like to hear music from?")
    artist = mic.activeListen()

    # User says the title
    mic.say("What title would you like to hear?")
    title = mic.activeListen()

    mic.say("Searching for title " + title + " from " + artist)
    return mpdCl.search("artist", artist, "title", title)

def mpd_play(mpdCl, mic, found):
    # Todo: Select from multiple answers
    mic.say("Playing")
    # Debug:
    print(found)
    print json.dumps(found, separators=(',', ': '))
    #mpdCl.play()

def mpd_update(mpdCl, mic):
    mic.say("Updating song database...")
    mpdCl.update()
    # Todo: Say amount of found titles and/or artists
    #title_count = mpdCl.count('title')
    #mic.mpdCl("Finished updating. Found " + title_count + " titles.")

def mpd_stop(mpdCl, mic):
    mpdCl.stop()
    mic.say("Stopped mp3 playback")

def close_mpdmpdCl(mpdCl):
    mpdCl.close()
    mpdCl.disconnect()

def isValid(text):
    play = bool(re.search(r'\bPlay\b',text, re.IGNORECASE))

    if play:
        return True
    else:
        return False
