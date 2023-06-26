from Script import createSubClips
from Zip_files import createZip
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from moviepy.editor import VideoFileClip
from Statistics import Stats

root = Tk()
root.title("Video trimmer")

sourceFilePath = StringVar()
destinationFolderPath = StringVar()
videoClipDuration = DoubleVar()
subclipDuration = IntVar(value=1)

inputVideo = None
videoDuration = None

totalSubclips = IntVar()
peecentCompleted = IntVar()
totalSubclipsProcessed = IntVar()

def setSourceFile():
    global inputVideo, videoDuration
    sourceFilePath.set(filedialog.askopenfilename())
    inputVideo = VideoFileClip(sourceFilePath.get())
    videoDuration = inputVideo.duration
    Stats.set_video_duration(video_duration=videoDuration)
    Stats.set_subclip_duration(subclip_duration=subclipDuration.get())
    videoClipDuration.set(videoDuration)
    VideoClipDurationLabel.update()
    totalSubclips.set(Stats.get_total_subclips())
    TotalSubclipsLabel.update()
    # subclipDuration.set(Stats.get_subclip_duration())
    # SubclipDurationLabel.update()

def setDestinationFolder():
    destinationFolderPath.set(filedialog.askdirectory())
    staticsFrame.grid(row=4)

def generate():
    global videoDuration
    # source = sourceFilePath.get()
    destination = destinationFolderPath.get()
    requiredDuration = subclipDuration.get()
    # createSubClips(source=source,destination=destination,requiredDuration=requiredDuration)
    subClips = []
    # inputVideo = VideoFileClip(source)
    # videoDuraion = inputVideo.duration # in seconds
    # Stats.set_video_duration(video_duration=videoDuraion)
    # Stats.set_subclip_duration(subclip_duration=requiredDuration)
    # videoClipDuration.set(videoDuraion)
    # VideoClipDurationLabel.update()
    # print(videoClipDuration.get(),videoDuraion)
    if requiredDuration <= videoDuration:
        start = 0
        end = requiredDuration
        subClip = inputVideo.subclip(start,end)
        subClips.append(subClip)
        remainingDuration = None
        while end < videoDuration:
            start = end
            remainingDuration = videoDuration - start
            if remainingDuration >= requiredDuration:
                end = start + requiredDuration
            else:
                end = start + remainingDuration
            if start < videoDuration :
                subClip = inputVideo.subclip(start,end)
                subClips.append(subClip)
        videoFileName = inputVideo.filename.split(".")[0].split("/")[-1]
        totalClips = len(subClips)
        for i in range(totalClips):
            subClips[i].write_videofile(f"{destination}\\{videoFileName} (part {i+1} of {totalClips}).mp4")
            Stats.set_subclips_processed(i+1)
            totalSubclipsProcessed.set(Stats.get_subclips_processed())
            Progress["value"] = Stats.get_processed_percentage()
            print(Progress["value"])
            Progress.update()
        print("Total clips = ", totalClips)
        inputVideo.close()
    else:
        print(f"Video duraion = {videoDuration}\nClip duration = {requiredDuration}\nCannot create clips as the clip duration is greater than the input videoduration")

def zip():
    createZip(destinationFolderPath.get())
    
Label(root,text="Source video file :").grid(row=0,column=0)
Button(root,text="Choose file",command=setSourceFile).grid(row=0,column=1)
Label(root,textvariable = sourceFilePath).grid(row=0,column=2)

Label(root,text="Destination Folder :").grid(row=1,column=0)
Button(root,text="Choose folder", command=setDestinationFolder).grid(row=1,column=1)
Label(root,textvariable = destinationFolderPath).grid(row=1,column=2,padx=3)

Label(root,text="Subclip duration (in seconds):").grid(row=2,column=0)
Entry(root,textvariable = subclipDuration).grid(row=2,column=1)

Button(root,text="Generate clips",command=generate).grid(row=3,column=0)
Button(root,text="Create ZIP file",command=zip).grid(row=3,column=1)
Button(root,text="Exit",command=exit).grid(row=3,column=2)

staticsFrame = Frame(root)
Label(staticsFrame,text="Video duration (in seconds)").pack()
VideoClipDurationLabel = Label(staticsFrame,textvariable=videoClipDuration)
VideoClipDurationLabel.pack()
Label(staticsFrame,text="Total subclips").pack()
TotalSubclipsLabel = Label(staticsFrame,textvariable=totalSubclips)
TotalSubclipsLabel.pack()

Progress = ttk.Progressbar(root,orient=HORIZONTAL,length=100,mode="determinate")
Progress.grid(row=5,column=1)
# Label(staticsFrame,text="subclip duratoion").pack()
# TotalSubclipsLabel = Label(staticsFrame,textvariable=totalSubclips)
# TotalSubclipsLabel.pack()
# staticsFrame.grid(row=4)

root.mainloop()