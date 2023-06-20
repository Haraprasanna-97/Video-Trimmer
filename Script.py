from moviepy.editor import VideoFileClip

subClips = []
inputVideo =  VideoFileClip("Input.mp4")
videoDuraion = inputVideo.duration # in seconds
requiredDuration = int(input("Enter clip size in seconds : ")) #in seconds
if requiredDuration <= videoDuraion:
    start = 0
    end = requiredDuration
    subClip = inputVideo.subclip(start,end)
    subClips.append(subClip)
    remainingDuration = None
    while end < videoDuraion:
        start = end
        remainingDuration = videoDuraion - start
        if remainingDuration >= requiredDuration:
            end = start + requiredDuration
        else:
            end = start + remainingDuration
        if start < videoDuraion :
            subClip = inputVideo.subclip(start,end)
            subClips.append(subClip)
    videoFileName = inputVideo.filename.split(".")[0]
    totalClips = len(subClips)
    for i in range(totalClips):
        subClips[i].write_videofile(f"{videoFileName} (part {i+1} of {totalClips}).mp4")
    print("Total clips = ", totalClips)
    inputVideo.close()
else:
    print(f"Video duraion = {videoDuraion}\nClip duration = {requiredDuration}\nCannot create clips as the clip duration is greater than the input videoduration")