import streamlit as st
st.title("Test App")

# playing door knock
# import audioplayer
# audioplayer.play_mp3("door_knock.mp3")

audio_file = open("door_knock.mp3","rb").read()
st.audio(auido_file,format='auido/mp3')

