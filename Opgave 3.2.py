import cv2
import numpy as np

# Funktion til at tilføje Gaussisk støj til et billede
def add_gaussian_noise(image, mean, std_dev):
    noisy_image = image.copy()
    noise = np.random.normal(mean, std_dev, image.shape)
    noisy_image = np.clip(noisy_image + noise, 0, 255)
    return noisy_image.astype(np.uint8)

# Funktion til middelværdisfiltrering af et billede
def mean_filter(image):
    filtered_image = cv2.blur(image, (3, 3))
    return filtered_image

# Funktion til medianfiltrering af et billede
def median_filter(image):
    filtered_image = cv2.medianBlur(image, 3)
    return filtered_image

# Indlæs rent gråskala billede
clean_image = cv2.imread('clean_image.png', cv2.IMREAD_GRAYSCALE)

# Tilføj Gaussisk støj
noisy_image_gaussian = add_gaussian_noise(clean_image, mean=0, std_dev=20)

# Anvend middelværdisfiltrering
filtered_image_mean_gaussian = mean_filter(noisy_image_gaussian)

# Anvend medianfiltrering
filtered_image_median_gaussian = median_filter(noisy_image_gaussian)

# Vis de støjfulde og filtrerede billeder
cv2.imshow('Gaussisk støjfuldt billede', noisy_image_gaussian)
cv2.imshow('Middelværdisfiltreret billede', filtered_image_mean_gaussian)
cv2.imshow('Medianfiltreret billede', filtered_image_median_gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
