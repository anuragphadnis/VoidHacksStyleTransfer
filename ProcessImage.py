from SegmentImage import Segment
from PIL import Image
import cv2
from StyleModel import StyleImage

class ProcessImage():
    def __init__(self, mode ):
        self.MODEL_PATH = {"mosaic": "mosaic.pth", "candy" :"candy.pth", "rain_princess": "rain_princess.pth", "udnie": "udnie.pth"}
        self.mode = mode
        print(mode)
        if self.mode == "complete":
            self.mode_set = False
        else:
            self.mode_set = True

    def run_model(self, image, style):
        styler = StyleImage()
        if self.mode_set:
            segment = image
            test = Segment()
            test.SegmentImage(segment)

            segmentedImage = cv2.imread("static/images/segmented.jpg")
            original = cv2.imread(segment)
            gray = cv2.cvtColor(segmentedImage, cv2.COLOR_BGR2GRAY)

            width, height = original.shape[1], original.shape[0]
            resize_ratio = 1.0 * 513 / max(width, height)
            target_size = (int(resize_ratio * width), int(resize_ratio * height))
            original = cv2.resize(original, target_size)

            _ , threshFore = cv2.threshold(gray,120,255 , cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU )
            _ , threshBack = cv2.threshold(gray,120,255 , cv2.THRESH_BINARY+cv2.THRESH_OTSU )

            if self.mode == "foreground":
                threshFore = cv2.cvtColor(threshFore, cv2.COLOR_GRAY2BGR)
                ImageForStyling = cv2.bitwise_or(threshFore, original)
                cv2.imwrite("static/images/ImageForStyling.jpg",ImageForStyling)
                styler.stylize("Model/"+self.MODEL_PATH[style], "static/images/ImageForStyling.jpg")
                styled = cv2.imread("static/images/styled.jpg")

                threshBack = cv2.cvtColor(threshBack, cv2.COLOR_GRAY2BGR)
                Background = cv2.bitwise_or(threshBack, original)

                width, height = Background.shape[1], Background.shape[0]
                resize_ratio = 1.0 * 513 / max(width, height)
                target_size = (int(resize_ratio * width), int(resize_ratio * height))
                styled = cv2.resize(styled, target_size)
                styled = cv2.bitwise_or(threshFore, styled)
                final = cv2.bitwise_and(Background, styled)
            elif self.mode == "background":
                threshBack = cv2.cvtColor(threshBack, cv2.COLOR_GRAY2BGR)
                Background = cv2.bitwise_or(threshBack, original)
                cv2.imwrite("static/images/ImageForStyling.jpg",Background)
                styler.stylize("Model/"+self.MODEL_PATH[style], "static/images/ImageForStyling.jpg")
                styled = cv2.imread("static/images/styled.jpg")

                threshFore = cv2.cvtColor(threshFore, cv2.COLOR_GRAY2BGR)
                Foreground = cv2.bitwise_or(threshFore, original)

                width, height = Foreground.shape[1], Foreground.shape[0]
                resize_ratio = 1.0 * 513 / max(width, height)
                target_size = (int(resize_ratio * width), int(resize_ratio * height))
                styled = cv2.resize(styled, target_size)
                styled = cv2.bitwise_or(threshBack, styled)
                final = cv2.bitwise_and(Foreground, styled)

        else:
            styler.stylize("Model/"+self.MODEL_PATH[style], image)
            final = cv2.imread("static/images/styled.jpg")
        #final = cv2.resize(final, (dims[1],dims[0]))
        filename = list(image.split("/"))[-1]
        cv2.imwrite("static/images/style"+filename, final)
        return ["static/images/style"+filename,"static/images/styled.jpg"]
