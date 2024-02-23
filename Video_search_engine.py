import os
import speech_recognition as sr
import ffmpeg
import streamlit as st

# Title of the Streamlit app
st.title("My code")

# Displaying a markdown header for the video
st.markdown("# Video: ")

# Displaying the video file
st.video("two_cats.mp4")

# Input box for the word to search for its count
given_word = st.text_input("Enter a word to look for its count")

# Function to extract a segment from the video
def extract_video_segment(input_file, output_file, start_time, duration):
    ffmpeg.input(input_file, ss=start_time).output(output_file, t=duration).run(overwrite_output=True)

# If a word is provided by the user
if given_word:
    # Convert video file to mp3
    command2mp3 = "ffmpeg -i two_cats.mp4 two_cats.mp3"
    os.system(command2mp3)

    # Convert mp3 to wav for speech recognition
    command2wav = "ffmpeg -i two_cats.mp3 two_cats.wav"
    os.system(command2wav)

    # Create a recognizer instance
    r = sr.Recognizer()

    # Recognize the audio file
    with sr.AudioFile('two_cats.wav') as source:
        audio_duration = source.DURATION  # Getting the duration of the audio in seconds
        audio = r.record(source, duration=audio_duration)

    # Convert audio to text
    text = r.recognize_google(audio)

    # Split text into words for further processing
    cleaned = text.lower().split()

    # Initialize word count and timestamp list
    word_count = 0
    timestamps = []

    # Assuming frames per second
    frame_rate = 20

    # Count occurrences of the given word and store timestamps
    for i, ele in enumerate(cleaned):
        if ele == given_word.lower().strip():
            word_count += 1
            # Convert frame index to time (in seconds)
            timestamp = i / len(cleaned) * audio_duration
            timestamps.append(timestamp)

    # Display extracted text from the video
    st.markdown("## Extracted text from video:")
    st.write(text)
    st.write()

    # Display the count of the given word
    st.markdown("### The count of the given word is:")
    st.write("Count =", word_count)

    # Display timestamps of word occurrences
    st.markdown("## Timestamps of the word occurrences:")
    for i in range(len(timestamps)):
        st.write(f"{i+1} time at {timestamps[i]:.2f} seconds")

    # Select a timestamp for trimming the video
    st.markdown("## Select a timestamp to trim the video:")
    selected_timestamp_index = st.selectbox("Select a timestamp:", range(len(timestamps)), format_func=lambda i: f"{timestamps[i]:.2f} seconds")
    
    # If a timestamp is selected, extract and display the video segment
    if selected_timestamp_index:
        # Extract and save the video segment
        extract_video_segment("two_cats.mp4", "video_segment.mp4", timestamps[selected_timestamp_index], duration=100)
        # Display the video segment
        st.video("video_segment.mp4")
