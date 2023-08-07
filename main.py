# from pytube import YouTube
# import streamlit as st
#
# st.write(" # Youtube Downloader")
# link = st.text_input("Enter the Youtube URL")
#
# yt = YouTube(link)
# if st.button("View Source"):
#     st.write("Title: ", yt.title)
#     st.write("Views: ", yt.views)
#
# if st.button("Download"):
#     yd = yt.streams.get_lowest_resolution()
#     # bina = yd.download()
#     yd.download()
#
#     # with open("bina.mp4","rb") as file:
#     #     btn = st.download_button(
#     #         label="Download",
#     #         data=file,
#     #         file_name=yt.title,
#     #         mime="mp4"
#     #     )

from pytube import YouTube
import streamlit as st

st.write(" # Youtube Downloader")
link = st.text_input("Enter the Youtube URL")

if st.button("View Source"):
    yt = YouTube(link)
    st.write("Title: ", yt.title)
    st.write("Views: ", yt.views)
    st.write(yt.title,'.mp4')

if st.button("Download"):
    yt = YouTube(link)
    yd = yt.streams.get_lowest_resolution()
    val = yd.download()
    video_file = open(val,'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)
    # st.download_button("Download Now", video)
    # with open('')

    # with open ("video.mp4","rb") as file:
    #     btn = st.download_button(
    #         label="Download",
    #         data=file,
    #         file_name="video.mp4",
    #         mime=
    #     )

