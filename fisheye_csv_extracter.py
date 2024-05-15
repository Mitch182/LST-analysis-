import numpy as np
import PIL as image 
import os 

def calculate_viewfactors(img_name,image):
   
    colors, counts = np.unique(image.reshape(-1, 3), axis=0, return_counts=True)
    total_pixels = sum(np.array(counts[1:]))
    #calculate images per class
    building_color = [180, 120, 120]
    tree_color = [4, 200, 3]
    sky_color = [6, 230, 230]
    # total_pixels = 321699
    building_pixels = np.sum(image == building_color)
    tree_pixels = np.sum(image == tree_color)
    sky_pixels = np.sum(image == sky_color)
    image_id = os.path.splitext(os.path.basename(img_name))[0]

    # #calculate class percentage 
    building_view = building_pixels / total_pixels 
    tree_view = tree_pixels / total_pixels
    sky_view = sky_pixels / total_pixels
   
    #print(colors, counts)    
    #create data structure
    data = {
        'id': image_id, 
        'building_view': building_view,
        'trees_view': tree_view,
        'sky_view': sky_view,
    }
    
    print( image_id)
    return data
