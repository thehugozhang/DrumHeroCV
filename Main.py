from tkinter import *
from PIL import Image, ImageTk
from AirDrums import main


root = Tk()
root.wm_title("Drum Hero")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("1366x768")
root.configure(background='black')
root.resizable(width=False, height=False)


titlephoto = Image.open("images/logo1.png")
titlephoto = titlephoto.convert("RGB")
titlephoto.mode = "RGB"
titleimg = ImageTk.PhotoImage(titlephoto)
titlelabel = Label(root, image = titleimg, borderwidth = 0, highlightthickness = 0)
titlelabel.image = titleimg
titlelabel.place(x = 298, y = 100)

button2photo = Image.open("images/Play.png")
button2photo = button2photo.convert("RGB")
button2photo.mode = "RGB"
button2img = ImageTk.PhotoImage(button2photo)
button2 = Button(root, image = button2img, highlightbackground ='#000000', highlightcolor = "#000000", foreground = "#000000", background = "#000000", borderwidth = 4, highlightthickness = 4, command = lambda: main())
button2.place(x = 370, y = 364)

creditphoto = Image.open("images/credit.png")
creditphoto = creditphoto.convert("RGB")
creditphoto.mode = "RGB"
creditimg = ImageTk.PhotoImage(creditphoto)
creditlabel = Label(root, image = creditimg, borderwidth = 0, highlightthickness = 0)
creditlabel.image = creditimg
creditlabel.place(x = 550, y = 600)



mainloop()
