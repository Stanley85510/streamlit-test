import streamlit as st
st.title("Test App")
st.write("Click the button to Start.")

if st.button("Start"):
    call_another_script("be_conversation.py")
    st.write("simulation started")



