from Zip_files import createZip
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from moviepy.editor import VideoFileClip
from Statistics import Statistics

Stats = None

root = Tk()
root.title("Video trimmer")

# destinationFolderPath = StringVar()
# videoClipDuration = DoubleVar()
# subclipDuration = IntVar(value=1)

Previous = ""
sourceFilePath = None
inputVideo = None
videoDuration = 1
subclipDuration = 1
totalSubclips = None
destinationFolderPath = None

# totalSubclips = IntVar()
# peecentCompleted = IntVar()
# totalSubclipsProcessed = IntVar()

def setSourceFile():
    global inputVideo, videoDuration, totalSubclips, sourceFilePath
    sourceFilePath = filedialog.askopenfilename()
    inputVideo = VideoFileClip(sourceFilePath)
    FileNameLabel.config(text=f"Source video file : {sourceFilePath}")
    FileNameButton.config(text="Change file")
    videoDuration = inputVideo.duration
    # Stats.set_video_duration(video_duration=videoDuration)
    # Stats.set_subclip_duration(subclip_duration=subclipDuration)
    # VideoClipDurationLabel.config(text=f"{videoDuration} seconds")
    # totalSubclips = Stats.get_total_subclips()
    # TotalSubclipsLabel.config(text=f"{totalSubclips} clips")
    # subclipDuration.set(Stats.get_subclip_duration())
    # SubclipDurationLabel.update()

def setDestinationFolder():
    global destinationFolderPath
    destinationFolderPath = filedialog.askdirectory()
    DestinationFolderLabel.config(text=f"Destination folder : {destinationFolderPath}")
    DestinationFolderButton.config(text="Chamge folder")
    staticsFrame.pack(side=RIGHT,fill=X)

def generate():
    global videoDuration, destinationFolderPath, subclipDuration,Stats
    ProgressBarFrame.pack()
    # source = sourceFilePath.get()
    # destination = destinationFolderPath.get()
    # requiredDuration = subclipDuration
    # createSubClips(source=source,destination=destination,requiredDuration=requiredDuration)
    subClips = []
    # inputVideo = VideoFileClip(source)
    # videoDuraion = inputVideo.duration # in seconds
    # Stats.set_video_duration(video_duration=videoDuraion)
    # Stats.set_subclip_duration(subclip_duration=requiredDuration)
    # videoClipDuration.set(videoDuraion)
    # VideoClipDurationLabel.update()
    # print(videoClipDuration.get(),videoDuraion)
    if subclipDuration <= videoDuration:
        start = 0
        end = subclipDuration
        subClip = inputVideo.subclip(start,end)
        subClips.append(subClip)
        remainingDuration = None
        while end < videoDuration:
            start = end
            remainingDuration = videoDuration - start
            if remainingDuration >= subclipDuration:
                end = start + subclipDuration
            else:
                end = start + remainingDuration
            if start < videoDuration :
                subClip = inputVideo.subclip(start,end)
                subClips.append(subClip)
        videoFileName = inputVideo.filename.split(".")[0].split("/")[-1]
        totalClips = len(subClips)
        for i in range(totalClips):
            subClips[i].write_videofile(f"{destinationFolderPath}\\{videoFileName} (part {i+1} of {totalClips}).mp4")
            Stats.set_subclips_processed(i+1)
            # totalSubclipsProcessed.set(Stats.get_subclips_processed())
            Progress["value"] = Stats.get_processed_percentage()
            Progress.update()
            ProgressLabel.config(text=f"{Progress['value']}% cmplete")
        print("Total clips = ", totalClips)
        inputVideo.close()
    else:
        print(f"Video duraion = {videoDuration}\nClip duration = {subclipDuration}\nCannot create clips as the clip duration is greater than the input videoduration")

def zip():
    global destinationFolderPath
    createZip(destinationFolderPath)

def exitApp():
    exit()
    
def setClipStats(event):
    global Stats, videoDuration,Previous
    if(event.char == "\b"):
        Previous = Previous[:-1]
    else:
        Previous += event.char
    print(Previous)
    Stats = Statistics(videoDuration,float(Previous))
    VideoClipDurationLabel.config(text=f"{videoDuration} seconds")
    totalSubclips = Stats.get_total_subclips()
    TotalSubclipsLabel.config(text=f"{totalSubclips} clips")
    print("video Duration",Stats.get_video_duration())
    print("subclip Duration",Stats.get_subclip_duration())
    
Top = Frame(root)
controlsFrame = Frame(Top)
FileNameLabel = Label(controlsFrame,text="Source video file : ")
FileNameLabel.grid(row=0,column=0)
FileNameButton = Button(controlsFrame,text="Choose file",command=setSourceFile)
FileNameButton.grid(row=0,column=1)
# Label(controlsFrame,textvariable = sourceFilePath).grid(row=0,column=2)

DestinationFolderLabel = Label(controlsFrame,text="Destination folder :")
DestinationFolderLabel.grid(row=1,column=0)
DestinationFolderButton = Button(controlsFrame,text="Choose folder", command=setDestinationFolder)
DestinationFolderButton.grid(row=1,column=1)
# Label(controlsFrame,textvariable = destinationFolderPath).grid(row=1,column=2,padx=3)

Label(controlsFrame,text="Subclip duration (in seconds):").grid(row=2,column=0)
SubclipDurationEntry = Entry(controlsFrame)
SubclipDurationEntry.bind("<Key>",setClipStats)
SubclipDurationEntry.grid(row=2,column=1)

Button(controlsFrame,text="Generate clips",command=generate).grid(row=3,column=0)
Button(controlsFrame,text="Create ZIP file",command=zip).grid(row=3,column=1)
Button(controlsFrame,text="Exit",command=exitApp).grid(row=3,column=2)
controlsFrame.pack(side=LEFT,fill=X)

staticsFrame = Frame(Top)
Label(staticsFrame,text="Video duration").grid(row=0,column=0)
VideoClipDurationLabel = Label(staticsFrame)
VideoClipDurationLabel.grid(row=0,column=1)
Label(staticsFrame,text="Total subclips").grid(row=1,column=0)
TotalSubclipsLabel = Label(staticsFrame,textvariable=totalSubclips)
TotalSubclipsLabel.grid(row=1,column=1)

Top.pack()

ProgressBarFrame = Frame(root)
Progress = ttk.Progressbar(ProgressBarFrame,orient=HORIZONTAL,length=300,mode="determinate")
Progress.grid(row=0,column=0)
ProgressLabel = Label(ProgressBarFrame)
ProgressLabel.grid(row=0,column=1)

# Progress.grid(row=5,column=1)
# Label(staticsFrame,text="subclip duratoion").pack()
# TotalSubclipsLabel = Label(staticsFrame,textvariable=totalSubclips)
# TotalSubclipsLabel.pack()
# staticsFrame.grid(row=4)

root.mainloop()