import math
class Statistics:
    def __init__(self) -> None:
        self.video_duration = 0
        self.subclip_duration = 0
        self.total_subclips = 0
        self.subclips_processed = 0
    
    def get_total_subclips(self):
        self.total_subclips = math.ceil(self.video_duration / self.subclip_duration)
        return self.total_subclips
    
    def set_subclips_processed(self,subclips_processed):
        self.subclips_processed = subclips_processed
    
    def get_subclips_processed(self):
        return self.subclips_processed
    
    def get_processed_percentage(self):
        return round((self.subclips_processed / self.total_subclips) * 100)
    
    def set_video_duration(self,video_duration):
        self.video_duration = video_duration

    def set_subclip_duration(self,subclip_duration):
        self.subclip_duration = subclip_duration
    
    def get_video_duration(self):
        return self.video_duration

    def get_subclip_duration(self):
        return self.subclip_duration

# print(A.get_total_subclips())
# A.set_subclips_processed(1)
# print(A.get_processed_percentage())