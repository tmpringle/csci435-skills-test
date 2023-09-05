from PIL import Image, ImageDraw
import xml.etree.ElementTree as ET
import sys

# Sources:
# Drawing using Pillow
# https://www.blog.pythonlibrary.org/2021/02/23/drawing-shapes-on-images-with-python-and-pillow/
#
# XML parsing in Python
# https://docs.python.org/3/library/xml.etree.elementtree.html
#
# Getting all files with extension in Python
# https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python

# global variable to store the current XML file's leaf nodes
leaf_nodes = []

# traverses the tree of XML nodes to file the XML file's leaf nodes
# and appends the leaf nodes to a list
def find_leaves(root):
    root_iterator = root.iter()
    next(root_iterator)
    if next(root_iterator, None) is None:   # passed-in node is a leaf node
        leaf_nodes.append(root)
    else:
        for child in root:
            find_leaves(child)

# parses the bounds attribute to get the xy coordinates for leaf node
# boundaries and returns them in a list corresponding to [x1, y1, x2, y2]
def get_bounds_list(bounds_str):
    bounds_list = bounds_str.split(",")
    bounds_list[0] = int(bounds_list[0][1:])
    bounds_list[-1] = int(bounds_list[-1][:-1])
    bounds_list[1] = bounds_list[1].split("][")
    bounds_list.insert(2, int(bounds_list[1][1]))
    bounds_list[1] = int(bounds_list[1][0])
    return bounds_list

if __name__ == "__main__":
    xml_files = []

    # gets all XML files passed in through the command line
    for i in range(1, len(sys.argv)):
        xml_files.append(sys.argv[i])

    for xml_file in xml_files:
        # gets the leaf nodes for an XML file
        tree = ET.parse(xml_file)
        root = tree.getroot()
        find_leaves(root)

        # opens up the image corresponding to the current XML file
        # and gets ready to draw on it
        image = Image.open(xml_file[:-3] + "png")
        draw = ImageDraw.Draw(image)

        for leaf in leaf_nodes:
            # gets the xy coordinates for the boundaries of
            # the current leaf node
            bounds_list = get_bounds_list(leaf.get("bounds"))
            x1 = bounds_list[0]
            y1 = bounds_list[1]
            x2 = bounds_list[2]
            y2 = bounds_list[3]

            # draws yellow rectangle around leaf node on screenshot
            draw.rectangle((x1, y1, x2, y2), outline="yellow", width=10)
        
        # saves annotated screenshot in output directory
        image.save("./output/" + xml_file[:-3] + "png")

        # resets global leaf nodes list for next XML file
        leaf_nodes = []