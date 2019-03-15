import os
from xml.etree.ElementTree import parse
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element

# 加載並解析xml
tree = ElementTree(file='C:\\Users\\joy.lin\\Desktop\\polygonarrange.xml')
# 抓根結點元素
root = tree.getroot() 
print('root: ',root)  # 根結點 是 annotation
print('tag: ', root.tag)
print('attribute: ', root.attrib)

# 找到annotation的子節點:

for child_of_root in root:
    print(child_of_root.tag, child_of_root.attrib, child_of_root.text)

# print('tag_root[0]: ', root[0].tag, ',', 'text_root[0]: ', root[0].text)

# for elem in tree.iter():
#     print(elem.tag, elem.text)



rotatepolygon = Element('rotatepolygon')