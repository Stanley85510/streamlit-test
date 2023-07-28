import streamlit as st
st.title("Sales Role Play")

import subprocess
def install_pygame():
    try:
        result = subprocess.run(["pip", "install", "pygame"], check=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("pygame installed successfully.")
        else:
            print("pygame installation failed.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    install_pygame()

