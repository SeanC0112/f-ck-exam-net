import subprocess

def switch_to_app_window(app_name):
    # AppleScript to activate a specific application
    script = f'tell app "{app_name}" to activate'
    
    # Execute the AppleScript using osascript
    subprocess.run(["osascript", "-e", script])

# Example usage: Switch to Finder
switch_to_app_window("Finder")