import streamlit as st
st.title("Test App")

# playing door knock
# import audioplayer
# audioplayer.play_mp3("door_knock.mp3")

# audio_file = open("door_knock.mp3","rb").read()
# st.audio(audio_file,format='auido/mp3')

import base64
import streamlit as st

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )


st.write("# Auto-playing Audio!")

autoplay_audio("door_knock.mp3")
