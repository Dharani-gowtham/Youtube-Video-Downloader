from pytube import YouTube
import streamlit as st

st.write(" # Youtube Downloader")
link = st.text_input("Enter the Youtube URL")

yt = YouTube(link)
if st.button("View Source"):
    st.write("Title: ", yt.title)
    st.write("Views: ", yt.views)

if st.button("Download"):
    yd = yt.streams.get_lowest_resolution()
    yd.download()
