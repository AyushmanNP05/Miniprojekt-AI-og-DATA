import cv2
import numpy as np

def add_gaussian_noise(image, mean, std_dev):
    noisy_image = image.copy()
    noise = np.random.normal(mean, std_dev, image.shape)
    noisy_image = np.clip(noisy_image + noise, 0, 255)
    return noisy_image.astype(np.uint8)
def mean_filter(image):
    filtered_image = cv2.blur(image, (3, 3))
    return filtered_image
def median_filter(image):
    filtered_image = cv2.medianBlur(image, 3)
    return filtered_image

clean_image = cv2.imread('clean_image.png', cv2.IMREAD_GRAYSCALE)
noisy_image_gaussian = add_gaussian_noise(clean_image, mean=0, std_dev=20)
filtered_image_mean_gaussian = mean_filter(noisy_image_gaussian)
filtered_image_median_gaussian = median_filter(noisy_image_gaussian)

cv2.imshow('Gaussisk støjfuldt billede', noisy_image_gaussian)
cv2.imshow('Middelværdisfiltreret billede', filtered_image_mean_gaussian)
cv2.imshow('Medianfiltreret billede', filtered_image_median_gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
