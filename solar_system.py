import tkinter as tk

root = tk.Tk()

# Bar Title
root.title("Solar System")

# Size of window with Background Color
canvas = tk.Canvas(root, width=800, height=400, bg='#D9D9D9')


def draw_planets(canvas):
    # Planet Sun
    canvas.create_oval(150, 150, 50, 250, fill='#FFFF00', outline='black')
    canvas.create_text(100, 200, text="Sun", fill='black')

    # Other planets distance, radius, color, and label
    planets = [
        (30, 5, '#FCA800', 'Mercury'),
        (80, 7, '#ACD9E3', 'Venus'),
        (120, 8, '#0000FD', 'Earth'),
        (170, 6, '#F60301', 'Mars'),
        (230, 15, '#A42B2A', 'Jupiter'),
        (300, 12, '#FFECCE', 'Saturn'),
        (380, 10, '#01C0FF', 'Uranus'),
        (430, 10, '#B0C4DD', 'Neptune'),
        (480, 3, '#546C34', 'Pluto')
    ]

    # Other planets with labels
    for distance, radius, color, label in planets:
        other_planets(canvas, distance, radius, color, label)


def other_planets(canvas, distance, radius, color, label):
    # Position of the planet
    x = 200 + distance
    y = 200

    # Planet Saturn with a ring
    if label == 'Saturn':
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline='black')
        canvas.create_oval(x - radius - 20, y + radius - 15, x + radius + 20, y + radius, outline='black', width=0.2)
    else:
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline='black')

    # Planets Name
    canvas.create_text(x, y + radius + 15, text=label, fill='black')


canvas.pack()

draw_planets(canvas)

root.mainloop()
