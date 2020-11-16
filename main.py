import streamlit as st
from dataset import Dataset
import random
from PIL import Image


def main():

    dataset = Dataset('./data/deam')
    idx = st.slider('audio number', min_value=0, max_value=100)
    audio = dataset[idx]

    img = Image.open('./m-sne/{}.jpg'.format(idx))
    st.image(img, use_column_width=True)

    st.audio(audio)

if __name__ == "__main__":
    main()
