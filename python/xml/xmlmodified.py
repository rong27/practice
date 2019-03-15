# learning source: https://blog.csdn.net/wklken/article/details/7603071

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element

'''讀取並解析xml文件,
in_path : xml路徑
return: ElementTree'''
def read_xml(in_path):
    tree = ElementTree()
    tree.parse(in_path)
    return tree 

'''將xml文件寫出,
tree: xml樹,
out_path:寫出路徑'''
def write_xml(tree, out_path):
    tree.write(out_path, encoding="utf-8", xml_declaration=True)

'''判斷某個節點是否包含所有傳入參數屬性,
node: 節點,
kv_map: 屬性及屬性值組成的map'''
def if_math(node, kv_map):
    for key in kv_map:
        if node.get(key) != kv_map.get(key):
            return False
    return True

'''查找某個路徑匹配的所有節點,
tree: xml樹,
path: 節點路徑'''
def find_nodes(tree, path):
    return tree.findall(path)

'''根據屬性及屬性值定位符合的節點,返回節點,
nodelist: 節點列表,
kv_map: 匹配屬性及屬性值map'''
def get_node_by_keyvalue(nodelist, kv_map):
    result_nodes = []
    for node in nodelist:
        if if_math(node, kv_map):
            result_nodes.append(node)
    return result_nodes

'''修改/增加/刪除 節點的屬性及屬性值'''
def change_node_properties(nodelist, kv_map, is_delete=False):
    for node in nodelist:
        for key in kv_map:
            if is_delete:
                if key in node.attrib:
                    if key in node.attrib[key]:
                        del node.attrib[key]

                else:
                    node.set(key, kv_map.gey(key))

''' 改變/增加/刪除一個節點的文本
text: 更新後的文本'''
def change_node_text(nodelist, text, is_add=False, is_delete=False):
    for node in nodelist:
        if is_add:
            node.text += text
        elif is_delete:
            node.text = ""
        else:
            node.text = text
        
'''新造一個節點
tag: 節點標籤
property_map: 屬性及屬性值map
content: 節點閉合標籤裡的文本內容
return 新節點'''
def create_node(tag, property_map, content):
    element = Element(tag, property_map)
    element.text = content
    return element

'''給一個節點添加子節點'''
def add_child_node(nodelist, element):
    for node in nodelist:
        node.append(element)

'''同過屬性及屬性值訂為一個節點，並刪除'''
def del_node_by_tagkeyvalue(nodelist, tag, kv_map):
    for parent_node in nodelist:
        children = parent_node.getchildren()
        for child in children:
            if child.tag == tag and if_math(child, kv_map):
                parent_node.remove(child)

    

# if __name__ == "__main__":
    #讀取xml文件
tree = read_xml("C:\\Users\\joy.lin\\Desktop\\polygonarrangeIn.xml")
print("tree: ",tree)

root = tree.getroot()
print("root: ",root)
print('attribute: ', root.attrib)

    #屬性修改
    #找到父節點
nodes = find_nodes(tree, "database")
print("nodes: ",nodes)

    #屬性修改
    #通過屬性準確定位子節點
    # result_nodes =get_node_by_keyvalue(nodes, {"name":"BProcesser"})
    # print("result_nodes: ", result_nodes)

    # 屬性修改
    # #修改節點屬性
    # change_node_properties(result_nodes, {"age":"1"})

    #屬性修改
    # #刪除節點屬性
    # change_node_properties(result_nodes, {"value":""}, True)

    #節點修改
    #新建節點
    # a = create_node("person", {"age":"15","money":"200000"}, "this is the firest content")

    #節點修改
    #將新建的節點插入到父節點之下
    # add_child_node(result_nodes, a)

    #刪除節點
    #定位父節點
    # del_parent_nodes = find_nodes(tree, "processers/services/service")
    #刪除節點
    #準確定位子節點並刪除之
    # del_node_by_tagkeyvalue(del_parent_nodes, "chain", {"sequency":"chain1"})
 

    #修改節點文本
    #定位節點
    # text_nodes = get_node_by_keyvalue(find_nodes(tree, "processers/services/service/chain"),{"sequency":"chain3"})
    # change_node_text(text_nodes, "new text")

    #輸出結果到文件
    # write_xml(tree, "C:\\Users\\joy.lin\\Desktop\\polygonarrangeOut.xml")


    

