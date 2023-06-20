import cv2
import numpy as np

def cylindrical_to_azimuthal(image):
    # Specify the input and output projection centers
    input_center = (image.shape[1] // 2, image.shape[0] // 2)
    output_center = (image.shape[1] // 2, image.shape[0] // 2)

    # Calculate the maximum radius from the input center
    max_radius = min(image.shape[1] - input_center[0], input_center[0])

    # Calculate the output image size
    output_size = (image.shape[1], image.shape[0])

    # Create the output image
    output_image = np.zeros_like(image)

    # Generate the transformation matrix
    M = cv2.getRotationMatrix2D(input_center, 0, 1)
    M[0, 2] = output_center[0] - input_center[0]
    M[1, 2] = output_center[1] - input_center[1]

    # Perform the perspective transformation
    output_image = cv2.warpAffine(image, M, output_size, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)

    return output_image

# Load the input image
input_image = cv2.imread('data/test/0.jpg')

# Convert the image from cylindrical to azimuthal projection
output_image = cylindrical_to_azimuthal(input_image)

# Display the input and output images
cv2.imshow('Input Image', input_image)
cv2.imshow('Output Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()