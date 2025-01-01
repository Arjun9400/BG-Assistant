import tkinter as tk
import keyboard
import threading
import sys
from instructions import Commands
import config
import os
import signal


suppressor = True  # Initialize suppressor variable

def run_gui():
    cmds = Commands()

    def update_label_with_key(key):
        current_text = label.cget("text")
        new_text = current_text + key
        label.config(text=new_text)

    def remove_last_character():
        current_text = label.cget("text")
        if len(current_text) > 1:
            new_text = current_text[:-1]
            label.config(text=new_text)

    def close_program():
        global suppressor
        suppressor = False  # Set suppressor to False to stop keyboard listening
        root.quit()
        root.destroy()
        sys.exit()

    def execute_cmds():
        text = label.cget("text")
        cmds.input(text[1:])
        close_program()
    def listen_for_keys():
        global suppressor
        # This function listens for key presses only when the GUI is active
        while True:
            event = keyboard.read_event(suppress=suppressor)
            if event.event_type == keyboard.KEY_DOWN:
                key = event.name
                if key == 'enter':
                    execute_cmds()
                    #close_program()
                    break
                elif key == 'backspace':
                    remove_last_character()
                elif key == 'space':
                    current_text = label.cget("text")
                    new_text = current_text + " "
                    label.config(text=new_text)
                elif len(key) == 1:
                    update_label_with_key(key)

    root = tk.Tk()
    root.title("Terminal")
    root.overrideredirect(True)
    root.attributes('-topmost', True)
    root.configure(bg='black')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 360
    window_height = 150
    x_position = screen_width - window_width
    y_position = screen_height - window_height
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    

    canvas = tk.Canvas(root, bg='black', height=window_height, width=window_width, bd=0, highlightthickness=0)
    canvas.pack()
    font = ('Courier', 14)
    label = tk.Label(root, text=">", bg='black', fg='white', font=font, bd=0, anchor='nw', justify='left')
    label.place(x=10, y=10)
    
    keyboard_thread = threading.Thread(target=listen_for_keys, daemon=True)
    keyboard_thread.start()

    root.protocol("WM_DELETE_WINDOW", close_program)
    root.mainloop()

run_gui()
