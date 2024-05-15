import cv2
import numpy as np
import os
import pandas as pd 
from PIL import Image
from fisheye_csv_extracter import calculate_viewfactors 
import torch 

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def equirectangular_to_fisheye(image):
    height, width = image.shape[:2]
    #print(height, width)

    
    # Crop the lower hemisphere of the image
    upper_half_image = image[:height // 2, :]

    # Determine the otput dimensions of the fisheye image
    output_dim = width 
 
    
    # Calculate the center coordinates
    center_x = width / (2*np.pi)
    center_y = width / (2*np.pi)

    # Calculate the radius of the fisheye image
    radius = output_dim / (2*np.pi)
    
    # Generate the mapping coordinates
    map_x = np.zeros((output_dim, output_dim), dtype=np.float32)
    map_y = np.zeros((output_dim, output_dim), dtype=np.float32)

    for y in range(output_dim):
        for x in range(output_dim):

        
            # Convert the coordinates to polar coordinates
            if x < center_x: 
                theta = 3 * np.pi / 2 - np.arctan((y - center_y) / (x- center_x))
           
            else: 
                theta = np.pi / 2 - np.arctan((y - center_y) / (x - center_x))
        
            rho = np.hypot(x - center_x, y - center_y)

            # Check if the point is in the upper hemisphere
            # if rho <= radius:
            # Calculate the corresponding coordinates in the input image
            src_x = int((theta / (2 * np.pi)) * width)
            src_y = int((rho / radius) * height // 2)
            
            
            # Assign the mapping coordinates
            map_x[y, x] = src_x
            map_y[y, x] = src_y
           

    # Apply the remapping to the input image
    fisheye_image = cv2.remap(upper_half_image, map_x, map_y, cv2.INTER_LINEAR)

    print(fisheye_image.shape[:2])
    return fisheye_image

input_folder = 'DPT/output_semseg'  
output_folder = 'Scriptie/data/fisheye_seg_gpu'  

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# List all image files in the input folder
image_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]
data = [] #empty list

for image_file in image_files:
    input_path = os.path.join(input_folder, image_file)
    output_path = os.path.join(output_folder, image_file)
    img_name = os.path.join(input_path)


    input_image = cv2.imread(input_path)
    
    # Apply the equirectangular to fisheye conversion
    output_image = equirectangular_to_fisheye(input_image)
    data_image = calculate_viewfactors(img_name, output_image)
    data.append(data_image)

    cv2.imwrite(output_path, output_image)

#save extracted data 
df = pd.DataFrame(data)
df.to_csv('fisheye_results.csv', index = False)
print("Conversion completed for all images.")
