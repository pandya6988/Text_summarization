import streamlit as st
from transformers import pipeline

st.set_page_config(layout='wide', initial_sidebar_state='collapsed')
st.title("Text Summarization")
sentence = st.text_area('Please enter your article :', height=50)
button = st.button("Predict")

Note = st.sidebar.info("Info : Please make sure that max >= min")
max = st.sidebar.slider('Select max', 50, 500, step=10, value=130)
min = st.sidebar.slider('Select min', 10, 450, step=10, value=30)

with st.spinner("Please wait. Shortly AI will summarize your text.."):
    if button and sentence:
        summarizer = pipeline("summarization")
        result = summarizer(sentence, max_length=max, min_length=min, do_sample=False)
        st.write(result[0]['summary_text'])

Like = st.button("Did you like this result!")
if Like:
    st.balloons()