import streamlit as st
import cv2
import numpy as np
from PIL import Image
import insightface
from insightface.app import FaceAnalysis
from insightface.app import ins_get_image

def load_image(image_path):
    return Image.open(image_path)



def main():
    st.title("Fashion Store")

    st.header("Sample Products")

    # Display sample product images

    col1,col2 = st.columns(2)
    with col1:
        st.image(load_image('image1.jpg'), use_column_width=True, caption="Image 1")
    with col2:
        st.image(load_image('image2.jpg'), use_column_width=True, caption="Image 2")

    if st.button("Check Out",key="1"):
        st.switch_page("pages/page_1.py")
    

    col3,col4 = st.columns(2)
    with col3:
        st.image(load_image('image5.jpg'), use_column_width=True, caption="Image 1")
    with col4:
        st.image(load_image('image6.jpg'), use_column_width=True, caption="Image 2")

    if st.button("Check Out",key="2"):
        st.switch_page("pages/page_2.py")


    col5,col6 = st.columns(2)
    with col5:
        st.image(load_image('image9.jpeg'), use_column_width=True, caption="Image 1")
    with col6:
        st.image(load_image('image10.jpeg'), use_column_width=True, caption="Image 2")

    if st.button("Check Out",key="3"):
        st.switch_page("pages/page_3.py")
    


if __name__ == "__main__":
    main()