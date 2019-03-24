from mss import mss
import numpy as np

class Capturing:

    
    def run(self, _):
        """
        called from pipeline 
        """
        return self.next_frame()

    def next_frame(self):
        pass

    
class CapturingWindowMSS(Capturing):

    def __init__(self, shape=(800, 600), framerate=25, os="windows"):
        self.shape = shape
        self.framerate = framerate
        self.frame = None
        self.sct = mss()
                    
    def next_frame(self):
        # Use the 1st monitor
        monitor = self.sct.monitors[0]

        # Capture a bbox using percent values
        left = monitor["left"] + monitor["width"] * 5 // 100  # 5% from the left
        top = monitor["top"] + monitor["height"] * 5 // 100  # 5% from the top
        right = left + 400  # 400px width
        lower = top + 300  # 300px height
        bbox = (left, top, right, lower)
        
        return np.array(self.sct.grab(bbox))

