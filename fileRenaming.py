from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os

directory = ""
files = []

def selectingFiles():
	global directory
	global files

	directory = filedialog.askdirectory(title="Select files location")
	files = sorted(os.listdir(directory))

	if len(files) == 0:
		messagebox.showinfo(title="Caution!!", message="No files selected")

	for i in files:
		fileNames.insert("end", i)

def renamingFiles():
	global directory
	global files

	os.chdir(directory)

	z = 1
	for i in files:
		os.rename(i, renameString.get() + str(z) + "." + str(i.split(".")[1]))
		z += 1

	messagebox.showinfo(title="Achnowledgement", message="Files renamed successfully")

	directory = ""
	files = []	
	fileNames.delete(0, "end")

root = Tk()
root.title("Bulk File Renaming Tool")
root.resizable(False, False)

openButton = Button(root, text="Open", command=selectingFiles)

frameForFileList = Frame(root)
fileListScrollbar = Scrollbar(frameForFileList, orient=VERTICAL)

fileNames = Listbox(frameForFileList, yscrollcommand=fileListScrollbar.set)

fileListScrollbar.config(command=fileNames.yview)

renameLabel = Label(root, text="New file name suffix")
renameString = Entry(root)

processButton = Button(root, text="Rename", command=renamingFiles)

openButton.grid(row=0, column=0, sticky=W+E)
fileNames.pack(side = LEFT, fill = BOTH) 
fileListScrollbar.pack(side = RIGHT, fill = BOTH)
frameForFileList.grid(row=1, column=0, rowspan=2)
renameLabel.grid(row=0, column=1)
renameString.grid(row=1, column=1, sticky=N)
processButton.grid(row=2, column=1, sticky=S+W+E)

root.mainloop()
