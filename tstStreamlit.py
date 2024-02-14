import cv2
import streamlit as st

st.title("Webcam Live Feed")

cap = cv2.VideoCapture(1)

frame_placeholder = st.empty()
stop_button_pressed = st.button("stop")
while cap.isOpened() and not stop_button_pressed:
    ret,frame = cap.read()
    if not ret:
        st.write("The capture has ended")
        break

    frame = cv.cvtColor(frame,cv2.COLOR_BRG2RGB)
    frame_placeholder.image(frame,channels="RGB")

    if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
        break

cap.release()
cv2.destroyAllWindows()
