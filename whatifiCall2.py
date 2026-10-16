import tkinter as tk
import time
import threading
import random


lyrics = [
    ("You know it's true", 0.07, 2.3),
    ("Yeah i miss you", 0.08, 3.2),
    ("You know it's true", 0.09, 3.1),
    ("So, What if i call?", 0.06, 2.7),
    ("And you pick up the phone", 0.06, 2.9),
    ("And i use this holiday", 0.06, 1.8),
    ("To make my way to your ghost", 0.08, 3.4),
    ("Oh, what if you're lonely?", 0.07, 2.9),
    ("You know i am too", 0.06, 2.8),
    ("And i get the chance to say", 0.05, 2.4),
    ("Merry Christmas i miss you", 0.08, 3.8),
    ("I MISS YOU", 0.09, 1.4),
]

root = tk.Tk()
root.title("What if i Call")
root.configure(bg="#FF1493")  

window_width, window_height = 600, 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Barbie Magenta Background
canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#4A0027", highlightthickness=0)
canvas.pack()

# Reverted to original Helvetica font
label = tk.Label(root, text="", font=("Helvetica", 20, "bold"), fg="#FFB6C1", bg="#4A0027")
label.place(relx=0.5, rely=0.5, anchor="center")

# Trademark label using original font styling
trademark_label = tk.Label(root, text="", font=("Helvetica", 12, "italic"), fg="#FF69B4", bg="#4A0027")
trademark_label.place(x=15, y=265, anchor="nw")

# Barbie Theme Glow Cycle (Pinks and White)
glow_colors = ["#FFFFFF", "#FFB6C1", "#FF69B4", "#FF1493", "#FFC0CB"]

particles = []

def create_particles(num=150):
    for _ in range(num):
        x = random.randint(0, window_width)
        y = random.randint(0, window_height)
        size = random.randint(2, 6)
        kind = random.choice(["broken_heart", "snow", "sparkle", "butterfly"])
        
        if kind == "broken_heart":
            shape = canvas.create_text(x, y, text="💔",
                                       font=("Helvetica", size + 8))
            particles.append((shape, kind, size))
        elif kind == "snow":
            shape = canvas.create_text(x, y, text="❆",
                                       fill=random.choice(["#FFFFFF", "#FFC0CB", "#FFB6C1"]),
                                       font=("Helvetica", size))
            particles.append((shape, kind, size))
        elif kind == "sparkle":
            shape = canvas.create_text(x, y, text="✦",
                                       fill=random.choice(["#FF69B4", "#FF1493", "#FFFFFF"]),
                                       font=("Helvetica", size))
            particles.append((shape, kind, size))
        else:  # butterfly
            shape = canvas.create_text(x, y, text="🦋",
                                       fill=random.choice(["#FFB6C1", "#FF1493", "#FFFFFF"]),
                                       font=("Helvetica", size + 4))
            particles.append((shape, kind, size))


def animate_particles():
    for shape, kind, size in particles:
        if kind == "broken_heart":
            canvas.move(shape, 0, 3)
            pos = canvas.coords(shape)
            if pos[1] > window_height:
                x = random.randint(0, window_width)
                canvas.coords(shape, x, 0)
        else:  # snow, sparkle, butterfly
            canvas.move(shape, 0, 1)
            pos = canvas.coords(shape)
            if pos[1] > window_height:
                x = random.randint(0, window_width)
                canvas.coords(shape, x, 0)
    root.after(30, animate_particles)

def twinkle_particles():
    barbie_twinkle = ["#FFFFFF", "#FFB6C1", "#FF69B4", "#FFC0CB"]
    for shape, kind, size in particles:
        if kind in ["snow", "sparkle"]:
            canvas.itemconfig(shape, fill=random.choice(barbie_twinkle))
    root.after(500, twinkle_particles)

def glow_effect():
    def cycle(i=0):
        label.config(fg=glow_colors[i % len(glow_colors)])
        root.after(300, cycle, i+1)
    cycle()

def typewriter_effect():
    def run():
        for line, char_delay, line_delay in lyrics:
            text = ""
            for char in line:
                text += char
                label.config(text=text)
                root.update()
                time.sleep(char_delay)
            time.sleep(line_delay)
            label.config(text="")
            root.update()
        
        # Display trademark in lower left after the last line finishes
        trademark_label.config(text="-jaijai")
        
    threading.Thread(target=run, daemon=True).start()

# Call setup
create_particles(150)

# Start animations
animate_particles()
twinkle_particles()
glow_effect()
root.after(500, typewriter_effect)

root.mainloop()