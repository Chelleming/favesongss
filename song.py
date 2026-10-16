import sys
import time


song_lines = [
    
    ("Touch my body tender", 2.2, 1.2),
    ("'Cause the feeling makes me weak", 2.5, 1.5),
    ("Kicking off the covers", 2.1, 1.3),
    ("I see the ceiling while you're looking down at me", 4.2, 3.0),
    
   
    ("How can we go back to being friends", 3.8, 1.2),
    ("When we just shared a bed?", 2.8, 2.2),
    ("How can you look at me and pretend", 3.5, 1.2),
    ("I'm someone you've never met?", 3.2, 3.0)
]


print("  NOW PLAYING: Back to Friends            ")
print("  Artist: Sombr                           ")


time.sleep(1.0)

for line_text, duration, line_pause in song_lines:
    sys.stdout.write("🎤 ")
    sys.stdout.flush()
    
    char_delay = duration / len(line_text)
    
    for char in line_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
        
    print() 
    time.sleep(line_pause)

print("\n--- Song finished ---")
print(" -jaijai:(")