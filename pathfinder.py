from PIL import Image
from path_classes import ElevationMap
import random

def read_line_of_ints(text):
    ints = []
    ints_as_strs = split_line(text)

    for int_as_str in ints_as_strs:
        ints.append(int(int_as_str))
    return ints

def split_line(line):
    return line.split()

def read_file_into_list(filename):
    with open(filename) as file:
        return file.readlines()

def read_file_into_ints(filename):
    lines = read_file_into_list(filename)

    list_of_lists = []
    for line in lines:
        list_of_lists.append(read_line_of_ints(line))
    return list_of_lists




if __name__ == "__main__":
    elevations = read_file_into_ints('elevation_small.txt')
    e_map = ElevationMap(elevations)

    e_map.draw_grayscale_gradient('map.png', 600, 600)