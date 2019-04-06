from TestModel import test
import argparse

def Style(roi, image, style):
    obj1= test(roi)  # complete, foreground, background
    images = obj1.run_model(image, style)
