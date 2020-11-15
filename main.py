import streamlit as st
from dataset import Dataset
import random
from PIL import Image
from pymongo import MongoClient


def main():

    methods = ['m-sne', 'd-sne', 'dscmr', 'contrastive', 'cross-modal']

    dataset = Dataset('./data/deam')
    idx = st.slider('audio number', min_value=0, max_value=1500)
    audio = dataset[idx]
    cols = st.beta_columns(len(methods))

    for i, method in enumerate(methods):
        with cols[i]:
            img = Image.open('./data/testers/{}/{}.jpg'.format(method, idx))
            st.subheader(method)
            st.image(img, use_column_width=True)

    st.audio(audio)

if __name__ == "__main__":
    main()
