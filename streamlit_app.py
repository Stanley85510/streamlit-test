import streamlit as st
st.title("Test App")

# playing door knock
# import audioplayer
# audioplayer.play_mp3("door_knock.mp3")

# audio_file = open("door_knock.mp3","rb").read()
# st.audio(audio_file,format='auido/mp3')



st.button(label="Start", key=None, help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)

autoplay_audio("door_knock.mp3")
autoplay_audio("door_greeting.mp3")
