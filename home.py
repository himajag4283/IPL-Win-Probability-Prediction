import streamlit as st
from PIL import Image

with st.container():
    st.subheader("Hello, welcome to our website :wave:")

    st.title("IPL WIN PROBABILITY PREDICTOR")
    st.write("## About us :point_down:")
    st.write(
        "This app can predict the real-time winning probabilities of each team based on second innings score!!"
    )
    image = Image.open(r'D:\PROJECT\IPL-Win-Probability-Prediction\th.jpeg')
    st.image(image, width=400)
    st.write("The teams are: ")
    image = Image.open(r'D:\PROJECT\IPL-Win-Probability-Prediction\IPL-2020-all-teams-logos.jpg')
    st.image(image, width=400)

with st.container():
    st.write("---")
    st.write("## How It Works")
    st.header("")
    # st.write("##")
    st.write(
        """
        - **Input Parameters**: Enter the target score, current score, overs completed, wickets down.

        - **Get predicted winning percentages**: By selecting the Predict probability option on the navigation pane you can try it out yourself.

        - Weeee have used Logistic regression to show the winning probability percentage of both the teams (modified)
        
        """
    )