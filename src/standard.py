import cv2
import skimage.measure as measure
import numpy as np


## Two longest lines across heart and lungs
def lines_ratio(image):
    l_heart = measure.label(image == 255)
    heart = measure.regionprops(l_heart)

    l_lungs = measure.label(image != 0)
    lungs = measure.regionprops(l_lungs)

    img_with_lines = image.copy()
    img_with_lines = cv2.cvtColor(img_with_lines, cv2.COLOR_GRAY2BGR)

    # find heart line
    if heart:
        length = 0
        longest_heart_coords = None
        for region in heart:
            coords = region.coords
            for row in np.unique(coords[:, 0]):  # Iterate through unique rows
                row_coords = coords[coords[:, 0] == row]  # Get all points in the row
                if len(row_coords) > length:
                    length = len(row_coords)
                    longest_heart_coords = row_coords
    else:
        print("No heart regions found in the image.")

    # find lungs line
    if lungs:
        length = 0
        longest_lungs_coords = None
        for region in lungs:
            coords = region.coords
            for row in np.unique(coords[:, 0]):  # Iterate through unique rows
                row_coords = coords[coords[:, 0] == row]  # Get all points in the row
                if len(row_coords) > length:
                    length = len(row_coords)
                    longest_lungs_coords = row_coords
    else:
        print("No lung regions found in the image.")



    # Draw lines on the image
    for coord in longest_heart_coords:
        img_with_lines[coord[0], coord[1]] = (0,0,255)

    for coord in longest_lungs_coords:
        img_with_lines[coord[0], coord[1]] = (255,0,0)

    return{
        "img": img_with_lines,
        "lungs_line_length": len(longest_lungs_coords),
        "heart_line_length": len(longest_heart_coords),
        "ratio" : round(len(longest_heart_coords) / len(longest_lungs_coords),2)
    }
