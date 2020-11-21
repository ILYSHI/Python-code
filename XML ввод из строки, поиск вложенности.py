from xml.etree import ElementTree

root = ElementTree.fromstring(input())

dict = {'red':0,
        'green':0,
        'blue':0
}

def child(root,n): # n - степень вложенности
    color = root.attrib['color']
    dict[color]+=n
    for childs in root:
        child(childs,n+1)
child(root,1)
print(dict['red'],dict['green'],dict['blue'])

