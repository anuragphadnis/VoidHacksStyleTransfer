This is a project develoed for Void Hacks for the Machine Learning track. The problem statemet asked to create an application which is capable of doing style transfer on human images.

There are two images involved
1. Target Image
2, Style Image

The Style of style image has to be transfered to the target image with its properties remaining intact.
This project uses CNN to separate out Humans and background from the target image. It then gives option to perform style transfer only on background, foreground or on complete image.

It uses Deeplab model to perform the task of segmentation of human features from the target image.
our system consists of two components: an image transformation network fW and a loss network φ that is used to define several loss
functions `1, . . . , `k. The image transformation network is a deep residual convolutional neural network parameterized by weights W; it transforms input images
x into output images ˆy via the mapping ˆy = fW (x). Each loss function computes
a scalar value `i(ˆy, yi) measuring the difference between the output image ˆy and
a target image yi
. The image transformation network is trained using stochastic
gradient descent to minimize a weighted combination of loss functions:
W∗ = arg min
W
Ex,{yi}
"X
i=1
λi`i(fW (x), yi)
#
(1)
Perceptual Losses for Real-Time Style Transfer and Super-Resolution 5
To address the shortcomings of per-pixel losses and allow our loss functions
to better measure perceptual and semantic differences between images, we draw
inspiration from recent work that generates images via optimization [6,7,8,9,10].
The key insight of these methods is that convolutional neural networks pretrained for image classification have already learned to encode the perceptual
and semantic information we would like to measure in our loss functions. We
therefore make use of a network φ which as been pretrained for image classification as a fixed loss network in order to define our loss functions. Our deep
convolutional transformation network is then trained using loss functions that
are also deep convolutional networks.
The loss network φ is used to define a feature reconstruction loss `
φ
f eat and
a style reconstruction loss `
φ
style that measure differences in content and style
between images. For each input image x we have a content target yc and a style
target ys. For style transfer, the content target yc is the input image x and the
output image ˆy should combine the content of x = yc with the style of ys; we
train one network per style target. For single-image super-resolution, the input
image x is a low-resolution input, the content target yc is the ground-truth highresolution image, and the style reconstruction loss is not used; we train one
network per super-resolution factor.

#Dependencies:
- open-cv
- tensorflow
- pytorch
- flask
