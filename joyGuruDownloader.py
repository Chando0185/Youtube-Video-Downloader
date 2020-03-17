from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import pygame 

file_size=0

# pygame.mixer.init()
# pygame.mixer.music.load('Fearless.mp3')
# pygame.mixer.music.set_volume(0.1)
# pygame.mixer.music.play(1)


def start_download():
	global file_size
	global urlField
	global ButtonBox
	url = urlField.get()
	path_to_save=askdirectory()
	ButtonBox.config(text="Please Wait...")
	ButtonBox.config(state=DISABLED)
	if path_to_save is None:
		return
	obj=YouTube(url)
	strm=obj.streams.first()
	strm.download(path_to_save)
	print("Done...")
	ButtonBox.config(text="Start Download")
	ButtonBox.config(state=NORMAL)
	showinfo("Download Finished","Download SuccessFull")
	urlField.delete(0,END)


root=Tk()
root.title("Youtube Video Downloader(Developed By Chando)")

root.geometry("600x500")

files=PhotoImage(file="icons8-youtube-256.png")

label=Label(root,text="Youtube Video Downloader",background="#b3ffff",fg="black",font=('Agency Fb', 30,'bold')).pack(fill='x',expand='no')

heading=Label(root, image=files)

heading.pack(side=TOP)

label=Label(root,text="Paste Your URL Here",fg="black",font=('Agency Fb', 20,'bold')).pack(fill='x',expand='no')

urlField = Entry(root, font=('Agency Fb', 20,'bold'), justify=CENTER)
urlField.pack(fill="both", padx=10)


ButtonBox=Button(root, text="Start Download", font=('Agency Fb', 20,'bold'), relief='ridge', command=start_download)
ButtonBox.pack(expand='no',fill=X,side=BOTTOM)


root.mainloop()