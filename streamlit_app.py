import streamlit as st
st.title("Test App")

# playing door knock
# import audioplayer
# audioplayer.play_mp3("door_knock.mp3")

import subprocess 
subprocess.run(["pip", "install", "pygame"])

import pygame
pygame.mixer.init()
