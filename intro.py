import streamlit as st

st.title("My first web app.")

st.header("Deploying using :blue[streamlit] :sunglasses:")

st.write("Learning streamlit for the first time")


agree = st.checkbox("I agree with Mohit.")

if agree:
    st.write("Great!")


genre = st.radio(
    "What's your favorite movie genre",
    ["Drama", "Comedy", "Documentary"])


if genre=="Comedy":
    st.write("You comedy me... HaHa")
elif genre == "Drama":
    pass



