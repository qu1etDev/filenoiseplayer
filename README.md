# filenoiseplayer
A python program that takes a .wav file (.mp3 not working) and plays it within a random range of time (up to an hour), for a custom set amount of times

The purpose of me uploading to github is for portfolio purposes as well as general public / educational use
Built using tkinter and pyinstaller
Resource Folder includes:
- build (don't know if its important)
- source code (filenoiseplayer.py)
- installpackages.bat (for if you want to develop using the source code)

TO USE:

1. Pick a minimum (left slider value) and a maximum (right slider value) time, each time the audio plays it will pick a random number between them and will wait (in seconds) that amount of time before playing again. (3600 is an hour btw)

2. Pick a file (.wav works, .mp3 I haven't figured out go to https://cloudconvert.com/mp3-to-wav) Once picked, the Log will display a number

3. Press plus or minus to choose the amount of times you want the file to be played before it stops

4. Play the file

5. Press remove file to cancel

(NOTE: I do not know what happens if you press play multiple times. Proceed with caution)
