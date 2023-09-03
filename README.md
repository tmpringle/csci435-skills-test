# CSCI 435 - Programming Skills Test by Tyler Pringle
## Setup & Operation
The codebase uses Python, so make sure you have at least **Python 3.8** installed.
1. Clone this repository to your device.
2. In a terminal, go into the root directory (`cd csci435-skills-test`) for this repo.
3. Install the necessary library: `pip3 install -r requirements.txt`
4. Run the `main.py` file: `python3 ./main.py`

Once the Python code annotates the screenshots, the annotated screenshots can be found in the output folder.

## My solution
At a high level, my code:
1. Finds all XML files in the input folder
2. Parses an XML file to find the leaf nodes and temporarily store them in a list
3. Opens the screenshot corresponding to the XML file for drawing
4. For each leaf node:
   1. Parses the node to get the information for where that leaf node is on screen
   2. Draws a yellow box around the node in the screenshot using the node's location information
5. Saves the annotated screenshot in the output folder
6. Repeats steps 2-5 for each XML file

## Design decisions
I chose to use Python since I figured the project's code would be a relatively small script to run. I also got more familiar with Python over the summer, so it made sense to keep using it for this project.

In terms of code, one thing that was not clear at first was how exactly I would parse XML files to find their leaf nodes. After finding the XML parser I would use, I decided to go for a recursive approach to finding and storing the leaf nodes. Since the GUI is tree-based (and the fact that the XML parser I found also treats XML files as tree structures), it made sense to use a tree-traversal approach that I learned in previous CS classes.

I chose the Pillow library for drawing and the ElementTree API for XML parsing simply because they were some of the first tools I found while researching how to do drawing/XML parsing. They are also quite easy to use.
