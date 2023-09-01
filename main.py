from PIL import Image, ImageDraw
import xml.etree.ElementTree as ET
import os

leaf_nodes = []

# Sources:
# Drawing using Pillow
# https://www.blog.pythonlibrary.org/2021/02/23/drawing-shapes-on-images-with-python-and-pillow/
#
# XML parsing in Python
# https://docs.python.org/3/library/xml.etree.elementtree.html
#
# Getting all files with extension in Python
# https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python

def find_leaves(root):
    root_iterator = root.iter()
    next(root_iterator)
    if next(root_iterator, None) is None:
        leaf_nodes.append(root)
    else:
        for child in root:
            find_leaves(child, leaf_nodes)

def get_bounds_list(bounds_str):
    bounds_list = bounds_str.split(',')
    bounds_list[0] = int(bounds_list[0][1:])
    bounds_list[-1] = int(bounds_list[-1][:-1])
    bounds_list[1] = bounds_list[1].split('][')
    bounds_list.insert(2, int(bounds_list[1][1]))
    bounds_list[1] = int(bounds_list[1][0])
    return bounds_list

xml_files = []

for file in os.listdir("./input"):
    if file.endswith(".xml"):
        xml_files.append("./input/" + file)

print(xml_files)

# for xml_file in xml_files:
#     tree = ET.parse(xml_file)
#     root = tree.getroot()
#     find_leaves(root)

#     for leaf in leaf_nodes:
#         bounds_list = get_bounds_list(leaf.get('bounds'))

#         image = Image.open(xml_file[:-3] + "png")
#         draw = ImageDraw.Draw(image)

#         draw.rectangle(bounds_list, outline="yellow", width=10)
#         image.save('./output/com.apalon.ringtones.png')