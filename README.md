# CommandPad

Highly customizable project allows users to interact with a terminal-like GUI which runs in background and can be controlled through configurable key bindings in the json file. The terminal can be used to open url, files and run scripts using custom keywords.

## Features
- **Configurable Key Bindings**: Users can define their own keys for opening and closing the terminal via an external JSON configuration file (e.g., `f4` for open, `f3` for close).
- **Customizable Actions**: Runs files by defining file location and input words in the json.
- **Memory efficient**: Code is optimized, designed to run in background without taking up too many resources.
- **Suppressed Keypresses**: GUI does not need focus to type onto, key presses are directly detected and suppressed when GUI is active.

## How It Works
1. **Key Bindings**: The keys to open and close the terminal are defined in the `commands.json` configuration file and can be changed.
2. **Terminal Window**: The terminal window is opened in the bottom-right corner of the screen.
3. **Key Listener**: The script listens for key presses in the background and executes actions based on the configured bindings.

## How to Use
1. Modify the `commands.json` file to set your preferred keys for opening and closing the terminal and actions to perform. Example:

      ```json
   {
       "commands": {
           "yt": {
               "type": "url",
               "action": "https://www.youtube.com/"
           },
           "word": {
               "type": "file",
               "action": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
           },
           "pytest": {
               "type": "file",
               "action": "C:\\python files\\test.py"
           }
       },
       "key_bindings": {
           "open_terminal": "f4",
           "close_terminal": "f3"
       }
   }
2. You might have to add this script as an exclusion to your anti-virus to work properly.
3. Script can added to task scheduler to run on startup to always have it on background
