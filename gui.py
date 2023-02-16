"""
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import time
import os

class Gui():
    def __init__(self):
        self.root = tk.Tk()
        self.browse = self.choose_folder()

        self.root.title('PCCL Haptik')
        self.w = Canvas(self.root, width=600, height=400)
        self.w.pack()

        self.button1 = tk.Button(self.root, text='Select Folder', width=25, command=self.browse)
        self.button2 = tk.Button(self.root, text='Close', width=25, command=self.root.destroy)
        self.button1.pack()
        self.button2.pack()

        self.root.mainloop()

    def choose_folder(self):
        filename = filedialog.askdirectory()
        print(filename)
        return filename

    def start_inspection(self):
        #create folder for results
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
        folder_name = str(time_string)
        if not os.path.exists(f"{folder_name}"):
            os.makedirs(folder_name)

        ourMessage ='This is our Message'
        messageVar = Message(self.root, text = ourMessage)
        messageVar.config(bg='lightgreen')
        messageVar.pack( )



if __name__ == "__main__":
    print("starting gui")
    gui = Gui()

"""
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