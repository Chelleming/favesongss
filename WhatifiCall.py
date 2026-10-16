
import sys
import time


song_lines = [
    
    ("You know it's true", 0.12, 2.1),
    ("Yeah, I miss you", 0.12, 2.9),
     ("You know it's true", 0.12, 3.0),
    
    ("So, what if I call?", 0.10, 1.6),
    ("And you pick up the phone?", 0.09, 2.5),
    ("And I use this holiday ", 4.2, 2.5),
    ("To make my way to your ghost",0.12, 1.5),
    ("Oh, what if your lonely?", 0.09, 2.9),
  
]


print("  NOW PLAYING: What If I Call             ")
print("  Artist: Alex Crichton                   ")


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
print("jaijai")