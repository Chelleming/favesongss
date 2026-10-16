import tkinter as tk
import time
import threading
import random


lyrics = [
    ("Nang iwan mo ako...", 0.08, 2.8),
    ("Bakit ba kailangan pang masaktan?", 0.07, 3.0),
    ("At maitanong sa 'king sarili", 0.07, 2.8),
    ("Kung ako ba ang may kasalanan?", 0.07, 3.2),
    ("Nang iwan mo ako...", 0.08, 2.8),
    ("Bakit 'di mo sinabi sa akin?", 0.07, 3.0),
    ("Na hindi mo na ako mahal...", 0.08, 3.5),
    ("Bakit kailangang iparamdam...", 0.08, 3.0),
    ("Na ako'y walang halaga?", 0.09, 4.0),
]

root = tk.Tk()
root.title("Nang Iwan (Chorus) - This Band")
root.configure(bg="#0D1117") 

window_width, window_height = 650, 320
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")


canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#0D1117", highlightthickness=0)
canvas.pack()

# Text Label (Original Helvetica Font)
label = tk.Label(root, text="", font=("Helvetica", 18, "bold"), fg="#E6EDF3", bg="#0D1117")
label.place(relx=0.5, rely=0.5, anchor="center")

# Trademark label in lower left
trademark_label = tk.Label(root, text="", font=("Helvetica", 11, "italic"), fg="#8B949E", bg="#0D1117")
trademark_label.place(x=15, y=285, anchor="nw")

# Sad & Cold Glow Colors (Cold White, Soft Cyan, Muted Blue, Grey)
glow_colors = ["#FFFFFF", "#C9D1D9", "#7D8590", "#58A6FF", "#A5D6FF"]

particles = []

def create_particles(num=120):
    for _ in range(num):
        x = random.randint(0, window_width)
        y = random.randint(0, window_height)
        size = random.randint(2, 5)
        kind = random.choice(["raindrop", "tear", "broken_heart", "sparkle"])
        
        if kind == "raindrop":
            length = random.randint(10, 18)
            shape = canvas.create_line(x, y, x, y+length,
                                       fill=random.choice(["#482344", "#304259", "#415A77"]), width=1)
            particles.append((shape, kind, length))
        elif kind == "tear":
            shape = canvas.create_text(x, y, text="💧",
                                       font=("Helvetica", size + 6))
            particles.append((shape, kind, size))
        elif kind == "broken_heart":
            shape = canvas.create_text(x, y, text="💔",
                                       font=("Helvetica", size + 6))
            particles.append((shape, kind, size))
        else:  # dim sparkle
            shape = canvas.create_text(x, y, text="✦",
                                       fill=random.choice(["#30363D", "#484F58", "#6E7681"]),
                                       font=("Helvetica", size))
            particles.append((shape, kind, size))


def animate_particles():
    for shape, kind, size in particles:
        if kind == "raindrop":
            canvas.move(shape, 0, 4)
            pos = canvas.coords(shape)
            if pos[1] > window_height:
                x = random.randint(0, window_width)
                canvas.coords(shape, x, 0, x, size)
        else:  # tears, broken hearts, sparkles
            canvas.move(shape, 0, 2)
            pos = canvas.coords(shape)
            if pos[1] > window_height:
                x = random.randint(0, window_width)
                canvas.coords(shape, x, 0)
    root.after(30, animate_particles)

def twinkle_particles():
    cold_twinkle = ["#30363D", "#484F58", "#6E7681", "#8B949E"]
    for shape, kind, size in particles:
        if kind == "sparkle":
            canvas.itemconfig(shape, fill=random.choice(cold_twinkle))
    root.after(600, twinkle_particles)

def glow_effect():
    def cycle(i=0):
        label.config(fg=glow_colors[i % len(glow_colors)])
        root.after(350, cycle, i+1)
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
        
       
        trademark_label.config(text="-jaijai")
        
    threading.Thread(target=run, daemon=True).start()

# Setup
create_particles(120)

# Start animations
animate_particles()
twinkle_particles()
glow_effect()
root.after(500, typewriter_effect)

root.mainloop()