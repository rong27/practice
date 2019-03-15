import xml.etree.ElementTree as ET
import sys

# tree = ET.ElementTree(file = "C:\\Users\\joy.lin\\Desktop\\branch.xml")

# root = tree.getroot()
# print(root)
# print(root.tag, root.attrib)

# for child_of_root in root:
#     print('tag: ',child_of_root.tag, '| attrib: ',child_of_root.attrib, '| text: ',child_of_root.text)

# #iter : 可以對某個元素對象之下,所有的子元素進行深度優先搜尋(Depth-First Search;DFS)
# for elem in tree.iter():
#     print(elem.tag, elem.attrib)

# print('------use Xpath------')
# #use XPath to find element
# for XPath_elem in tree.iterfind('branch/sub-branch'):
#     print('tag: ', XPath_elem.tag, '| attrib: ', XPath_elem.attrib, '| text: ', XPath_elem.text)


# # modify an xml file
# root = tree.getroot()
# print(root)
# del root[2] # delete the third child-element
# root[0].set('foo', 'bar')

# for subelem in root:
#     print(subelem.tag, subelem.attrib)

# # 將這個tree寫到新的文件中:
# tree.write('C:\\Users\\joy.lin\\Desktop\\branchOut.xml')

# # build an xml file
# elem = ET.Element('elem')
# child1 = ET.SubElement(elem, 'child1')
# child1.text = 'some text'
# child2 = ET.SubElement(elem, 'child2')
# elemb = ET.Element('elem_b')
# root = ET.Element('root')
# child3 = ET.SubElement(elem, 'child3')
# child3.text = 'This is child3'
# root.extend((elem, elemb))
# tree = ET.ElementTree(root)
# tree.write('C:\\Users\\joy.lin\\Desktop\\buildnew.xml')

tree = ET.ElementTree(file = 'C:\\Users\\joy.lin\\Desktop\\polygonarrangeIn.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib, child.text)

for rotatepolygon in root.iter('rotatepolygon'):
    print(rotatepolygon.tag)

