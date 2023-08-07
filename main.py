from pytube import YouTube
import time
import streamlit as st

st.write(" # Youtube Downloader")
link = st.text_input("Enter the Youtube URL")


yt = YouTube(link)
if st.button("View Source"):
    st.write("Title: ", yt.title)
    st.write("Views: ", yt.views)

    st.download_button("Download", "/requirements.txt")

if st.button("Download"):
    yd = yt.streams.get_lowest_resolution()
    yd.download()

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)