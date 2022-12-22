import pandas as pd
import xml.etree.cElementTree as et

root=et.Element("dictionary")

#Son
excel_data = pd.read_excel('son.xlsx')
data = pd.DataFrame(excel_data, columns=['id', 'word', 'property'])

l=len(data)
for i in range(l):
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='son', id=str(data['id'][i]), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1]
    else:
        et.SubElement(root, "word", classId='son', id=str(data['id'][i]), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i])

tree = et.ElementTree(root)
tree.write("word.xml", xml_declaration=True, encoding='utf-8')
