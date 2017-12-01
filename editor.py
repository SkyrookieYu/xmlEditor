# pylint: disable=C0103,C0111,W0614,W0401,C0200,C0325,C1001
from Tkinter import *
import tkFileDialog
import xml.etree.ElementTree as ET

##
# xmlEditor is a WYSIWYG xml editor
##


class XMLGui:
    def __init__(self, master):
        self.master = master
        self.title = "XML Editor"
        self.xml_root = None
        master.title(self.title)

    def loadFile(self):
        filename = tkFileDialog.askopenfilename(initialdir=".", title="Select file", filetypes=(
            ("xml files", "*.xml"), ("all files", "*.*")))
        xml_file_tree = ET.parse(filename)
        self.xml_root = xml_file_tree.getroot()
        self.renderData()

    def saveFile(self):
        print "Save here"

    def renderData(self):
        for child in self.xml_root:
            print child.tag + ", " + str(child.attrib) + " = " + child.text

    def getTitle(self):
        print self.title

# End class XMLGui

### CODE ENTRY ###
tree = ET.parse("samples/food.xml")
for elem in tree.iter():
    print elem
    #print child.tag + ", " + str(child.attrib) + " = " + child.text

# root = Tk()
# xml_gui = XMLGui(root)
# menubar = Menu(root)

# filemenu = Menu(menubar, tearoff=0)
# filemenu.add_command(label="Open", command=xml_gui.loadFile)
# filemenu.add_command(label="Save", command=xml_gui.loadFile)
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=root.quit)

# menubar.add_cascade(label="File", menu=filemenu)

# root.config(menu=menubar)
# root.mainloop()
