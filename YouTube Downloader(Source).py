import customtkinter as ctk
from pytube import YouTube
from threading import Thread
from tkinter import messagebox

# ----------------- تنظیمات ظاهری -----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("YouTube Downloader")
app.geometry("500x350")

# ----------------- توابع -----------------
def start_download():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Error", "Please enter a YouTube URL.")
        return

    Thread(target=download_video, args=(url,)).start()

def download_video(url):
    try:
        yt = YouTube(url)
        title_label.configure(text=f"🎬 {yt.title}", text_color="lightgreen")

        # لیست کیفیت‌ها
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        best_stream = streams.get_highest_resolution()

        status_label.configure(text="Downloading...", text_color="yellow")
        best_stream.download()
        status_label.configure(text="✅ Download complete!", text_color="lightgreen")

    except Exception as e:
        status_label.configure(text=f"❌ Error: {e}", text_color="red")

# ----------------- رابط کاربری -----------------
title = ctk.CTkLabel(app, text="🎥 YouTube Video Downloader", font=("Arial", 20, "bold"))
title.pack(pady=20)

url_entry = ctk.CTkEntry(app, width=400, placeholder_text="Enter YouTube video URL")
url_entry.pack(pady=10)

download_btn = ctk.CTkButton(app, text="Download", command=start_download, width=200)
download_btn.pack(pady=10)

title_label = ctk.CTkLabel(app, text="", wraplength=400)
title_label.pack(pady=10)

status_label = ctk.CTkLabel(app, text="")
status_label.pack(pady=10)

footer = ctk.CTkLabel(app, text="Made with Arshia Rahnemayi ", text_color="gray")
footer.pack(side="bottom", pady=10)

app.mainloop()
