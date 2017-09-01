# -*- coding: utf-8-*-
#Written by Silvério Santos

import re
#import json
from mpd import MPDClient

WORDS = ["PLAY"]

PRIORITY = 1

def handle(text, mic, profile):
    mpdCl = get_mpdClient()   
    
    # User decides to play or stop 
    mic.say("What do you want to do: play, stop or update?")
    action = mic.activeListen()
    
    if action == "PLAY":
        #Search for artist and title
        found = mpd_search(mpdCl, mic)
        if len(found) == 0:
            # If not found: error message
            mic.say("No titles found.")
        else:
            # If found: play it 
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
    # User to say the artist
    mic.say("What artist would you like to hear music from?")
    artist = mic.activeListen()

    # User to say the title
    mic.say("What title would you like to hear?")
    title = mic.activeListen()

    mic.say("Searching for title " + title + " from " + artist)
    return mpdCl.search("artist", artist, "title", title)

def mpd_play(mpdCl, mic, found):
    if len(found) > 0:
        mic.say("Playing")
        mpdCl.clear()
        mpdCl.playid(mpdCl.addid(found[0]['file']))

def mpd_update(mpdCl, mic):
    mic.say("Updating song database...")
    mpdCl.update()

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
