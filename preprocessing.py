import numpy as np
from cv2 import cv2 

class Preprocessing:

    def __init__(self, region_interest=True, bird_eye=True, ):
        self.procedures = []
        if region_interest:
            self.procedures.append(self.__region_interest)
        if bird_eye:
            self.procedures.append(self.__bird_eye)

    def run(self, inputs):
        return self.execute(inputs)

    def execute(self, inputs):
        if self.procedures:
            procedure = self.procedures.pop()
            return self.execute(procedure(inputs))


    def __threshold(self, inputs):
        pass

    def __bird_eye(self, img):
        h, w, _ = img.shape
        before = np.array([(0, h), (w / 4, h / 2), (3 * w / 4, h / 2), (w, h)], np.float32)
        after = np.array([(w / 4, h), (w / 4, 0), (3 * w / 4, 0), (0.79 * w, h)], np.float32)
        
        M = cv2.getPerspectiveTransform(before, after)
        dst = cv2.warpPerspective(img, M, (w, h))
        return dst
        
    def __region_interest(self, img):
        """
        inputs image must be array (n, n, 3)
        """
        h, w, _ = img.shape

        vertices = np.array([[
            (0, h),
            (w // 5, h // 2),
            (4*w // 5, h // 2),
            (w, h)
        ]], np.int32)
        def region_of_interest(img, vertices):
            # Define a blank matrix that matches the image height/width.
            mask = np.zeros_like(img)
            # Retrieve the number of color channels of the image.
            channel_count = img.shape[2]
            # Create a match color with the same color channel counts.
            match_mask_color = (255,) * channel_count
            
            # Fill inside the polygon
            cv2.fillPoly(mask, vertices, match_mask_color)
            
            # Returning the image only where mask pixels match
            masked_image = cv2.bitwise_and(img, mask)
            return masked_image
        return region_of_interest(img, vertices)