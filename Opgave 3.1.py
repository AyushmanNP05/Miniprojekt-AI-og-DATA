import cv2
import numpy as np

# Funktion til at tilføje salt-peber støj til et billede
def add_salt_pepper_noise(image, salt_pepper_ratio):
    noisy_image = image.copy()
    height, width = noisy_image.shape
    num_salt_pepper = int(salt_pepper_ratio * width * height)
    
    # Tilføj hvide pixels (salt)
    coords_salt_x = np.random.randint(0, width - 1, num_salt_pepper)
    coords_salt_y = np.random.randint(0, height - 1, num_salt_pepper)
    noisy_image[coords_salt_y, coords_salt_x] = 255
    
    # Tilføj sorte pixels (peber)
    coords_pepper_x = np.random.randint(0, width - 1, num_salt_pepper)
    coords_pepper_y = np.random.randint(0, height - 1, num_salt_pepper)
    noisy_image[coords_pepper_y, coords_pepper_x] = 0
    
    return noisy_image

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

# Tilføj salt-peber støj
noisy_image_salt_pepper = add_salt_pepper_noise(clean_image, salt_pepper_ratio=0.1)

# Anvend middelværdisfiltrering
filtered_image_mean_salt_pepper = mean_filter(noisy_image_salt_pepper)

# Anvend medianfiltrering
filtered_image_median_salt_pepper = median_filter(noisy_image_salt_pepper)

# Vis de støjfulde og filtrerede billeder
cv2.imshow('Medianfiltreret billede', filtered_image_median_salt_pepper)
cv2.imshow('Salt-peber støjfuldt billede', noisy_image_salt_pepper)
cv2.imshow('Middelværdisfiltreret billede', filtered_image_mean_salt_pepper)

cv2.waitKey(0)
cv2.destroyAllWindows()