import sys
sys.path.append("/Users/TOSUKUi/Documents/workspace/gta-self-driving/")

from pipeline import PipeLine
from capturing import CapturingWindowMSS
from preprocessing import Preprocessing
from cv2 import cv2
import numpy as np


cap = CapturingWindowMSS(os="linux")
preprocess = Preprocessing()
pl = PipeLine()
procedures = [cap, preprocess]    

while 1:
    
    sct_img = pl.execute(procedures)
    print("aaa")
    print(sct_img)
    cv2.imshow('screen', np.array(sct_img))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break


