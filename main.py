import cv2
import streamlit as st
st.title("webcame application")
run = st.checkbox("Run")
frame_window = st.image([])
cam = cv2.VideoCapture(0)
c = 0
while run:
    c += 1
    ret, frame = cam.read()
    
    frame_window.image(frame)
    if c == 1:
        st.write("shuvam singh")

else:
    st.write("click please")
