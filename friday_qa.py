""" practice from friday afternoon Q&A"""

def read_line_of_ints(text):
    ints = []
    ints_as_strs = split_line(text)
    for int_as_str in ints_as_strs:
        ints.append(int(int_as_str))

def split_line(line):
    return line.split()


# def test_can_read_line_of_ints():
#     text = "10 12 9 345 2 78"
#     assert read_line_of_ints(text) == [10, 12, 9, 345, 2, 78]

if __name__ == "__main__":
    text = "10 12 9 345 2 78"
    read_line_of_ints(text)

###################################################

def read_file_into_list(filename):
        """given a file, return a list of each line in the file as a string."""
        with open(filename) as file:
                return file.readlines()

def read_file_into_ints(filename):
        lines = read_file_into_list(filename)

        list_of_lists = []
        for line in lines:
                list_of_lists.append(read_line_of_ints(lines))
        return list_of_lists

######################################################


class ElevationMap:
        """
        ElevationMap is a class that takes a matrix (list of lists, 2D) of integers and can be used to generate an image of those elevations like a standard elevation map.
        """

        def __init__(self, elevations):
                self.elevations = elevations
                
        def elevation_at_coordinate(self, x, y):
                return self.elevations[y][x]

        """ have to reverse numbers in matrix ex. list y coordinate first, then list x coordinate to find the point on the axis you want
        """

        def min_elevation(self):
                return min([min(row) for row in self.elevations])

        def max_elevations(self):
                return max([min(row) for row in self.elevations])
        
        def intensity_at_coordinate(self, x, y):
                elevation = self.elevation_at_coordinate(x, y)
                min_elevation = self.min_elevation()
                max_elevation = self.max_elevation()

                return (elevation - min_elevation) / (max_elevation)

elevations = read_file_into_ints()
e_Map = ElevationMap(elevations)

##############################
#using PIL

def draw_grayscale_gradient(self, filename, width, heigh):
        image = PIL>Image.new(mode='L', size=(width, height))
        for x in range(width):
                for y in range(heigh):
                        image.draw((x, y), (int(x / width * 255))
        image.save(filename)

