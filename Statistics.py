import math
class Statistics:
    def __init__(self,duration,subclip_duration) -> None:
        self.duration = duration
        self.subclip_duration = subclip_duration
        self.total_subclips = 0
        self.subclips_processed = 0
    
    def get_total_subclips(self):
        self.total_subclips = math.ceil(self.duration / self.subclip_duration)
        return self.total_subclips
    
    def set_subclips_processed(self,subclips_processed):
        self.subclips_processed = subclips_processed
        return self.subclips_processed
    
    
A = Statistics(158.29,70)
print(A.get_total_subclips())
print(A.set_subclips_processed(1))
print(A.set_subclips_processed(2))
print(A.set_subclips_processed(3))