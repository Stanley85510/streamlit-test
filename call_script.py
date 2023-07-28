import subprocess
def call_another_script(script_name):
    # Use subprocess to call the other script as a separate process
    subprocess.run(["python", script_name])
