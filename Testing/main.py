"""
DEPRECATED: OLD CODE FOR THE BUZZER SONGS
"""
import board
import simpleio


# Define pin connected to piezo buzzer.
PIEZO_PIN = board.D10 

# All needed notes
notes = {
    "C" : 523, 
    "C#" : 554, 
    "D" : 587, 
    "D#" : 622, 
    "E" : 659, 
    "F" : 698, 
    "F#" : 740, 
    "G" : 784, 
    "G#" : 830, 
    "A": 880, 
    "A#" : 932, 
    "B" : 987
}

# Crab rave song          
crab_rave = [("D", 0.24), 
            ("A#", 0.24), 
            ("G", 0.24), 
            ("G", 0.12), 
            ("D", 0.24), 
            ("D", 0.12), 
            ("A", 0.24), 
            ("F", 0.24), 
            ("F", 0.12),
            ("D", 0.24), 
            ("D", 0.12),
            ("A", 0.24), 
            ("F", 0.24), 
            ("A", 0.12), 
            ("C", 0.24),
            ("C", 0.24),
            ("E", 0.24),
            ("E", 0.12),
            ("F", 0.24), 
            ("D", 0.24),
            ("A#", 0.24), 
            ("G", 0.24),
            ("G", 0.12), 
            ("D", 0.24),
            ("D", 0.12), 
            ("A", 0.24), 
            ("F", 0.24), 
            ("F", 0.12), 
            ("D", 0.24),
            ("D", 0.12), 
            ("A", 0.24), 
            ("F", 0.24), 
            ("F", 0.12), 
            ("C", 0.24), 
            ("C", 0.24), 
            ("E", 0.24), 
            ("E", 0.12), 
            ("F", 0.24)]

# Main loop will go through each tone in order up and down.
while True:
    # Play tones going from start to end of list.
    for i in range(len(crab_rave)):
        simpleio.tone(PIEZO_PIN, notes[crab_rave[i][0]], duration=crab_rave[i][1]) 
