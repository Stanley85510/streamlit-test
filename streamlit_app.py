# #App Front End
# import streamlit as st
# st.title("Test App")
# st.write("Click the button to Start.")

# #Define functions
# import base64
# def autoplay_audio(file_path: str):
#     with open(file_path, "rb") as f:
#         data = f.read()
#         b64 = base64.b64encode(data).decode()
#         md = f"""
#             <audio controls autoplay="true">
#             <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
#             </audio>
#             """
#         st.markdown(
#             md,
#             unsafe_allow_html=True,
#         )

# #App Backend
# if st.button("Start"):
#     st.write("simulation started")
#     autoplay_audio("door_knock.mp3")
#     autoplay_audio("door_greeting.mp3")

import streamlit as st
import threading
import queue
import time

# Define a function to play audio in a separate thread
def play_audio_thread(file_path, audio_queue):
    # Simulate playing the audio here (replace this with your actual audio playing code)
    # For example, you can use a library like Pygame or Pydub to play the audio
    print(f"Playing audio: {file_path}")
    time.sleep(2)  # Simulated audio playing time
    print(f"Audio finished: {file_path}")
    audio_queue.put(True)

# Define the main function
def main():
    st.title("Test App")
    st.write("Click the button to Start.")

    # Create a queue to synchronize audio playback
    audio_queue = queue.Queue()

    # Start the first audio in a separate thread
    thread1 = threading.Thread(target=play_audio_thread, args=("door_knock.mp3", audio_queue))
    thread1.start()

    # Wait for the first audio to finish
    audio_queue.get()

    # Start the second audio in a separate thread
    thread2 = threading.Thread(target=play_audio_thread, args=("door_greeting.mp3", audio_queue))
    thread2.start()

    # Wait for the second audio to finish
    audio_queue.get()

    st.write("Audio playback finished.")

if __name__ == "__main__":
    main()


