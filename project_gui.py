from operator import attrgetter
import tkinter as tk
from tkinter import Text, ttk, filedialog
from identify_face import *
from mark_attendence import *

root = tk.Tk()
root.title("Attendence System")

style = ttk.Style()
style.configure('custom.TButton', font=('arial rounded mt', 10),
                                    # background='red',
                                    relief='solid')

# style.map('custom.TButton', background=[('active', 'green')])

style.configure('custom1.TButton',font=('arial', 10),
                                    background='#ECE1D8',
                                    relief='raised')               

style.configure("custom.TLabel", background='#F1F2EA',
                                relief='sunken')

style.configure("custom.TFrame", background='#ECE1D8')

main_frame = ttk.Frame(root, padding=(10,10,10,10), style='custom.TFrame')
main_frame.grid(column=0, row=0)

filename = tk.StringVar()
filename_entry = ttk.Entry(main_frame,width=40, textvariable=filename, style='custom.TLabel')
filename_entry.grid(column=0, row=0,columnspan=2)

def choose_file_name():
    f = filedialog.askopenfilename()
    filename.set(f)


# choose_file = tk.Button(main_frame, text='Choose Photo', command=choose_file_name, background='#ECE1D8')
choose_file = ttk.Button(main_frame, text='Choose Photo', command=choose_file_name, style = 'custom.TButton' )
choose_file.grid(column=2, row=0, sticky='W E N S')

def run_attendence_system():
    print("Marking Attendence...")
    img_path = filename.get()
    found_faces = recognize_faces(img_path)
    found_faces = list(set(found_faces))
    mark_attendence_of_students(found_faces)
    reply_entry.delete('1.0', 'end')
    for person in found_faces:
        if person!='UNKNOWN' and person!='~ENCODING':
            reply_entry.insert('end' , person+'\n')
    print("Attendence Marked\n")
    

mark_attendence = ttk.Button(main_frame, text='MARK ATTENDENCE' , command=run_attendence_system, style='custom1.TButton')
mark_attendence.grid(column=0, row=1, columnspan=2, sticky='W E N S')

def _show_attendence():
    attendence = read_attendence()
    reply_entry.delete('1.0', 'end')
    for k,v in attendence.items():
        reply_entry.insert('end', "{:15}".format(k) + ' : ' + str(v)+'\n')

show_attendence = ttk.Button(main_frame, text='SHOW ATTENDENCE' , command=_show_attendence, style='custom1.TButton')
show_attendence.grid(column = 2, row=1, sticky='W E N S')

reply_entry = Text(main_frame, width=20, height=20, wrap='word', background='#ECE1D8')
reply_entry.grid(column=0,row=2, columnspan=3, sticky='W E N S')

root.resizable(0,0)
root.iconbitmap(None)
root.mainloop()