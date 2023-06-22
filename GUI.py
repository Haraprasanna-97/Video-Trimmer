from Script import createSubClips
from Zip_files import createZip
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Video trimmer")

sourceFilePath = StringVar()
destinationFolderPath = StringVar()
duration = IntVar()

def setSourceFile():
    sourceFilePath.set(filedialog.askopenfilename())

def setDestinationFolder():
    destinationFolderPath.set(filedialog.askdirectory())

def submit():
    source = sourceFilePath.get()
    destination = destinationFolderPath.get()
    requiredDuration = duration.get()
    createSubClips(source=source,destination=destination,requiredDuration=requiredDuration)

Label(root,text="Source video file :").grid(row=0,column=0)
Button(root,text="Choose file",command=setSourceFile).grid(row=0,column=1)
Label(root,textvariable = sourceFilePath).grid(row=0,column=2)

Label(root,text="Destination Folder :").grid(row=1,column=0)
Button(root,text="Choose folder :", command=setDestinationFolder).grid(row=1,column=1)
Label(root,textvariable = destinationFolderPath).grid(row=1,column=2)

Label(root,text="Subclip duration:").grid(row=2,column=0)
Entry(root,textvariable = duration).grid(row=2,column=1)
Button(root,text="Generate clips",command=submit).grid(row=3,column=0,columnspan=3)

root.mainloop()
# createSubClips("C:\\Users\\KIIT\\Documents\\Python\\Video editing in python\\Input.mp4","C:\\Users\\KIIT\\Documents\\Python\\Video editing in python\\Destination",30)
# createZip()