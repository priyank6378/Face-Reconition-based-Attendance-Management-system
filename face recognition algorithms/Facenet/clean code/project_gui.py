from ast import main
from cgitb import text
import tkinter as tk
from tkinter import Text, ttk, filedialog
from face_recognition import *
from face_detection import *

root = tk.Tk()
root.title("Attendence System")
main_frame = ttk.Frame(root, padding=(10,10,10,10))
main_frame.grid(column=0, row=0)



filename = tk.StringVar()
filename_entry = ttk.Entry(main_frame, textvariable=filename)
filename_entry.grid(column=0, row=0,columnspan=2)

def choose_file_name():
    f = filedialog.askopenfilename()
    filename.set(f)
    print(f)

choose_file = ttk.Button(main_frame, text='Choose Photo', command=choose_file_name, )
choose_file.grid(column=2, row=0)


def run_attendence_system():
    found_faces = recognize_faces(filename.get())
    

mark_attendence = ttk.Button(main_frame, text='MARK ATTENDENCE' , command=run_attendence_system)
mark_attendence.grid(column=0, row=1, columnspan=3)

root.mainloop()