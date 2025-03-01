import os
import moviepy.editor as mp
import speech_recognition as sr
from pydub import AudioSegment
from fpdf import FPDF

def extract_audio(video_path, audio_path):
    video = mp.VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_wav(audio_path)
    audio.export(audio_path, format="wav")

    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="pt-BR")
    return text

def create_pdf(text, pdf_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf.output(pdf_path)

def process_video(video_file, audio_dir, pdf_dir):
    video_filename = os.path.basename(video_file)
    video_base_name, video_extension = os.path.splitext(video_filename)
    audio_path = os.path.join(audio_dir, f"{video_base_name}.wav")
    pdf_path = os.path.join(pdf_dir, f"{video_base_name}.pdf")

    extract_audio(video_file, audio_path)
    text = transcribe_audio(audio_path)
    create_pdf(text, pdf_path)

if __name__ == "__main__":
    video_dir = "input_videos"
    audio_dir = "input_audio"
    pdf_dir = "output_pdfs"

    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(pdf_dir, exist_ok=True)

    for video_file in os.listdir(video_dir):
        if video_file.endswith(".mp4") or video_file.endswith(".mkv"):
            video_path = os.path.join(video_dir, video_file)
            process_video(video_path, audio_dir, pdf_dir)
