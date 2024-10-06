import tkinter as tk # tkinter is used as gui/themed widget for buttons,windows,etc
from tkinter import ttk 


BG_COLOR = "#1E1F26"     
FG_COLOR = "#F0EDEE"      
ACCENT_COLOR = "#F25C54"   


TITLE_FONT = ("Helvetica", 32, "bold")
STATE_FONT = ("Helvetica", 20)
TIME_FONT = ("Helvetica", 60, "bold")
BUTTON_FONT = ("Helvetica", 16)

#initializing the main menu
root = tk.Tk()
root.geometry("800x500")  
root.title("Professional Stopwatch")
root.resizable(False, False)  #no resizing
root.config(bg=BG_COLOR)

#main frame to hold all widgets
main_frame = tk.Frame(root, bg=BG_COLOR)
main_frame.pack(expand=True, fill='both')


title_frame = tk.Frame(main_frame, bg=BG_COLOR)
title_frame.pack(pady=20)

display_frame = tk.Frame(main_frame, bg=BG_COLOR)
display_frame.pack(pady=20)

button_frame = tk.Frame(main_frame, bg=BG_COLOR)
button_frame.pack(pady=20)

title_label = tk.Label(
    title_frame, 
    text="Stopwatch", 
    bg=BG_COLOR, 
    fg=FG_COLOR, 
    font=TITLE_FONT
)
title_label.pack()

state_label = tk.Label(
    display_frame, 
    text="Paused...", 
    bg=BG_COLOR, 
    fg=ACCENT_COLOR, 
    font=STATE_FONT
)
state_label.pack(pady=(0, 10))

time_label = tk.Label(
    display_frame, 
    text="00:00:00:00", 
    bg=BG_COLOR, 
    fg=FG_COLOR, 
    font=TIME_FONT
)
time_label.pack()

#initializing the style
style = ttk.Style()
style.theme_use('clam')  

#styles for button
style.configure(
    'TButton',
    font=BUTTON_FONT,
    foreground=FG_COLOR,
    background=BG_COLOR,
    borderwidth=1,
    relief="flat",
)
style.map(
    'TButton',
    background=[('active', ACCENT_COLOR)],
    foreground=[('active', BG_COLOR)]
)


button_padding = {'padx': 20, 'pady': 10}

start_button = ttk.Button(
    button_frame, 
    text="Start", 
    command=lambda: update_stopwatch(),
    style='TButton'
)
start_button.grid(row=0, column=0, padx=10)

stop_button = ttk.Button(
    button_frame, 
    text="Stop", 
    command=lambda: stop(), #calls stop button when clicked
    style='TButton'
)
stop_button.grid(row=0, column=1, padx=10)


reset_button = ttk.Button(
    button_frame, 
    text="Reset", 
    command=lambda: reset(),
    style='TButton'
)
reset_button.grid(row=0, column=2, padx=10)


def on_enter(e, btn):
    btn['background'] = ACCENT_COLOR
    btn['foreground'] = BG_COLOR
    btn['borderwidth'] = 2  

def on_leave(e, btn):
    btn['background'] = BG_COLOR
    btn['foreground'] = FG_COLOR
    btn['borderwidth'] = 1 

#events for bind hover
for btn in [start_button, stop_button, reset_button]:
    btn.bind("<Enter>", lambda e, b=btn: on_enter(e, b))
    btn.bind("<Leave>", lambda e, b=btn: on_leave(e, b))

#initializing time variables
secs = 0
mins = 0
hours = 0
ms = 0
timer = None

def update_stopwatch():
    global hours, mins, secs, ms, timer
    state_label.config(text="Running...")
    start_button.state(['disabled']) 
    
    ms += 1
    if ms == 10:
        secs += 1
        ms = 0
    if secs == 60:
        mins += 1
        secs = 0
    if mins == 60:
        hours += 1
        mins = 0
    
    #updating time display
    time_label.config(text=f"{hours:02}:{mins:02}:{secs:02}:{ms:02}")
    
    #scheduling next update
    timer = root.after(100, update_stopwatch)

def stop():
    global timer
    state_label.config(text="Paused...")
    start_button.state(['!disabled']) 
    if timer:
        root.after_cancel(timer)
        timer = None

def reset():
    global hours, mins, secs, ms, timer
    state_label.config(text="Paused...")
    start_button.state(['!disabled'])  
    hours = 0
    mins = 0
    secs = 0
    ms = 0
    if timer:
        root.after_cancel(timer)
        timer = None
    time_label.config(text="00:00:00:00")

#running main event loop
root.mainloop()
