import sys
import subprocess
import keyboard 
from instructions import Commands
#from tendo import singleton

#me = singleton.SingleInstance() # allows only 1 instance to run at a time


def exec_func():
    commands = Commands('commands.json')
    key_bindings = commands.get_key_bindings()
    open_key = key_bindings.get("open_terminal")
    close_key = key_bindings.get("close_terminal")
    while True:
        event = keyboard.read_event()  # Wait for a key event
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            if key == open_key:  
                # Launch the GUI script as a new process
                subprocess.run(['pythonw', 'terminal.pyw'])  
            elif key == close_key:  # Exit the program
                sys.exit()


if __name__ == "__main__":
    exec_func()
