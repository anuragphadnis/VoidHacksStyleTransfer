from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import pickle
from DeepLabModel import DeepLabModel


class Segment():
    def __init__(self):
        self.MODEL = DeepLabModel("Model/deeplab_model.tar.gz")
        print('model loaded successfully!')
        self.LABEL_NAMES = np.asarray(['background','person'])

        self.FULL_LABEL_MAP = np.arange(len(self.LABEL_NAMES)).reshape(len(self.LABEL_NAMES), 1)
        self.FULL_COLOR_MAP = self.label_to_color_image(self.FULL_LABEL_MAP)
    
    def SegmentImage(self, image_url):
        self.run_visualization(image_url)

    def create_pascal_label_colormap(self):
        """Creates a label colormap used in PASCAL VOC segmentation benchmark.

        Returns:
            A Colormap for visualizing segmentation results.
        """
        colormap = np.zeros((256, 3), dtype=int)
        ind = np.arange(256, dtype=int)

        for shift in reversed(range(8)):
            for channel in range(3):
                colormap[:, channel] |= ((ind >> channel) & 1) << shift
            ind >>= 3

        return colormap


    def label_to_color_image(self,label):
        """Adds color defined by the dataset colormap to the label.

        Args:
            label: A 2D array with integer type, storing the segmentation label.

        Returns:
            result: A 2D array with floating type. The element of the array
            is the color indexed by the corresponding element in the input label
            to the PASCAL color map.

        Raises:
            ValueError: If label is not of rank 2 or its value is larger than color
            map maximum entry.
        """
        if label.ndim != 2:
            raise ValueError('Expect 2-D input label')

        colormap = self.create_pascal_label_colormap()

        if np.max(label) >= len(colormap):
            raise ValueError('label value too large.')

        return colormap[label]


    def vis_segmentation(self,image, seg_map):
        seg_image = self.label_to_color_image(seg_map).astype(np.uint8)
        seg_image = Image.fromarray(seg_image)
        seg_image.save("static/images/segmented.jpg")


    def run_visualization(self,url):
        """Inferences DeepLab model and visualizes result."""

        original_im = Image.open(url)

        print('running deeplab on image %s...' % url)
        resized_im, seg_map = self.MODEL.run(original_im)

        self.vis_segmentation(resized_im, seg_map)