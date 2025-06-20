from pytube import YouTube

def download_video(link):
    try:
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}")
        stream.download()
        print("✅ Download complete!")
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    video_link = input("Enter YouTube video link: ")
    download_video(video_link)

Explanatation of Code:-
Here 
Bilkul bhai! Yeh raha iska **simple English explanation** — jo tum directly GitHub pe `README` ke liye use kar sakte ho:

---

### 📄 Simple Explanation – YouTube Video Downloader in Python

This Python script allows you to download any YouTube video in the **highest available quality** using the `pytube` library.

---

### 💡 How it works:

1. It asks the user to **enter a YouTube video link**.
2. It uses the `pytube` library to access that video.
3. It finds the **highest resolution** stream of the video.
4. It downloads the video to your **default directory**.
5. It shows a success message when done.
6. If something goes wrong (like a broken link or no internet), it will show an error message.
### 📌 Features:
* Very simple to use.
* Downloads the best available quality.
* Works on most YouTube video links.
### 🧠 Requirements:
* Python installed on your system
* `pytube` library
  You can install it using:
bash
  pip install pytube
### 🖥️ How to run:
bash
python your_script_name.py
Then paste the YouTube video link when it asks.
