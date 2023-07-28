import streamlit as st
st.title("Test App")
st.write("Click the button to Start.")

import call_script

if st.button("Start"):
    call_script.call_another_script("be_conversation.py")
    st.write("simulation started")



