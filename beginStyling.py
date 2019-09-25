from ProcessImage import ProcessImage
import argparse

def Style(roi, image, style):
    obj1= ProcessImage(roi)  # complete, foreground, background
    images = obj1.run_model(image, style)
