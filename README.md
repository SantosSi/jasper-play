jasper-play
===========

Jasper MP3 player module, controlling MPD

The speech to text (STT) system has to correctly and uniquely identify the 
names of the artists and titles of your songs. Currently this is a problem
with the local Sphinx STT, which has a limited amount of recognized words.   

## Installation
1. Install mpd and mpc with your operating system's methods (e.g. package 
   manager on Linux)
2. Configure mpd for the folder storing your MP3s
3. Install playmp3.py into jasper-client's module subfolder

## Usage
```
You: Play
JASPER: What do you want to do: play, stop or update?
You: Play
JASPER: What artist would you like to hear music from?
You: <an artist from your MP3 files>
JASPER: What title would you like to hear?
You: <a title from your MP3 files>
JASPER: Searching for title <title> from <artist>
JASPER: Playing
```
or:
```
You: Play
JASPER: What do you want to do: play, stop or update?
You: Stop
JASPER: Stopped mp3 playback
```
or
```
You: Play
JASPER: What do you want to do: play, stop or update?
You: Update
JASPER: Updating song database
```