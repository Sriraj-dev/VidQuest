import os
import streamlit as st
import requests
from transcript_generator import save_transcripts

from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "api")
api_port = int(os.environ.get("PORT", 8080))


#Streamlit UI elements:
st.sidebar.title("VidQuest 🖥️ 🔍")
st.sidebar.write("Add YouTube Video Links:")
video_links = st.sidebar.text_area("Paste YouTube Video Links (One per line)")
upload_button = st.sidebar.button("Upload")
if upload_button:
    if(video_links):
        with st.spinner("Uploading..."):
            save_transcripts(video_links.split('\n'))
        st.success("Uploaded!!")



st.write("Ask any question related to the videos:")
question = st.text_input("Enter your prompt here")

if st.button("Submit"):

    if(video_links.__len__ == 0):
        st.write("Please upload the youtube links first!")

    elif(question):
        url = f'http://{api_host}:{api_port}/'
        data = {"query": question}
        response = requests.post(url, json=data)
        st.write(response.json())
    
    else:
        st.write("Please enter a prompt!")

st.sidebar.markdown("""---""")
with st.sidebar.expander("ℹ️ About"):
    st.write("This is a RAG application using pathway framework and LLM_APP features which allows the users to easily interpret youtube videos. This is an AI app where you can add links of the youtube videos which you want to understand and this will help you clarify / summarise the videos for you!")
    st.write("How to Use:")
    st.write("1. Add the links of youtube videos.")
    st.write("2. Ask any question related to the videos.")
    st.write("Want to contribute?👋🏻👋🏻")
    st.write("Here is the code repository: 😁")
    st.write("[pathway_sample_app](https://github.com/Sriraj-dev/pathway_sample_app)")
