import webbrowser
import os
import subprocess
import json

class Commands:
    def __init__(self, config_file='commands.json'):
        self.command_map = {}
        self.last_result = None  # To store the result of the last operation
        self.load_commands(config_file)

    def load_commands(self, config_file):
        try:
            with open(config_file, 'r') as file:
                config = json.load(file)
                self.command_map = config.get("commands", {})
                self.key_bindings = config.get("key_bindings", {})
        except FileNotFoundError:
            print(f"Error: Configuration file '{config_file}' not found.")
        except json.JSONDecodeError:
            print(f"Error: Configuration file '{config_file}' is not valid JSON.")
    
    def get_key_bindings(self):
        return self.key_bindings

    def execute_command(self, command, *args):
        if command in self.command_map:
            cmd_info = self.command_map[command]
            cmd_type = cmd_info.get("type")
            action = cmd_info.get("action")

            if cmd_type == "url":
                webbrowser.open(action)
            elif cmd_type == "file":
                os.startfile(action) #open files with default program, to run with non-default use subprocess.run
            else:
                print(f"Error: Command type '{cmd_type}' is not supported.")
        else:
            print(f"Error: Command '{command}' not found in configuration.")

    def input(self, user_input):
        tokens = user_input.strip().split()
        if len(tokens) == 0:
            return "Error: No command provided."
        
        command = tokens[0].lower()
        args = tokens[1:]
        self.execute_command(command, *args)
