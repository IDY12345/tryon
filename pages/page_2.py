import streamlit as st
import cv2
import numpy as np
from PIL import Image
import insightface
from insightface.app import FaceAnalysis
from insightface.app import ins_get_image

def load_image(image_path):
    return Image.open(image_path)

def swap_faces(model_image, user_image):
    app = FaceAnalysis(name='buffalo_l')
    app.prepare(ctx_id=0, det_size=(640, 640))

    # Load model image
    img = cv2.cvtColor(np.array(model_image), cv2.COLOR_RGB2BGR)
    faces = app.get(img)

    # Load model
    model_path = "inswapper_128.onnx"  # Update with your model path
    swapper = insightface.model_zoo.get_model(model_path)

    # Load user face
    user_img = cv2.cvtColor(np.array(user_image), cv2.COLOR_RGB2BGR)
    user_faces = app.get(user_img)
    user_face = user_faces[0]  # Extract user face

    result = img.copy()
    for face in faces:
        result = swapper.get(result, face, user_face, paste_back=True)

    # Convert result back to RGB
    result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    return Image.fromarray(result_rgb)


col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image(load_image('image5.jpg'), use_column_width=True, caption="Image 1")
with col2:
    st.image(load_image('image6.jpg'), use_column_width=True, caption="Image 2")
with col3:
    st.image(load_image('image7.jpg'), use_column_width=True, caption="Image 3")
with col4:
    st.image(load_image('image8.jpg'), use_column_width=True, caption="Image 4")


st.header("Try It On")

    # Upload user's photo
uploaded_file = st.file_uploader("Upload your photo", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    user_image = Image.open(uploaded_file)

        # Load model image
    model_image1 = load_image('image5.jpg')
    model_image2 = load_image('image7.jpg')
    


if st.button("Try On"):

        swapped_image1 = swap_faces(model_image1, user_image)
        swapped_image2 = swap_faces(model_image2, user_image)
        

        col1, col2 = st.columns(2)
        with col1:
            st.image(swapped_image1, use_column_width=True, caption="Image 1")
        with col2:
            st.image(swapped_image2, use_column_width=True, caption="Image 2")


      