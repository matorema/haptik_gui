import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

class MyFirstGUI:
    def __init__(self, root):
        self.root = root
        root.title("PCCL Haptik GUI")
        root.geometry("1024x768")
        root.maxsize(1280, 1024)

        # label to show the chosen folder
        self.label = Label(root, text=None, font=('Calibri 15 bold'))
        self.label.pack(side=tk.BOTTOM, padx=5, pady=5)

        # button to choose the folder
        self.choose_folder_button = Button(root, text="Choose Folder", command=self.choose_folder)
        self.choose_folder_button.pack(side=tk.BOTTOM, padx=5, pady=5)

        # button to start something
        self.start_inspection_button = Button(root, text="Start Something", command=self.start_inspection)
        self.start_inspection_button.pack(side=tk.BOTTOM, padx=5, pady=5)

        #place holder for the result image
        self.imagebox = tk.Label(root)
        self.imagebox.pack()
        
    def choose_folder(self):
        filename = filedialog.askdirectory()
        if filename:
            self.choose_folder_button["state"] = "disabled"
            self.label["text"] = str(filename)

    def start_inspection(self):
        if not self.label["text"]:
            self.warning("Choose the folder first")
        else:
            self.start_inspection_button["state"] = "disabled"
            image = ImageTk.PhotoImage(Image.open("qrcode.png"))
            self.imagebox.config(image=image)
            self.imagebox.image = image

    def warning(self, msg):
        messagebox.showinfo("Warning", msg)
        


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()