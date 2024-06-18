import streamlit as st
import requests

st.title("Text summarizer")
st.write("Get your text summarized")

user_input = st.text_area("Input", "", height=400, max_chars=None, key=None, help=None, placeholder="Enter the text to be summarized")

submit_button = st.button(label="Summarize")

output_area = st.empty()

if submit_button:
    data = {'data': user_input}
    response = requests.post('http://localhost:8000', json=data)
    if response.status_code == 200:
        output_text = response.json().get('summary')
        output_area.text(output_text)
        # Display the output text with larger height and no horizontal scrolling
        output_area.markdown(f'<div style="height: 400px; overflow-y: auto;">{output_text}</div>', unsafe_allow_html=True)
    else:
        output_area.text('Error in getting the summary')


