import streamlit as st
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from PIL import Image
import google.generativeai as genai

st.set_page_config(layout="wide")
st.title("✍️ Hand Gesture Math Solver")

col1, col2 = st.columns([3, 2])
run = col1.checkbox("Run Camera", value=False)
FRAME_WINDOW = col1.image([])
output_text_area = col2.empty()

genai.configure(api_key="AIzaSyDBHwLxjpSfm_ur6ZMP0y-F7eW9U5cZB8M")
model = genai.GenerativeModel('gemini-2.0-flash')

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

prev_pos = None
canvas = None
output_text = ""

def get_hand_info(img):
    hands, img = detector.findHands(img, draw=False, flipType=True)
    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        fingers = detector.fingersUp(hand)
        return fingers, lmList
    return None

def draw(info, prev_pos, canvas):
    fingers, lmList = info
    current_pos = None
    if fingers == [0, 1, 0, 0, 0]:
        current_pos = lmList[8][0:2]
        if prev_pos is None:
            prev_pos = current_pos
        cv2.line(canvas, current_pos, prev_pos, (0, 255, 0), 10)
    elif fingers == [0, 1, 0, 0, 1]:
        canvas = np.zeros_like(canvas)
    return current_pos, canvas

def send_to_ai(model, canvas, fingers):
    if fingers == [1, 1, 1, 1, 0]:
        pil_image = Image.fromarray(canvas)
        response = model.generate_content(["Solve me a maths problem", pil_image])
        return response.text
    return ""

while run:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    if canvas is None:
        canvas = np.zeros_like(img)

    info = get_hand_info(img)
    if info:
        fingers, lmList = info
        prev_pos, canvas = draw(info, prev_pos, canvas)
        response = send_to_ai(model, canvas, fingers)
        if response:
            output_text = response

    image_combined = cv2.addWeighted(img, 0.7, canvas, 0.3, 0)
    FRAME_WINDOW.image(image_combined, channels='BGR')

    if output_text:
        output_text_area.subheader("Answer:")
        output_text_area.code(output_text)

cap.release()
