import cv2
import numpy as np

def compare_fingerprint_images(image1_path, image2_path):
    # Read the fingerprint images in grayscale mode
    img1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)

    # Check if images are loaded successfully
    if img1 is None or img2 is None:
        print("Error: Couldn't read the images.")
        return

    # Calculate histograms for both images
    hist_img1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
    hist_img2 = cv2.calcHist([img2], [0], None, [256], [0, 256])

    # Normalize the histograms (optional step)
    cv2.normalize(hist_img1, hist_img1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    cv2.normalize(hist_img2, hist_img2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

    # Calculate the correlation between the histograms
    correlation = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_CORREL)

    # Set a threshold for similarity
    threshold = 0.95  # Adjust the threshold according to your requirement

    # Check if the correlation value is greater than the threshold
    if correlation > threshold:
        print("The fingerprint images are similar with a correlation of:", correlation)
    else:
        print("The fingerprint images are different with a correlation of:", correlation)

# Replace 'fingerprint1.jpg' and 'fingerprint2.jpg' with the paths of your fingerprint images
image_path1 = 'img1.jpg'
image_path2 = 'img3.jpg'

compare_fingerprint_images(image_path1, image_path2)
