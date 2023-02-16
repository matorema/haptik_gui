import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

class MyFirstGUI:
    def __init__(self, root):
        self.root = root
        root.title("PCCL Haptik GUI")
        root.geometry("650x900")
        root.maxsize(650, 900)
        root.minsize(650, 900)
        root.configure(background='LightBlue2')
        self.header_image = ImageTk.PhotoImage(Image.open("pccl.jpeg"))

        #header with pccl image
        self.header = tk.Label(root)
        self.header.pack(side=tk.TOP)
        self.header.config(image=self.header_image)
        self.header.image = self.header_image
        self.header.configure(background='LightBlue2')

        # label to show the chosen folder
        self.label = Label(root, text=None, font=('Calibri 15 bold'))
        self.label.pack(side=tk.BOTTOM)
        self.label.configure(background='LightBlue2')

        # button to choose the folder
        self.choose_folder_button = Button(root, text="Choose Folder", command=self.choose_folder)
        self.choose_folder_button.pack(side=tk.BOTTOM)

        # button to start something
        self.start_inspection_button = Button(root, text="Start Something", command=self.start_inspection)
        self.start_inspection_button.pack(side=tk.BOTTOM)

        #place holder for the result image
        self.imagebox = tk.Label(root)
        self.imagebox.pack(side=tk.TOP)
        self.imagebox.configure(background='LightBlue2')

        
        
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
        

if __name__ == "__main__":
    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()