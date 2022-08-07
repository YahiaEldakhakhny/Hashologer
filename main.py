# IMPORTS
import hashlib
from tkinter import *
from pathlib import Path


# CREATE ROOT WIDGET
root = Tk()

# CREATE CHILD WIDGETS
lbl_file_path = Label(root, text="File Path")
lbl_checksum = Label(root, text="SHA256")
lbl_output = Label(root, text="")

e_file_path = Entry(borderwidth=5, width=60)
e_checksum = Entry(borderwidth=5, width=60)

# FUNCTION TO CALCULATE SHA256
def get_sha256(path):
    with open(path, 'rb') as opened_file:
        content = opened_file.read()
        sha256 = hashlib.sha256()
        sha256.update(content)
        return sha256.hexdigest()

# FUNCTION TO VERIFY THE HASH OF THE FILE MATCHES THE ENTERED HASH
def verify():
    lbl_output.config(text="Checking...")
    lbl_output.grid(row=2, column=2)
    file_path = Path(e_file_path.get())
    nominal_sha256 = e_checksum.get()
    
    if e_file_path.get() == "":
        lbl_output.config(text="No File Path Found")
    elif nominal_sha256 == "":
        lbl_output.config(text="No Checksum Found")
    else:
        file_path_obj = Path(file_path)
        generated_sha256 = get_sha256(file_path_obj)
        # Assign the value of the output using ternary conditional
        output = "Hash Verified" if generated_sha256 == nominal_sha256 else "Wrong Hash"
        lbl_output.config(text= output)


btn_verify = Button(root, text="Verify", command=verify, bg='#C5C5C5')

# POSITION CHILD WIDGETS IN THE WINDOW
lbl_file_path.grid(row=0, column=0)
lbl_checksum.grid(row=1, column=0)
lbl_output.grid(row=2, column=2)

btn_verify.grid(row=1, column=5)

e_file_path.grid(row=0, column=1, columnspan=4)
e_checksum.grid(row=1, column=1, columnspan=4)

root.mainloop()