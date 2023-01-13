import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
    except:
        finishLabel.configure(text="Invalid Link Bro", text_color="blue")
    finishLabel.configure(text="The Thing is done, like frfr , No Cap")       





# settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

# app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# UI elements
title = customtkinter.CTkLabel(app, text="your link here")
title.pack(padx=10, pady=10)

# input link
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Download Text
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# download button
download = customtkinter.CTkButton(app, text="DOWNLOAD", command=startDownload)
download.pack(padx=10, pady=10)

# run app
app.mainloop()
