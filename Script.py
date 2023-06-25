from moviepy.editor import VideoFileClip
from Statistics import Stats

def createSubClips(source,destination,requiredDuration):
    subClips = []
    inputVideo = VideoFileClip(source)
    videoDuraion = inputVideo.duration # in seconds
    Stats.set_video_duration(video_duration=videoDuraion)
    Stats.set_subclip_duration(subclip_duration=requiredDuration)
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
        videoFileName = inputVideo.filename.split(".")[0].split("/")[-1]
        totalClips = len(subClips)
        for i in range(totalClips):
            subClips[i].write_videofile(f"{destination}\\{videoFileName} (part {i+1} of {totalClips}).mp4")
            Stats.set_subclips_processed(i+1)
        print("Total clips = ", totalClips)
        inputVideo.close()
    else:
        print(f"Video duraion = {videoDuraion}\nClip duration = {requiredDuration}\nCannot create clips as the clip duration is greater than the input videoduration")