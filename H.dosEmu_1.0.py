import os
import tkinter as tk
from tkinter import messagebox

class Hdos:
    def __init__(self):
        self.running = True
        self.commands = {
            'help': self.help,
            'exit /s': self.exit,
            'exit /r': self.restart,
            'echo': self.echo,
        }

    def run(self):
        print("H.dos 1.0\nType 'help' for a list of commands.")
        while self.running:
            command_input = input("H.dos> ").strip()
            self.handle_command(command_input)

    def handle_command(self, command_input):
        if not command_input:
            return
        parts = command_input.split()
        command = parts[0]
        args = parts[1:]
        
        if command in self.commands:
            self.commands[command](args)
        else:
            print(f"Unknown command: {command}")

    def help(self, args):
        print("Available commands:")
        for command in self.commands:
            print(f" - {command}")

    def exit(self, args):
        print("Exiting H.dos...")
        self.running = False

    def restart(self, args):
        print("Restarting H.dos...")
        self.running = False
        self.run()  # Restart the emulator

    def echo(self, args):
        print(' '.join(args))

def start_emulator():
    emulator = Hdos()
    emulator.run()

def on_start_click():
    root.destroy()
    start_emulator()

# GUI setup
root = tk.Tk()
root.title("H.dos 1.0")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

welcome_label = tk.Label(frame, text="Welcome to H.dos 1.0 Emulator", font=("Helvetica", 16))
welcome_label.pack(pady=10)

start_button = tk.Button(frame, text="Start H.dos", command=on_start_click, font=("Helvetica", 14))
start_button.pack(pady=10)

exit_button = tk.Button(frame, text="Exit", command=root.quit, font=("Helvetica", 14))
exit_button.pack(pady=10)

root.mainloop()
