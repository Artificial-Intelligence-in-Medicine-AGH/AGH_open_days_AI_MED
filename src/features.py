from src import centers, heat_map


def distance_map_center(img):
    center = centers.cross_center(img)
    distance_map = heat_map.create_map(img, center)

    return distance_map

def distance_map_line(img):
    line = centers.longest_vertical_line
    distance_map = heat_map.create_line_map(img, line)

    return distance_map