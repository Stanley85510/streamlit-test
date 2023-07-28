import streamlit as st
st.title("Sales Role Play")

import modules
modules.install_pygame()

# Starting the simulation with a door knock and the user answering the door
import audioplayer
audioplayer.play_mp3("door_knock.mp3")
