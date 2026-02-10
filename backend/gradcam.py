import cv2
import numpy as np

def generate_gradcam(model, img_path):

    image = cv2.imread(img_path)
    heatmap = cv2.applyColorMap(image, cv2.COLORMAP_JET)

    output = "gradcam.jpg"
    cv2.imwrite(output, heatmap)

    return output
