# Video_Search_Engine
This project is a video search engine that utilizes speech recognition to transcribe audio from videos. It allows users to search for specific words within the video, providing the count of occurrences of the searched word, and enabling users to select timestamps to trim the video based on word occurrences.

## Vosk Model
This project utilizes the Vosk model for speech recognition. The Vosk model implementation can be found in the vosk_model file.

## Modules Used:
--os: For interacting with the operating system.
--speech_recognition: For transcribing audio from videos.
--ffmpeg: For converting video and audio formats.
--streamlit: For creating the user interface.
--Speech Recognition and Video Analysis
--Converts the video file to mp3 format using ffmpeg.
--Converts the mp3 file to WAV format for speech recognition.
--Utilizes the speech_recognition module to transcribe the audio from the video into text.
--Counts the occurrences of the entered word within the transcribed text.
--Calculates timestamps corresponding to the occurrences of the entered word in the video.

## Timestamp
For calculating the timestamp, I assumed the number of frames in the video and then based on that calculated it using a formula. It may vary from video to video.
### Demo
Included  video demonstrating the video search engine in action.

## Note:
As this was my first time using Streamlit, the Python script required proper formatting to avoid repetition. While there may be some errors and the implementation might not be perfect, the script effectively accomplishes the required task of creating a video search engine with speech recognition capabilities. I acknowledge that improvements can be made to enhance the code's efficiency and readability, and I welcome any feedback or suggestions for improvement."
