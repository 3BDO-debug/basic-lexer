import time
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from lexer import action_starter
from variables import *

screen = Tk()
screen.title("Essaaaam w gymoooo in the house bitcheeees !")
screen.geometry("400x200")
filename = "File not uploded yet"


def read_file():
    file_path = askopenfile(mode="r", filetypes=(("Text Files", "*.txt"),))
    global filename
    filename = str(file_path.name)

    if file_path is not None:

        uploded_filename = Label(screen, text=filename)
        uploded_filename.grid(row=10, column=1)

        label_index = 11


        for label in labels:

            title = Label(screen, text=label)
            title.grid(row=label_index, column=0)

            label_value = ",".join(str(x) for x in action_starter()[label])
            label = Label(screen, text=label_value)
            label.grid(row=label_index, column=1)
            label_index += 1


action_button_label = Label(screen, text="Upload c++ code")
action_button_label.grid(row=0, column=0, padx=10)

action_button = Button(screen, text="Choose c++ file", command=lambda: read_file())
action_button.grid(row=0, column=1)

uploded_filename_label = Label(screen, text=f"Uploded filename :")
uploded_filename_label.grid(
    row=10,
    column=0,
)


screen.mainloop()
