import streamlit as st
from transformers import pipeline

st.set_page_config(layout='wide', initial_sidebar_state='collapsed')
st.title("Text Summarization/Question-Answer")
st.info("You can set hyperparameter from sidebar.")
sentence = st.text_area('Please enter your article :', height=50)
button = st.button("Predict")

Note = st.sidebar.info("Info : Please make sure that max >= min")
max = st.sidebar.slider('Select max', 50, 500, step=10, value=130)
min = st.sidebar.slider('Select min', 10, 450, step=10, value=30)
do_sample = st.sidebar.checkbox("Do sample",value=False)

with st.spinner("Please wait. Shortly AI will summarize your text.."):
    if button and sentence:
        summarizer = pipeline("summarization")
        result = summarizer(sentence, max_length=max, min_length=min, do_sample=do_sample)
        st.write(result[0]['summary_text'])

question = st.text_input("Ask me anything from this article:")
ask = st.button("Ask")
with st.spinner("Please wait..."):
    if ask and sentence:
        ans = pipeline("question-answering")
        answer = ans(question=question, context=sentence)
        st.write(f"Answer : {answer['answer']}")


Like = st.button("Did you like this result!")
if Like:
    st.balloons()