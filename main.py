import cv2
import streamlit as st
from streamlit_webrtc import (
    AudioProcessorBase,
    ClientSettings,
    VideoProcessorBase,
    WebRtcMode,
    webrtc_streamer,
)
st.title("webcame application")
run = st.checkbox("Run")
frame_window = st.image([])
cam = cv2.VideoCapture(1)
c = 0
while run:
    c += 1
    ret, frame = cam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_window.image(frame)
    if c == 1:
        st.write("shuvam singh")
    break

else:
    st.write("click please")
